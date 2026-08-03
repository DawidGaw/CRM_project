# CRM System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.x-success)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Redis](https://img.shields.io/badge/Redis-7-red)
![Celery](https://img.shields.io/badge/Celery-Enabled-green)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![AWS](https://img.shields.io/badge/AWS-Elastic_Beanstalk-orange)

A modern **Customer Relationship Management (CRM)** application built with **Django**.

The project demonstrates backend development using **PostgreSQL**, **Redis**, **Celery**, **Docker**, and deployment to **AWS Elastic Beanstalk**.

---

## Features

- User authentication and authorization
- Custom user model
- Client management (CRUD)
- Deal management
- Task management
- Notification system
- Dashboard
- Asynchronous background tasks with Celery
- Scheduled tasks with Celery Beat
- PostgreSQL database
- Dockerized development environment
- AWS Elastic Beanstalk deployment

---

## Tech Stack

| Category | Technology                       |
|----------|----------------------------------|
| Language | Python 3.13                      |
| Framework | Django                           |
| Database | PostgreSQL                       |
| Background Tasks | Celery / Celery Beat             |
| Message Broker | Redis                            |
| Containerization | Docker & Docker Compose          |
| Cloud | AWS Elastic Beanstalk / S3 / RDS |
| Frontend | Bootstrap 5                      |

---

## Project Structure

```
core/             Django project configuration
clients/          Client management
deals/            Deal management
tasks/            Task management
notifications/    Notification system
users/            Authentication and user management
```

---

## Getting Started

### Clone the repository

```bash
git clone <repository-url>

cd CRM
```

### Configure environment variables

```bash
cp .env.dist .env
```

Update the `.env` file with your own configuration.

### Start the application

```bash
docker compose up --build
```

### Apply database migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

The application will be available at:

```
http://localhost:8000
```

---

## Docker Services

| Service | Port |
|----------|------|
| Django | 8000 |
| PostgreSQL | 5432 |
| Redis | 6379 |
| Flower | 5555 |

---

## Celery

Start Celery Worker:

```bash
docker compose up celery
```

Start Celery Beat:

```bash
docker compose up celery-beat
```

Start Flower:

```bash
docker compose up flower
```

Flower Dashboard:

```
http://localhost:5555
```

---

## Deployment

The application is configured for deployment to **AWS Elastic Beanstalk**.

```bash
eb init
eb create
eb deploy
```
---

## Author

Developed as a portfolio project demonstrating modern backend development with Django, Docker, Celery and AWS.