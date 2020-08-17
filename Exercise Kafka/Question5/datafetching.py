import requests , json


r = requests.get("https://reqres.in/api/users?page=2")

data = r.json()

#print(data.items())

f = open("demofile5.json", "a")
for item in data.items():
    if (item[0]=='data'):
        actual = item[1]
        for j in actual:
            f.write(json.dumps(j)+"\n")
f.close()