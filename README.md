# 🚀 Docker Fast App

Aplicación web full stack utilizando Docker con arquitectura de 3 capas:

- 🟦 Frontend (Node.js + serve)
- 🟩 Backend (Flask - Python)
- 🟨 Base de datos (MySQL)

---

## 🧱 Estructura del proyecto
docker-fast-app/
│
├── frontend/
│ ├── index.html
│ ├── package.json
│ └── Dockerfile
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── db/
│ └── init.sql
│
└── docker-compose.yml


---

## ⚙️ Tecnologías utilizadas

- Docker
- Docker Compose
- Python (Flask)
- MySQL
- Node.js

---

## ▶️ Ejecución del proyecto

```bash
docker-compose up --build

---

## 🌐 Acceso a la aplicación
Frontend: http://localhost:3000
Backend: http://localhost:5000
API endpoint: http://localhost:5000/list
