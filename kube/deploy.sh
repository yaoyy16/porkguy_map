kubectl delete rc porkguy-server-rc || true
kubectl create -f kube/service.yml
kubectl create -f kube/server-rc.yaml
kubectl get pod
