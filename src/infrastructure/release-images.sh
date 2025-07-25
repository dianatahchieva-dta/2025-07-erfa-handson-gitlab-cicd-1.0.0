if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <version-tag>"
    echo "Example: $0 1.2.3"
    exit 1
fi

VERSION_TAG="$1"

docker build -f Dockerfile.gitlab -t "gitlabcicdhandson001.azurecr.io/erfa-gitlab:${VERSION_TAG}" .
docker build -f Dockerfile.gitlab-runner -t "gitlabcicdhandson001.azurecr.io/erfa-gitlab-runner:${VERSION_TAG}" .

# Push the images to the ACR
#az login
#az acr login -n gitlabcicdhandson001
#docker push "gitlabcicdhandson001.azurecr.io/erfa-gitlab:${VERSION_TAG}"
#docker push "gitlabcicdhandson001.azurecr.io/erfa-gitlab-runner:${VERSION_TAG}"
