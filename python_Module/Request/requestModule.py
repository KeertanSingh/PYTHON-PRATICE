# Importing request module 
import requests   

# sending get request
x=requests.get("https://google.com/")

with open("request.html", 'w') as file:
    file.write(x.text); 