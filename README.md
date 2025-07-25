# 2025-07-erfa-handson-gitlab-cicd
Hands-on ERFA about Gitlab CI/CD Pipelines

## Getting Started

### Prerequisites

1. Docker Desktop
2. Azure CLI
3. (only on Windows) WSL 2 incl. WSL integration on Docker Desktop
4. Local clone of this repo

### Setup the Lab
```bash
cd Lab_Setup

docker-compose up -d
```

### Login to Gitlab

http://localhost:8000

- Username: root
- Password: YourSecurePassword

## Build the infrastructure for later use
```bash
cd src/infrastructure
docker-compose up -d

# Modify the repositories and so on

docker-compose down

az login
az acr login -n gitlabcicdhandson001
./release-images.sh <semantic-version>
```
