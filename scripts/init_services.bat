# Login to Docker
docker login

# Build the Docker image for the retriever service
docker build -f services/retriever/Dockerfile -t chaimshvadron/retriever:latest .

# Push the Docker image to the repository
docker push chaimshvadron/retriever:latest

# Build and push the Docker image for the persister service
docker build -f services/persister/Dockerfile -t chaimshvadron/persister:latest .
docker push chaimshvadron/persister:latest
