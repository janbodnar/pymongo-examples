#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    cars = db.cars.find()

    print(cars.next())
    print(cars.next())
    print(cars.next())
    
    cars.rewind()

    print(cars.next())
    print(cars.next())
    print(cars.next())    

    print(list(cars))
