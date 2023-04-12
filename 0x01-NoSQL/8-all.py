#!/usr/bin/env python3
"""
Python function to list all docs
"""
import pymongo


def list_all(mongo_collection):
    """
    simple function to list all doc in a collection
    """
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [item for item in docs]
