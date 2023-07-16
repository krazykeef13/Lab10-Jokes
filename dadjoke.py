import requests

url = "https://icanhazdadjoke.com/"

payload = {}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
responsejson = response.json()

print("Your Dad joke is: " + str(responsejson['joke']))
