import requests
import json
import jsonpath

a=requests.get("https://reqres.in/api/users?page=2")
print(a)
print("-----------------------")
print("request.content =",a.content) # get content
print("request.status_code =",a.status_code)
print("request.headers =",a.headers)
print("-----------------------")
#print(a.headers.avatar)

print("-----------------------")
b=json.loads(a.text)
print(b)
print("-----------------------")
c=jsonpath.jsonpath(b,'total_pages') #fetching 1st value from json
print("first value of api =",c[0])
#assert c[0]==4

print("--------------POST-----------------------------------------------------------")
# read input json

# with open('input_api.json','r') as abc:
#data = json.loads(abc)
#print("Type : ",type(data))

file =open('div.json',"r")
input_json=file.read()
req_json=json.loads(input_json) # returns JSON object as # a dictionary
#json.loads(jsonstring) #for Json string
#json.loads(fileobject.read()) #for fileobject
print(req_json)

rep=requests.post("https://reqres.in/api/users",req_json)

print("response.content =",rep.content)
print("-----------------------")
print("reponse.status_code =",rep.status_code)
print("-----------------------")
print("reponse.headers =",rep.headers)
print("-----------------------")
print("reponse.content-length =",rep.headers.get("content-length"))
print("-----------------------")
print("response.text =",rep.text)
print("-----------------------")
#parse response to json
response_json=json.loads(rep.text)
post=jsonpath.jsonpath(response_json,'id')
print(post)
print(post[0])
post1=jsonpath.jsonpath(response_json,'name')
print(post1[0])
post2=jsonpath.jsonpath(response_json,'age')
print(post2[0].key())
print(post2[0])