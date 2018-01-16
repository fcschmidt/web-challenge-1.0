import datetime


def default(obj):
    """Convert Datetime Python objects to string JSON"""
    if type(obj) is datetime.date or type(obj) is datetime.datetime:
        return obj.isoformat()
    if type(obj) is datetime.time or type(obj) is datetime.datetime.time:
        return obj.isoformat()
