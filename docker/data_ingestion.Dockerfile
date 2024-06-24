FROM python:3.9-slim

WORKDIR /app

COPY services/data_ingestion/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY services/data_ingestion/ .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
