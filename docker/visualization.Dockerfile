FROM python:3.9-slim

WORKDIR /app

COPY services/visualization/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/visualization/ .

CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]
