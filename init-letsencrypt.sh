#!/bin/bash

# =============================================================================
# init-letsencrypt.sh — One-time SSL bootstrap for wayffs-api.edioq.com
# =============================================================================
# Run this script ONCE on the EC2 server to obtain the initial SSL certificate.
# After that, the certbot container in docker-compose.prod.yml handles renewals.
#
# Usage:
#   sudo bash init-letsencrypt.sh
#
# Prerequisites:
#   - Port 443 must be open in the EC2 Security Group
#   - DNS A record for the domain must point to this server's IP
# =============================================================================

set -e

# ─── CONFIGURATION ──────────────────────────────────────────────────────────
# Values are pulled from .env automatically

if [ -f ".env" ]; then
    API_DOMAIN=$(grep '^API_DOMAIN=' .env | cut -d '=' -f2)
    LETSENCRYPT_EMAIL=$(grep '^LETSENCRYPT_EMAIL=' .env | cut -d '=' -f2)
else
    echo "ERROR: .env not found. Please ensure it exists in the current directory."
    exit 1
fi

if [ -z "$API_DOMAIN" ]; then
    echo "ERROR: API_DOMAIN is not set in .env"
    exit 1
fi

if [ -z "$LETSENCRYPT_EMAIL" ]; then
    echo "ERROR: LETSENCRYPT_EMAIL is not set in .env"
    exit 1
fi

domains=($API_DOMAIN)
email=$LETSENCRYPT_EMAIL
staging=0  # Set to 1 to test against Let's Encrypt staging (no rate limits)
data_path="./certbot"
compose_file="docker-compose.prod.yml"

# ─── PREFLIGHT ───────────────────────────────────────────────────────────────

if [ -z "$email" ]; then
  echo "ERROR: Please set your email address in this script (line 24)."
  echo "       Let's Encrypt requires an email for certificate notifications."
  exit 1
fi

if ! [ -x "$(command -v docker)" ]; then
  echo "ERROR: docker is not installed." >&2
  exit 1
fi

echo "=== SSL Certificate Bootstrap for ${domains[0]} ==="
echo ""

# ─── STEP 1: Download recommended TLS parameters ────────────────────────────

echo "### Downloading recommended TLS parameters ..."
mkdir -p "$data_path/conf"

if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot/certbot/ssl-dhparams.pem > "$data_path/conf/ssl-dhparams.pem"
  echo "   ✓ Downloaded TLS parameters"
else
  echo "   ✓ TLS parameters already exist, skipping"
fi

# ─── STEP 2: Create dummy certificate so Nginx can start ────────────────────

echo "### Creating dummy certificate for ${domains[0]} ..."
cert_path="$data_path/conf/live/${domains[0]}"
mkdir -p "$cert_path"

docker compose -f "$compose_file" run --rm --entrypoint "\
  openssl req -x509 -nodes -newkey rsa:4096 -days 1 \
    -keyout '/etc/letsencrypt/live/${domains[0]}/privkey.pem' \
    -out '/etc/letsencrypt/live/${domains[0]}/fullchain.pem' \
    -subj '/CN=localhost'" certbot
echo "   ✓ Dummy certificate created"

# ─── STEP 3: Start Nginx with dummy cert ────────────────────────────────────

echo "### Starting Nginx ..."
docker compose -f "$compose_file" up --force-recreate -d nginx
echo "   ✓ Nginx is running"

# ─── STEP 4: Delete dummy cert and request real one ─────────────────────────

echo "### Deleting dummy certificate ..."
docker compose -f "$compose_file" run --rm --entrypoint "\
  rm -Rf /etc/letsencrypt/live/${domains[0]} && \
  rm -Rf /etc/letsencrypt/archive/${domains[0]} && \
  rm -Rf /etc/letsencrypt/renewal/${domains[0]}.conf" certbot
echo "   ✓ Dummy certificate removed"

echo "### Requesting Let's Encrypt certificate for ${domains[0]} ..."

# Build domain args
domain_args=""
for domain in "${domains[@]}"; do
  domain_args="$domain_args -d $domain"
done

# Use staging server if requested
if [ $staging != "0" ]; then
  staging_arg="--staging"
  echo "   ⚠ Using Let's Encrypt STAGING server (cert won't be trusted)"
else
  staging_arg=""
fi

docker compose -f "$compose_file" run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    --email $email \
    $domain_args \
    --rsa-key-size 4096 \
    --agree-tos \
    --no-eff-email \
    --force-renewal" certbot
echo "   ✓ Certificate obtained!"

# ─── STEP 5: Reload Nginx with real cert ────────────────────────────────────

echo "### Reloading Nginx with the real certificate ..."
docker compose -f "$compose_file" exec nginx nginx -s reload
echo "   ✓ Nginx reloaded"

# ─── STEP 6: Start all services ─────────────────────────────────────────────

echo "### Starting all production services ..."
docker compose -f "$compose_file" up -d
echo "   ✓ All services running"

echo ""
echo "=============================================="
echo "  ✅ SSL setup complete!"
echo "  🔒 https://${domains[0]} is now live"
echo "  🔄 Auto-renewal is handled by the certbot container"
echo "=============================================="
