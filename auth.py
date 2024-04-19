import json
def userAuthenticator(id, password):
    f = open("database/user.json")
    data = json.load(f)
    users = data["User_list"]

    for user in users:
        if user['id'] == id and user['password'] == password:
            result=[True,user["type"]]
            return result
