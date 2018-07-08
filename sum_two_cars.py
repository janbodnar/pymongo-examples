#!/usr/bin/python3

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:
    
    db = client.testdb

    agr = [{ '$match': {'$or': [ { 'name': "Audi" }, { 'name': "Volvo" }] }}, 
        { '$group': {'_id': 1, 'sum2cars': { '$sum': "$price" } }}]; 

    val = list(db.cars.aggregate(agr))

    print('The sum of prices of two cars is {}'.format(val[0]['sum2cars']))

#client.close()