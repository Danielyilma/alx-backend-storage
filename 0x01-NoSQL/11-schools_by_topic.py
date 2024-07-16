#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic):
    schools = (mongo_collection.find({"topics": {"$in": [topic]}}))
    result = []

    for school in schools:
        result.append(school)
    return result