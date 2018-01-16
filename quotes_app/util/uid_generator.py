import random
import time


def uid_generator():
    """Uid generator for a session and return it."""
    timestamp = "%08x" % time.time()
    uid_session = '%s%s' % (timestamp, "%016x" % random.getrandbits(128))
    return uid_session
