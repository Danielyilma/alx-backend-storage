#!/usr/bin/env python3
'''search by topic'''


def schools_by_topic(mongo_collection, topic):
    '''search for a school by the topic'''
    schools = (mongo_collection.find({"topics": {"$in": [topic]}}))
    result = []

    for school in schools:
        result.append(school)
    return result
