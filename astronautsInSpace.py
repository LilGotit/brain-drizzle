import requests
response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
print("Space contains these known individuals:")
for person in json["people"]:
    print(person["name"], person["craft"])