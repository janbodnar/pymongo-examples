#!/usr/bin/python3

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb
    print(db.collection_names())

    status = db.command("dbstats")
    pprint(status)