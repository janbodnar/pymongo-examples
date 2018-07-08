#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.testdb

    n_cars = db.cars.find().count()

    print("There are {} cars".format(n_cars))