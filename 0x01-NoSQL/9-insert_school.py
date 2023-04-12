#!/usr/bin/env python3
"""
Doc insertion using python
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    inserting documents into collection
    """
    info = mongo_collection.insert_one(kwargs)
    return info.inserted_id
