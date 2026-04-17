# 🚀 Docker Fast App

![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![Python](https://img.shields.io/badge/Python-Flask-green?logo=python)
![Node](https://img.shields.io/badge/Node.js-Frontend-brightgreen?logo=node.js)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Status](https://img.shields.io/badge/Status-Running-success)

Aplicación web **full stack** basada en arquitectura desacoplada utilizando contenedores Docker.

---

## 🧱 Arquitectura del Proyecto

El sistema está compuesto por tres servicios independientes:

* 🟦 **Frontend:** Node.js (servidor estático con *serve*)
* 🟩 **Backend:** API REST con Flask (Python)
* 🟨 **Base de datos:** MySQL

---

## 🧠 Diagrama de Arquitectura

```id="diagram1"
        🌐 Usuario (Browser)
                 │
                 ▼
        ┌─────────────────┐
        │   Frontend      │
        │   (Node.js)     │
        │  Port: 3000     │
        └────────┬────────┘
                 │ HTTP
                 ▼
        ┌─────────────────┐
        │    Backend      │
        │   (Flask API)   │
        │  Port: 5000     │
        └────────┬────────┘
                 │ SQL
                 ▼
        ┌─────────────────┐
        │   MySQL DB      │
        │   Port: 3306    │
        └─────────────────┘

        🔗 Docker Network (internal)
```

---

## 🐳 Ejecución con Docker

Levanta todo el entorno con un solo comando:

```bash id="run1"
docker-compose up --build
```

---

## ⚙️ Arquitectura y Comunicación

* Cada servicio corre en su propio contenedor.
* Comunicación interna mediante red Docker.
* El backend accede a la base de datos usando `db` como hostname.
* Separación clara de responsabilidades.

---

## 🔄 Flujo de Funcionamiento

1. Usuario accede a `http://localhost:3000`
2. Frontend solicita datos al backend (`/list`)
3. Backend consulta MySQL
4. MySQL retorna datos
5. Backend responde en JSON
6. Frontend renderiza resultados

---

## 🌐 Endpoints

| Servicio | URL                        |
| -------- | -------------------------- |
| Frontend | http://localhost:3000      |
| Backend  | http://localhost:5000      |
| API      | http://localhost:5000/list |

---

## 🧪 Estado del Sistema

✔ mysql-db → running
✔ python-api → running
✔ react-app → running

Sistema completamente funcional en entorno Docker.

---

## 📌 Características

* ✔ No monolítico
* ✔ Modular
* ✔ Escalable (en teoría)
* ✔ Basado en contenedores

---

## 🧠 Descripción Técnica

Arquitectura desacoplada basada en contenedores, donde cada servicio opera de forma independiente dentro de una red Docker, permitiendo comunicación eficiente y despliegue reproducible.

---

## 📂 Estructura del Proyecto

```id="struct1"
docker-fast-app/
│
├── frontend/
│   ├── index.html
│   ├── package.json
│   └── Dockerfile
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── db/
│   └── init.sql
│
└── docker-compose.yml
```

---

## 🎥 Demo (opcional)

👉 Aquí puedes agregar:

* GIF del sistema funcionando
* Screenshot de Docker Desktop
* Captura del navegador con datos renderizados

---

## 👨‍💻 Autor

Desarrollado como proyecto práctico de arquitectura full stack con Docker.

