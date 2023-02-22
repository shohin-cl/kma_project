import json

userID = input("Enter your ID: ")

with open("sample.json") as file:
    data = json.load(file)
    for i in data:
        if data[i]["ID number"] == userID:
            print(json.dumps(data[i], indent=4, ensure_ascii=False))

