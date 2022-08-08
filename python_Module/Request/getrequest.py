# Begin by importing the Requests module:
import requests   
import json

# sending get request
r = requests.get("https://google.com")

# Will return webpage content 
content = r.text
# with open("google.html","w") as file:
    # file.write(content)

# Will return header 
header = r.headers
header = dict(header)
# with open("header.json", 'w') as file:
#         file.write(json.dumps(header))

#Will return encoded url 
url = r.url
# print(url)

# will return text encoding
encode = r.encoding
# print(encode)

# will return source code of website 
code = r.content
# print(content)

# status code 
print(r.status_code)
print(r.history)





