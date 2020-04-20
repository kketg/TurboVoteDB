import json
class db:
    
    def __init__(self):
        self.jFile = open("db.json").read()
        self.dataList = json.loads(self.jFile)
    def fromJSON(self, j):
        return json.loads(j)
    def updateFromFile(self):
        self.jFile = open("db.json").read()
        self.dataList = json.loads(self.jFile)
        for i in self.dataList:
            print(i)
    def toJSON(self):
        self.updateFromFile()
        return json.loads(self.jFile)
    def updateToFile(self):
        for i in self.dataList:
            print(i)
        f = open("db.json", "w")
        f.write(json.dumps(self.dataList))
        f.close()
    def addToDb(self, newDict):
        self.dataList.append(newDict)
        self.updateToFile()
    def searchDb(self, id):
        self.updateFromFile()
        for i in self.dataList:
            if i["id"] == id:
                return i
    def changeCurrentTime(self,id,time):
        loc = self.searchDb(int(id))
        print(loc)
        loc["currentWaitTime"] = int(time)
        self.updateToFile()
        return loc