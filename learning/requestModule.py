# Python requests is a python library used to get requests from the web page.
import requests
url = "https://httpbin.com"

# get requests
# GET request is used to request the data from the server.
r = requests.get(url)

# print(r.text)  # source code
# print(r.url)

# post request
payload = {"key1":"value"}
r1 = requests.post(f"{url}/post", data=payload)

print(r1.text)