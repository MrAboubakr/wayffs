#!/bin/bash

# Function to handle cleanup on exit
cleanup() {
    echo ""
    echo "Stopping all services..."
    # Kill background jobs
    kill $(jobs -p) 2>/dev/null
    # Stop docker containers if they were started by this script
    docker compose stop db
    echo "Done."
    exit
}

# Trap SIGINT (Ctrl+C) and SIGTERM
trap cleanup SIGINT SIGTERM

echo "Starting Wayffs Development Environment..."

# 1. Start Database (PostgreSQL)
echo "Starting Database..."
# Use --remove-orphans and force recreate to avoid name conflicts
docker compose up -d --remove-orphans db

# Wait for DB to be ready
echo "Waiting for database to be ready..."
sleep 2

# Run Migrations
echo "Running Migrations..."
cd backend
if [ -f "venv/bin/python" ]; then
    ./venv/bin/python manage.py migrate
else
    echo "Warning: venv not found. Skipping migrations."
fi
cd ..

# 2. Start Backend
echo "Starting Backend..."
# Check if something is already running on 8000
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null ; then
    echo "Warning: Something is already running on port 8000. Skipping backend start."
else
    cd backend
    if [ -f "venv/bin/python" ]; then
        # Use the venv python directly to ensure Django is found
        ./venv/bin/python manage.py runserver &
        BACKEND_PID=$!
    else
        echo "Error: venv not found or python missing in venv. Please run 'python -m venv venv' and install requirements."
    fi
    cd ..
fi

# 3. Start Frontend
if [ "$SKIP_FRONTEND" = "1" ]; then
    echo "Skipping Frontend (SKIP_FRONTEND=1)..."
elif [ ! -d "frontend" ]; then
    echo "Skipping Frontend (frontend directory not found)..."
else
    echo "Starting Frontend..."
    # Check if something is already running on 5173
    if lsof -Pi :5173 -sTCP:LISTEN -t >/dev/null ; then
        echo "Warning: Something is already running on port 5173. Skipping frontend start."
    else
        cd frontend
        # Use --port 5173 to ensure it doesn't jump to 5174
        npm run dev -- --port 5173 &
        FRONTEND_PID=$!
        cd ..
    fi
fi

echo ""
echo "------------------------------------------------"
echo "Services are running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo "Press Ctrl+C to stop everything."
echo "------------------------------------------------"

# Wait for background processes
wait
