# 🚀 Arpit Turukmare — Portfolio Website

> A personal portfolio web application built with Flask, deployed using a complete DevOps CI/CD pipeline.

## 📋 About

This project is a **DevOps Lab Practical** that demonstrates an end-to-end CI/CD pipeline using industry-standard tools. The application is a personal portfolio website showcasing projects, skills, and achievements.

**Student:** Arpit Turukmare  
**College:** Saraswati College of Engineering, Kharghar  
**Course:** B.E. Information Technology  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Application** | Python, Flask |
| **Testing** | pytest |
| **Version Control** | Git, GitHub |
| **CI/CD** | Jenkins |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes (Minikube) |
| **Cloud** | AWS EC2 (Ubuntu) |
| **Monitoring** | Health Check (`/health`) |

---

## 🔄 CI/CD Pipeline

```
GitHub → Jenkins → pytest → Docker → Kubernetes → AWS EC2 → Health Check
```

1. **GitHub** — Source code repository
2. **Jenkins** — Automates build and test pipeline
3. **pytest** — Runs automated tests
4. **Docker** — Containerizes the application
5. **Kubernetes** — Orchestrates container deployment
6. **AWS EC2** — Cloud hosting
7. **Health Check** — Monitors application status

---

## 📁 Project Structure

```
arpit-portfolio/
├── app.py                 # Flask application
├── test_app.py            # pytest test cases
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── Jenkinsfile            # Jenkins CI/CD pipeline
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── templates/
│   ├── base.html          # Base template with navbar
│   ├── index.html         # Homepage
│   ├── projects.html      # Projects page
│   ├── skills.html        # Skills page
│   └── achievements.html  # Achievements page
├── static/
│   └── style.css          # Stylesheet
└── k8s/
    ├── deployment.yaml    # Kubernetes Deployment
    └── service.yaml       # Kubernetes Service
```

---

## 🌐 Application Routes

| Route | Description |
|-------|-------------|
| `/` | Homepage — About me, contact, education |
| `/projects` | Projects — TechSentry, ScoreScope-AI, YOLOv8 |
| `/skills` | Technical skills organized by category |
| `/achievements` | Hackathon wins, certifications, timeline |
| `/health` | Health check — returns `{"status": "healthy"}` |

---

## ▶️ Run Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open in browser: http://localhost:5000
```

---

## 🧪 Run Tests

```bash
pytest test_app.py -v
```

---

## 🐳 Run with Docker

```bash
# Build image
docker build -t arpit-portfolio .

# Run container
docker run -d -p 5000:5000 --name arpit-portfolio arpit-portfolio

# Open in browser: http://localhost:5000
```

---

## ☸️ Run with Kubernetes (Minikube)

```bash
# Start Minikube
minikube start

# Build image inside Minikube
eval $(minikube docker-env)
docker build -t arpit-portfolio:latest .

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Get the URL
minikube service arpit-portfolio-service --url
```

---

## 📸 Screenshots

1. ✅ VS Code project files
2. ✅ Application running locally
3. ✅ pytest showing tests passed
4. ✅ GitHub repository
5. ✅ Jenkins successful build
6. ✅ AWS terminal showing `docker ps`
7. ✅ Application running via AWS public IP
8. ✅ `/health` endpoint showing healthy
9. ✅ Kubernetes pods running (`kubectl get pods`)

---

## 👤 Author

**Arpit Turukmare**  
📧 turukmarearpit@gmail.com  
📱 +91 9082158341  
🎓 Saraswati College of Engineering, Kharghar  

---

*Built with ❤️ as a DevOps Lab Practical Project © 2026*
