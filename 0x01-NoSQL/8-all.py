#!/usr/bin/env python3
'''list all document in a collection'''

def list_all(mongo_collection):
    '''function that return list of documents'''
    result = []

    for collection in mongo_collection.find():
        result.append(collection)

    return result
