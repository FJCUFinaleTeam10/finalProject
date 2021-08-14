import csv
import json
import pandas as pd
import pymongo

client = pymongo.MongoClient("140.136.151.94",27017)
db = client ["RMDP"]
collection = db ["Generate_Driver"]
data = pd.read_csv('driver1.csv',encoding = 'ISO-8859-1')
#print(data['City'])
'''
data1=pd.DataFrame()
data = pd.read_csv('zomato.csv',encoding = 'ISO-8859-1')
data1['Restaurant_ID'] = data['Restaurant ID']
data1['Country_Code'] = data['Country Code']
data1['City'] = data['City']
data1['Locality'] = data['Locality']
data1['Longitude'] = data['Longitude']
data1['Latitude'] = data['Latitude']
data1['Cuisines'] = data['Cuisines']
data1['Average_Cost_for_two'] = data['Average Cost for two']
data1['Currency'] = data['Currency']
data1['Has_Table_booking'] = data['Has Table booking']
data1['Has_Online_delivery'] = data['Has Online delivery']
data1['Is_delivering_now'] = data['Is delivering now']
#data1['Switch_to_order_menu'] = data['Switch to order menu']
data1['Price_range'] = data['Price range']
data1['Aggregate_rating'] = data['Aggregate rating']
data1['Rating_color'] = data['Rating color']
data1['Rating_text'] = data['Rating text']
data1['Votes'] = data['Votes']
print(data1)
'''
data_json = json.loads(data.to_json(orient='records'))
collection.insert(data_json)
