import requests

r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)


a = 1

#defining a sample function
b = 2
print(a+b)