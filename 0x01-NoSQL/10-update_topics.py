#!/usr/bin/env python3
'''update a document'''


def update_topics(mongo_collection, name, topics):
    '''function to update a document'''
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
    )
