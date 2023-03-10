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
helm install myflask . -n staging
helm uninstall myflask  # to uninstall
helm list --namespace [namespace-name]

helm upgrade -f myflask/values.yaml myflask  ./myflask -n staging # upgrade helm chart
helm install myflask . --debug --dry-run # use dry run to see the helm chart values
```
helm upgrade -f values.yaml 

## Use helm to deploy ingress

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx # add repo for ingress-nginx 
helm search repo ingress-nginx search charts in repo
helm pull ingress-nginx/ingress-nginx  # this will pull the chart to local system, then we can update the chart
helm upgrade -f values.yaml --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace


Installation Of Argo Workflow And ArgoCD To Build A Pipeline



Use Argo Workflow To Create CI Pipeline



Use ArgoCD to deploy the built image \n 





