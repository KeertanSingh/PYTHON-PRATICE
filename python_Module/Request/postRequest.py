import re
import requests

# creating payload which we will post 
payload = {
    'username':'admin', 
    'password':'1234'
}

# making post request 
post = requests.post('https://httpbin.org/post', data=payload)

# making get request 
get = requests.get('https://httpbin.org/get', params=payload)

print(get.url)

print(post)
print(post.url)