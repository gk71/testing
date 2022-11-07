creating docker image using the Dockerfile
----> docker build -t <tagname> .

To download the image to local:
----> minikube ssh docker pull <image:tagname>

To create a service on minikube execute the following:
----> kubectl apply -f srvs.yaml

To create the required deployment execute the following command:
---->kubectl apply -f assignment.yaml

The above steps will create a containerized python web application.

To reverse the message displayed on the web application, run the application reverse.py
----> python3 reverse.py


--------------------------------------------------------
The task of deployment of containarized application and the application to reverse the message can be achieved by executing the below script.
--> chmod 777 script.sh
--> ./script.sh

