# import urllib library
from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
# the url here is the ip of minikube and the node port of minikube defined in srvs.yaml
url = "http://192.168.49.2:30008/"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
#print(data_json)


#jsn_object = json.loads(data_json)

# printing keys and values
for i in data_json:
   if i == 'message':
      value = data_json[i]


print(value[::-1])

