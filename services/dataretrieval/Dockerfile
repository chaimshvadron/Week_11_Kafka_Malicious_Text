FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY services/dataretrieval/ ./services/dataretrieval/
COPY shared/ ./shared/

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "services.dataretrieval.dataretrieval_service"]
