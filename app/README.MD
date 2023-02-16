Build docker image, inside minikube cluster

```javascript
eval $(minikube docker-env)

./build.sh && docker image prune  (prune will remove dangling image after the rebuild)
```

 \n Rolling Update For The Deployment


1. apply the initial deployment.yaml. kubectl apply -f
2. Rebuild the image. The image contains hash value
3. Update the yaml with the specific image
4. kubectl apply -f flask-deploy.yaml again.
5. kubectl rollout status deployment myflask => check the deployment status \n 

Horizontal Scaling Test using k6 load test

<https://k6.io/docs/get-started/installation/>


You should also use minikube mount to mount data folder from localhost to minikube docker container.


