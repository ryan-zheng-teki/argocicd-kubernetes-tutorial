Build docker image, inside minikube cluster

```javascript
eval $(minikube docker-env)

docker build -t myflask:v1 . && docker image prune  (prune will remove dangling image after the rebuild)
```

 \n 