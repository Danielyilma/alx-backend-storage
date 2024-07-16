#!/usr/bin/env python3

def list_all(mongo_collection):
    result = []

    for collection in mongo_collection.find():
        result.append(collection)

    return result
