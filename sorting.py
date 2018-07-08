#!/usr/bin/python3

from pymongo import MongoClient, DESCENDING

client = MongoClient('mongodb://localhost:27017/')

with client:
    db = client.testdb

    cars = db.cars.find().sort("price", DESCENDING)

    for car in cars:
        print('{0} {1}'.format(car['name'], 
            car['price']))