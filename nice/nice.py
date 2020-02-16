"""Main module."""
from contextlib import contextmanager
from datetime import date
import datetime


def parents(klass):
    parent_classes = klass.mro()
    parent_classes.remove(klass)

    return parent_classes


@contextmanager
def simple_timer():
    """
   Usage: time a function execution in seconds
   example:
   with simple_timer():
       some_function()
   """
    print ("Starting...\n")
    start = datetime.datetime.now()

    try:
        yield
    finally:
        finish = datetime.datetime.now()
        seconds = (finish - start).total_seconds()
        print ("\nFinished, took {} seconds".format(seconds))


def readable_datetime(timestamp):
    print date.fromtimestamp(timestamp).strftime("%B %d %Y, %I:%M:%S %p")
