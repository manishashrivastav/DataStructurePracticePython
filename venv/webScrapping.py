import requests
from bs4 import BeautifulSoup
import  hashlib
class HashTable:
    def __init__(self, capacity=15):
        self.capacity = capacity
        self.size = 0
        self.buckets = []

        for i in range(0, capacity):
            self.buckets.append(None)

    def hashFunction(self, key):
        hashCode = int(hashlib.sha512(key.encode("utf-8")).hexdigest(), 16) % 8
        return hashCode

    def put(self, team):
        key = team.teamName
        index = self.hashFunction(key)

        added = False
        if self.buckets[index] ==None:
            self.buckets[index] = team
            print(">> team Added at index:", index, "Details:", team)

        else:
            while added !=True:
                if index <len(self.buckets)-1:
                    index +=1
                else:
                    index=0
                if self.buckets[index] == None:
                    self.buckets[index] = team
                    print(">> Team Added at index:", index, "Details:", team)
                    added =True
        self.size += 1


class Team:

    def __init__(self , teamName , total , won ,lost , tied , abondoned ,
                 points , netRunRate, scoreFor , scoreAgainst):

        self.teamName = teamName
        self.total = total
        self.won = won
        self.lost = lost
        self.tied = tied
        self.abondoned = abondoned
        self.points = points
        self.netRunRate = netRunRate
        self.scoreFor = scoreFor
        self.scoreAgainst = scoreAgainst

    def __str__(self):

        return "{},{},{},{},{},{},{},{},{},{}".\
            format(self.teamName, self.total , self.won, self.lost,
                  self.tied , self.abondoned , self.points,
                  self.netRunRate , self.scoreFor, self.scoreAgainst)

url = "https://www.espncricinfo.com/table/series/8048/season/2019/ipl"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

spantags = soup.find_all("span" , class_="team-names")
tdtags = soup.find_all("td" , class_="")
listofData=[]
for tag2 in tdtags:
    listofData.append(tag2.text)

i=0
objectList=[]
for tag in spantags:
    s= Team(tag.text , listofData[i] ,listofData[i+1] , listofData[i+2],
            listofData[i+3],listofData[i+4],listofData[i+5],listofData[i+6],
            listofData[i+7], listofData[i+8])

    objectList.append(s)
    print(s)
    print()
    i +=9

print(objectList)

for obj in objectList:
    hRef = HashTable()
    hRef.put(obj)

















