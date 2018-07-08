#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    agr = [ {'$group': {'_id': 1, 'all': { '$sum': '$price' } } } ]

    val = list(db.cars.aggregate(agr))

    print('The sum of prices is {}'.format(val[0]['all']))

#client.close()