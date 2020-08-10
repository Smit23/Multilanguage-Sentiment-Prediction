import pandas as pd
import json
from pymongo import MongoClient

path = "C:\\Users\\smit2\\Downloads\\Data\\UScomments.csv"
df = pd.read_csv( path, names = ['id','comment', 'likes','replies'])
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


result = db.comments.find_one()
print(result['comment'])
