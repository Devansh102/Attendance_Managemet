class localUser:
   
    def __init__(self,id,password,user):
        self.id  = id
        self.password= password
        self.user=user

    def printUsr(self):
        print(self.id)
        print(self.password)
        print(self.user)

    def getId(self):
        return self.id
    
    def getUser(self):
        print(self.user)
        return self.user