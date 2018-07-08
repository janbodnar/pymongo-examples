#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    car = db.cars.find_one({'name': 'Volvo'})
    print(car)
