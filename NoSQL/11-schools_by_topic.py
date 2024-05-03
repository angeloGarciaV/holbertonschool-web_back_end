#!/usr/bin/env python3
"""Function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic: str):
    """Function that returns the list of school having a specific topic"""
    query: dict = {"topics": topic}
    schools: list = []

    for school in mongo_collection.find(query):
        schools.append(school)

    return schools
