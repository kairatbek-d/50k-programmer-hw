import requests

response = requests.get("https://www.python.org")

f = open('python.html', mode='w')
f.write(response.text)
f.close()