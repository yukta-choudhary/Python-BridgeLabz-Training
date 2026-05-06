import json

data= {
"name":"Alex",
"role":"Engineer"
}

with open("user.json","w") as file:
    json.dump(data,file)