
import pymongo
import pandas as pd
client = pymongo.MongoClient('localhost',27017)
db = client['mongo']
collection = db['weatherHistory']
with open('weatherHistory.csv')as finput:
    for line in finput:
        row_list =line.rstrip('\n').split(',')
        row_dict = dict(zip(column_names_list,row_list))
        try:
            row_dict['age']= int(row_dict['age'])
            collection.insert_one(row_dict)
        except:
            pass
