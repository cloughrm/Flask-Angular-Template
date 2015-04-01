import bson
import json
import datetime
from pymongo.cursor import Cursor


class APIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return str(obj)
        elif isinstance(obj, bson.timestamp.Timestamp):
            return str(obj)
        elif isinstance(obj, bson.objectid.ObjectId):
            return str(obj)
        elif isinstance(obj, Cursor):
            return [x for x in obj]
        return json.JSONEncoder.default(self, obj)
