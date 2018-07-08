#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    cars = db.cars.find({}, {'_id': 1, 'name':1})

    for car in cars:
        print(car)
