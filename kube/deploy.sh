kubectl delete rc porkguy-server-rc || true
kubectl create -f service.yml || true
kubectl create -f server-rc.yml
kubectl get pod
kubectl get service
