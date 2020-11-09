from pymongo import MongoClient


client = MongoClient()
db = client.waimaoba_db
coll = db.company_information

data = coll.find()
for d in data:
    print(d['ContactPerson'], d['Email'])
