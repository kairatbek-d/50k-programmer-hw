import requests

getLink = input()

response = requests.get(getLink)

print(response.status_code)

text = response.text.split()
amount = 0
for partText in text:
    if "<img" in partText:
        amount+=1

print(amount)