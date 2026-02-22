#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo ""
    echo "Stopping all services..."
    docker compose down
    echo "Done."
    exit
}

# Trap SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

echo "Starting Wayffs Development Environment..."

# 1. Build and start all Docker services (DB + Backend + Frontend)
echo "Starting Docker services..."
DOCKER_BUILDKIT=0 docker compose --env-file .env up -d --build --remove-orphans db backend frontend

# Wait for DB to be ready
echo "Waiting for database to be ready..."
sleep 3

# 2. Run Migrations inside the backend container
echo "Running Migrations..."
docker compose exec backend python manage.py makemigrations --noinput
docker compose exec backend python manage.py migrate --noinput

# 3. Start Frontend locally
echo "Starting Frontend..."
cd frontend
npm run dev -- --port 5173 &
FRONTEND_PID=$!
cd ..

echo ""
echo "------------------------------------------------"
echo "Services are running!"
echo "Backend:  http://localhost:8000  (Docker)"
echo "Frontend: http://localhost:5173  (Local)"
echo "API Docs: http://localhost:8000/api/docs/"
echo "Press Ctrl+C to stop everything."
echo "------------------------------------------------"

# Follow Docker logs
docker compose logs -f


