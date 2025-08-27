FROM python:3.11-slim

WORKDIR /app

COPY services /app/services
COPY shared /app/shared
COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app:/app/shared

CMD ["python", "-m", "services.retriever.main"]
