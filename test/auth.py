import json
def userAuthenticator(id, password):

    print("Checking " , id , password)
    f = open("../database/user.json")
    data = json.load(f)
    users = data["User_list"]

    for user in users:
        if user['id'] == id and user['password'] == password:
            print("Hello", user["id"])
            result=[True,user["type"]]
            return result
        
    print("Not verified")
