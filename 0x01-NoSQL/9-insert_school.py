#!/usr/bin/env python3
'''insert data into mongodb'''


def insert_school(mongo_collection, **kwargs):
    '''function that inserts item in mongo collection'''
    return mongo_collection.insert_one(kwargs).inserted_id
