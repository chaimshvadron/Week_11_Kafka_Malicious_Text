FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app
COPY services/enricher /app/services/enricher
COPY shared /app/shared
COPY data /app/data
COPY resources/nltk_data /app/resources/nltk_data

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app:/app/shared
ENV NLTK_DATA=/app/resources/nltk_data

CMD ["python", "-m", "services.enricher.main"]
