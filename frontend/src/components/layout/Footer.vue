<template>
  <footer class="footer">
    <div class="footer__inner">
      <!-- Brand column -->
      <div class="footer__col footer__col--brand">
        <div class="footer__brand">
          <span class="footer__logo">W</span>
          <span class="footer__brand-text">Wayffs</span>
        </div>
        <p class="footer__description">
          Track your projects, collaborate with your team, and stay on top of every task.
        </p>
        <div class="footer__social">
          <a href="https://github.com" target="_blank" rel="noopener" class="footer__social-link" title="GitHub">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
            </svg>
          </a>
          <a href="#" class="footer__social-link" title="Twitter">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
          </a>
        </div>
      </div>

      <!-- Quick Links -->
      <div class="footer__col">
        <h4 class="footer__heading">Quick Links</h4>
        <router-link to="/" class="footer__link">Home</router-link>
        <router-link to="/login" class="footer__link">Login</router-link>
        <router-link to="/register" class="footer__link">Register</router-link>
      </div>

      <!-- Product -->
      <div class="footer__col">
        <h4 class="footer__heading">Product</h4>
        <a href="#features" class="footer__link">Features</a>
        <a href="#" class="footer__link">Pricing</a>
        <a href="#" class="footer__link">Documentation</a>
      </div>

      <!-- Contact -->
      <div class="footer__col">
        <h4 class="footer__heading">Contact</h4>
        <a href="mailto:hello@wayffs.com" class="footer__link">hello@wayffs.com</a>
        <a href="#" class="footer__link">Support</a>
      </div>
    </div>

    <div class="footer__bottom">
      <p>&copy; {{ currentYear }} Wayffs. All rights reserved.</p>
    </div>
  </footer>
</template>

<script setup lang="ts">
const currentYear = new Date().getFullYear();
</script>

<style scoped>
.footer {
  background: var(--wayfs-surface);
  border-top: 1px solid var(--wayfs-border);
  padding: 3rem 1.5rem 1.5rem;
  margin-top: auto;
}

:global(.dark) .footer {
  background: var(--color-dark-surface);
}

.footer__inner {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1fr;
  gap: 2rem;
}

.footer__brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}

.footer__logo {
  width: 32px;
  height: 32px;
  border-radius: 0.5rem;
  background: linear-gradient(135deg, #5634BA, #560DDE);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 1rem;
  color: #fff;
}

.footer__brand-text {
  font-weight: 800;
  font-size: 1.15rem;
  background: linear-gradient(135deg, #5634BA, #560DDE);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer__description {
  font-size: 0.85rem;
  color: var(--wayfs-text-secondary);
  line-height: 1.5;
  max-width: 280px;
  margin-bottom: 1rem;
}

.footer__social {
  display: flex;
  gap: 0.75rem;
}

.footer__social-link {
  width: 36px;
  height: 36px;
  border-radius: 0.5rem;
  border: 1px solid var(--wayfs-border);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--wayfs-text-secondary);
  transition: all 0.2s ease;
}

.footer__social-link:hover {
  color: #48C6CB;
  border-color: #48C6CB;
  background: rgba(72, 198, 203, 0.06);
}

.footer__heading {
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--wayfs-text);
  margin-bottom: 1rem;
}

.footer__link {
  display: block;
  text-decoration: none;
  font-size: 0.85rem;
  color: var(--wayfs-text-secondary);
  margin-bottom: 0.5rem;
  transition: color 0.2s ease;
}

.footer__link:hover {
  color: #48C6CB;
}

.footer__bottom {
  max-width: 1200px;
  margin: 2rem auto 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--wayfs-border);
  text-align: center;
  font-size: 0.8rem;
  color: var(--wayfs-text-secondary);
}

@media (max-width: 768px) {
  .footer__inner {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>
