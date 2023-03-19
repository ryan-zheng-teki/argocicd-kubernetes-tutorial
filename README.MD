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



Installation Of Kubernetes On Server


install openvpn on our server

install docker runtime before install kubernetes <https://www.cloudsigma.com/how-to-install-operate-docker-on-ubuntu-in-the-public-cloud/>

follow the website to install the kubernetes <https://www.cloudsigma.com/how-to-install-and-use-kubernetes-on-ubuntu-20-04/>


kubectl apply -f <https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml>

kubectl apply -f <https://raw.githubusercontent.com/coreos/flannel/master/Documentation/k8s-manifests/kube-flannel-rbac.yml>


Download remote kubeConfig to local system

## merge the master node config to the local .kube/config file

```javascript
scp -P 40110 user@ip:~:/home/ubs/.kube/config ~/Downloads/kubeconfig
```

 \n 

```javascript
cp ~/.kube/config ~/.kube/config.bak && KUBECONFIG=~/.kube/config:/home/ryan/Downloads/kubeconfig kubectl config view --flatten > /tmp/config && mv /tmp/config ~/.kube/config
```



```javascript
scp -P 40110 user@remote_ip:/path/to/remote/kube/config ~/.kube/config
```

 \n 


sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --apiserver-advertise-address=0.0.0.0

```javascript
ssh -L 6443:10.60.0.4:6443 user@ip -p 40110
```

 \n 

After installing this, i get the following message


Installation Of Argo Workflow And ArgoCD To Build A Pipeline

Create event source

kubectl apply -f ci/event/eventsource.yaml -n staging



Use Argo Workflow To Create CI Pipeline



Use ArgoCD to deploy the built image \n 

Question: how can we use environment variable to update the image id in helmchat values.yaml?

Antwort: set IMAGE_ID environment variable, then use






