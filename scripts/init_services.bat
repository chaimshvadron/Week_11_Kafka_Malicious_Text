# Login to Docker
docker login

# Build the Docker image for the retriever service
docker build -f services/retriever/Dockerfile -t chaimshvadron/retriever:latest .

# Push the Docker image to the repository
docker push chaimshvadron/retriever:latest