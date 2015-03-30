import json
import datetime
from bson.objectid import ObjectId
from pymongo.cursor import Cursor


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        elif isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, Cursor):
            return [x for x in obj]
        return json.JSONEncoder.default(self, obj)
