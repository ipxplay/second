import json

with open("user.json",encoding="utf-8") as f:
    userinfo = json.load(f)
if userinfo:
    str = input(userinfo+"is your name?")
    if str=="yes":
        print("welcome"+userinfo+"login")
    else:
        username = input("your name:")
        with open("user.json",mode="w",encoding="utf-8") as f:
           json.dump(username,f) 
else:
    username = input("your name:")
    with open("user.json",mode="w",encoding="utf-8") as f:
        json.dump(username,f) 
    