
FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY CRM .

CMD ["python", "CRM/manage.py", "runserver", "0.0.0.0:8000"]
