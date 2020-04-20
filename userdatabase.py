import json
class userdb:
    
    def __init__(self):
        self.jFile = open("users.json").read()
        self.dataList = json.loads(self.jFile)
    def fromJSON(self, j):
        return json.loads(j)
    def updateFromFile(self):
        self.jFile = open("users.json").read()
        self.dataList = json.loads(self.jFile)
        for i in self.dataList:
            print(i)
    def toJSON(self):
        self.updateFromFile()
        return json.loads(self.jFile)
    def updateToFile(self):
        for i in self.dataList:
            print(i)
        f = open("users.json", "w")
        f.write(json.dumps(self.dataList))
        f.close()
    def addToDb(self, newDict):
        self.dataList.append(newDict)
        self.updateToFile()
    def searchDb(self, id):
        self.updateFromFile()
        for i in self.dataList:
            if i.id == id:
                return i
    
        
    