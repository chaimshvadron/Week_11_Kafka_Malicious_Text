FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY services/persister/ ./services/persister/
COPY shared/ ./shared/
COPY resources/nltk_data/ ./resources/nltk_data/

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "services.persister.main"]
