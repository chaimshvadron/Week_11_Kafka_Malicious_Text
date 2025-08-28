FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY services/dataretrieval /app/services/dataretrieval
COPY shared /app/shared
ENV PYTHONUNBUFFERED=1
ENV NLTK_DATA=/app/resources/nltk_data
ENV PYTHONPATH=/app:/app/shared
EXPOSE 8000
CMD ["uvicorn", "services.dataretrieval.main:app", "--host", "0.0.0.0", "--port", "8000"]
