""" Write a Python function that returns the list of school having a specific topic:
    Prototype: def schools_by_topic(mongo_collection, topic):
    mongo_collection will be the pymongo collection object
    topic (string) will be topic searched """


def schools_by_topic(mongo_collection, topic):
    """ filter schools by topic """
    db = mongo_collection.find({'topic': {'$in': list(topic)}})
    return db
