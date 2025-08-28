FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY services/retriever /app/services/retriever
COPY shared /app/shared
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app:/app/shared
ENV NLTK_DATA=/app/resources/nltk_data

CMD ["python", "-m", "services.retriever.main"]
