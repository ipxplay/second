import json


# with open("user.json",encoding="utf-8") as f:
#     userinfo = json.load(f)
# if userinfo:
#     str = input(userinfo+"is your name?")
#     if str=="yes":
#         print("welcome"+userinfo+"login")
#     else:
#         username = input("your name:")
#         with open("user.json",mode="w",encoding="utf-8") as f:
#            json.dump(username,f) 
# else:
#     username = input("your name:")
#     with open("user.json",mode="w",encoding="utf-8") as f:
#         json.dump(username,f) 

filename = "user.json"
def saveData(username,filename=filename):   
     with open("user.json",mode="w",encoding="utf-8") as f:
        json.dump(username,f) 
def getData(filename=filename):    
    try:
        with open("user.json",encoding="utf-8") as f:
            userinfo = json.load(f)
    except:
         return None
    return userinfo
def greet_newuser():
    username = input("your name:")
    saveData(username)
def greet_olduser(userinfo):
    print("welcome"+userinfo+"login")

def greet_user():
    userinfo = getData()
    if userinfo:
        str = input(userinfo+"is your name?")
        if str=="yes":
            greet_olduser(userinfo)
        else:
            greet_newuser() 
    else:
        greet_newuser()

if __name__=="__main__":
    greet_user()
    
    
    