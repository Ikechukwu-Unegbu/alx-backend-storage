#!/usr/bin/env python3
"""
Task 11 file
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find school by given topic or value
    """
    return mongo_collection.find({"topics":  {"$in": [topic]}})
