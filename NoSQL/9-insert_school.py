#!/usr/bin/env python3
"Python function that inserts a new document in a collection based on kwargs"
import pymongo


def insert_school(mongo_collection, **kwargs) -> str:
    """Insert a new document in a collection based on kwargs"""

    new_document = mongo_collection.insert_one(kwargs)

    return new_document.inserted_id
