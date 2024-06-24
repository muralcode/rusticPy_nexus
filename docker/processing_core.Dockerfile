FROM python:3.9-slim

WORKDIR /app

COPY services/processing_core/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY rust_module/ /rust_module
RUN apt-get update && apt-get install -y build-essential
RUN cd /rust_module && cargo build --release
COPY services/processing_core/rust_bindings /rust_bindings
COPY rust_module/target/release/librust_module.so /rust_bindings/rust_module.so

COPY services/processing_core/ .

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "main:app"]
