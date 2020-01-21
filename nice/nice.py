"""Main module."""

def parents(klass):
    parent_classes = klass.mro()
    parent_classes.remove(klass)

    return parent_classes
