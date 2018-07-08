#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    cars = db.cars.find().where('this.price<15000')
    print(db.cars.find().where.__doc__)

    print(list(cars))
