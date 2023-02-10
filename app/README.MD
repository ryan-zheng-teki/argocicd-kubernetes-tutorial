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




```yaml

(1)start a process for us
(2)stop a process for us
(3)monitor a process for us. Automatically restart the process when its down


Kubelet 
class Pod {
  metadata: Array<string> 
  
  start() {
     call docker run
  }
}

acceptYaml(inputConfig: YAML) {
   pod = new Pod()
   pod.imageId = 
   pod.start()
}


docker run given the image id
```


