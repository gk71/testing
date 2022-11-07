#!/bin/sh

kubectl apply -f srvs.yaml
kubectl apply -f assignment.yaml

sleep 120

python3 reverse.py
