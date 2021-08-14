import csv
import json
import pandas as pd
from pymongo import MongoClient

client = client = MongoClient('mongodb://test:test@140.136.151.94:27017/RMDP')
db = client["RMDP"]
testDriverCollection = db["test_driver"]
zomatoCollection = db["test_restaurant"]
driverData = pd.read_csv('driver1.csv', encoding='ISO-8859-1')
restaurantData = pd.read_csv('zomato.csv', encoding='ISO-8859-1')
# print(data['City'])

driverData = json.loads(driverData.to_json(orient='records'))
restaurantJson = json.loads(restaurantData.to_json(orient='records'))
zomatoCollection.insert_many(restaurantJson)
