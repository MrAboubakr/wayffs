# Wayffs

Wayffs is an open-source project designed for simplicity, clarity, and security. It features a modern Django backend and a Vue.js frontend, containerized with Docker and ready for deployment on AWS.

## 🚀 Tech Stack

- **Backend**: Python (Django / Django Rest Framework)
- **Frontend**: Vue.js 3 (TypeScript, Vite)
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Hosting**: AWS EC2 (Free Tier Optimized)

## 🛠️ Quick Start

To get the entire development environment running (Database, Backend, and Frontend), simply run:

```bash
./dev.sh
```

This script will:
1. Start the PostgreSQL database container.
2. Run database migrations.
3. Start the Django backend (on port 8000).
4. Start the Vue frontend (on port 5173).

## 📂 Project Structure

- `/backend`: Django API and core business logic.
- `/frontend`: Vue.js application.
- `docker-compose.yml`: Handles service orchestration.
- `dev.sh`: Unified development startup script.

## 🤝 Contributing

We welcome community contributions! Please ensure your code follows the project's focus on simplicity and low resource usage.

---
*Created for community-driven development.*
