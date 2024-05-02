FROM python:alpine

WORKDIR /app

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]