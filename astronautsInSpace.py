import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print(type(response))
print(response.__dict__)
print(dir(response))
print(response.content(title))
json = response.json()
print("Space contains these known individuals:")
for person in json["people"]:
    print(person["name"])