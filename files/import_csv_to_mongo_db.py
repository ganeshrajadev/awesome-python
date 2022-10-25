import csv
from turtle import title
import pymongo
import os
from dotenv import load_dotenv

load_dotenv() # Loading ENV file data

FILE_NAME= os.environ['FILE_NAME']  # file name of the csv to be loaded
MONGO_CONNECTION_STRING = os.environ['MONGO_CONNECTION_STRING']
DATABASE_NAME=os.environ['DATABASE_NAME']
COLLECTION_NAME=os.environ['COLLECTION_NAME'] 

data=[]

with open(FILE_NAME, mode ='r')as file:
  csvFile = csv.reader(file)
  index=0
  for lines in csvFile:
      if index==0:
        title=lines
      else:
        title_index=0
        temp={}
        for item in lines:
          print(item,index)
          temp[title[title_index]]=item
          title_index+=1
        data.append(temp)
      index+=1
myclient = pymongo.MongoClient(MONGO_CONNECTION_STRING)

mydb = myclient[DATABASE_NAME]

mycol = mydb[COLLECTION_NAME]

response = mycol.insert_many(data)

print(response.inserted_ids)
