@echo off
REM Build and push all service images to Docker Hub

set REPO=chaimshvadron/iranian-terror-tweets-hunter

REM Build images

docker build -t %REPO%-retriever:latest -f services/retriever/Dockerfile .
docker build -t %REPO%-preprocessor:latest -f services/preprocessor/Dockerfile .
docker build -t %REPO%-enricher:latest -f services/enricher/Dockerfile .
docker build -t %REPO%-persister:latest -f services/persister/Dockerfile .
docker build -t %REPO%-dataretrieval:latest -f services/dataretrieval/Dockerfile .

REM Push images

docker push %REPO%-retriever:latest
docker push %REPO%-preprocessor:latest
docker push %REPO%-enricher:latest
docker push %REPO%-persister:latest
docker push %REPO%-dataretrieval:latest

echo All images built and pushed successfully!
