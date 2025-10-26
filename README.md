# Flask + Redis Multi-Container App

## 📋 About This Project
A simple web application demonstrating Docker multi-container architecture with Flask and Redis.

This was my first multi-container Docker project where I learned how to orchestrate multiple services using Docker Compose.

## 🚀 Features
- Flask web server with two routes
- Redis database for persistent visit counter
- Multi-container setup with Docker Compose
- Data persists across container restarts

## 🛠️ Technologies Used
- Python 3.9
- Flask 3.0.0
- Redis 7
- Docker & Docker Compose

## 📦 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/roodyadam/flask-reds-docker.git
cd flask-reds-docker
```

2. **Build and start the containers:**
```bash
docker-compose up --build
```

3. **Visit in your browser:**
- Welcome page: `http://localhost:5001`
- Counter page: `http://localhost:5001/count`

4. **Stop the application:**
Press `Ctrl+C`, then:
```bash
docker-compose down
```

## 📂 Project Structure
```
.
├── app.py                 # Flask application with routes
├── Dockerfile            # Docker configuration for Flask
├── requirements.txt      # Python dependencies
├── docker-compose.yml    # Multi-container orchestration
└── README.md            # This file
```

## 🧪 Testing the Application

1. Visit `http://localhost:5001` to see the welcome page
2. Click the link or go to `http://localhost:5001/count`
3. Refresh the page multiple times - the counter increments!
4. Stop and restart containers - the counter persists!

## 🎓 What I Learned

Building this project taught me:
- How to create Dockerfiles for Python applications
- Using Docker Compose to manage multiple containers
- Container networking and service communication
- Troubleshooting port conflicts and syntax errors
- Persistent data storage using Docker volumes
- Pushing Docker projects to GitHub

### Challenges I Overcame:
- Fixed port 5000 conflict by remapping to 5001
- Debugged Python syntax errors with backticks
- Corrected file naming (`requirement.txt` → `requirements.txt`)
- Understood Docker port mapping (internal vs external)

## 📝 How It Works

1. **Flask Application** runs on port 5000 inside the container
2. **Docker Compose** maps it to port 5001 on your machine
3. **Redis Database** stores the visit count persistently
4. **Docker Network** allows Flask and Redis to communicate
5. **Docker Volume** keeps Redis data even after restarts

## 🔮 Future Improvements

- [ ] Add user authentication
- [ ] Implement additional routes (reset counter, view history)
- [ ] Add health check endpoints
- [ ] Include error logging and monitoring
- [ ] Deploy to cloud platform (AWS/GCP)
- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Switch to PostgreSQL for relational data

## 👤 Author

Created by Roody Adam as a learning project for Docker and DevOps practices.

GitHub: [@roodyadam](https://github.com/roodyadam)

## 📄 License

This project is open source and available for learning purposes.
EOF
