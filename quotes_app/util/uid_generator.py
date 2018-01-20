# This generator can be replaced by lib uuid of python
# https://docs.python.org/3.5/library/uuid.html
# or use lib hash https://docs.python.org/3/library/hashlib.html
import random
import time


def uid_generator():
    """Returns a 40-character uid

    Uid generator for a session and return it.
    """
    timestamp = "%08x" % time.time()
    uid_session = '%s%s' % (timestamp, "%016x" % random.getrandbits(128))
    return uid_session
