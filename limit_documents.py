#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    cars = db.cars.find().skip(2).limit(3)

    for car in cars:
        print('{0}: {1}'.format(car['name'], car['price']))
