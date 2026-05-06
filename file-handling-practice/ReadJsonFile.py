import json

with open("user.json","r") as file:
	data=json.load(file)
	print(data)