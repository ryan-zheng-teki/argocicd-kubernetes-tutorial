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


## How to start server locally

uvicorn  app:app --host 0.0.0.0 --port 5000

## Performance Testing

k6 run loadtest.js


## Use helm to deploy

`cd helm/myflask`

```javascript
helm install myflask . --namespace [namespace-name]
helm uninstall myflask  # to uninstall
helm list --namespace [namespace-name]
```


Installation Of Argo Workflow And ArgoCD To Build A Pipeline



Use Argo Workflow To Create CI Pipeline



Use ArgoCD to deploy the built image \n 



