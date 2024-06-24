FROM python:3.9-slim

WORKDIR /app

COPY services/ai_model_creation/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/ai_model_creation/ .

CMD ["gunicorn", "--bind", "0.0.0.0:5003", "app:app"]
