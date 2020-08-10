import pandas as pd
import json
from pymongo import MongoClient

path = "C:\\Users\\smit2\\Downloads\\Data\\UScomments.csv"
df = pd.read_csv( path, names = ['id','comment', 'likes','replies'], low_memory=True)
df.head()

df = df.iloc[1:]
df.head()

#from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected.")
except:
    print("Not connected.")

db = conn.database

comment_collection = db.comments
comments_youtube = df['comment']

comments_youtube.head()

#import json
records = json.loads(df.T.to_json()).values()
comment_collection.insert_many(records)


f = open("C:/Users/smit2/OneDrive/Desktop/Sub-word-LSTM-master/Data/data.txt", "a", encoding = 'UTF-8')

count = 0
for x in db.comments.find():
    print(x['comment'])
    f.write(x['comment'])
    f.write("\n")
    count = count + 1
    if(count > 10):
        break
f.close()
