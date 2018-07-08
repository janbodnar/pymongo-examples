#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    expensive_cars = db.cars.find({'price': {'$gt': 50000}})

    for ecar in expensive_cars:
        print(ecar['name'])
