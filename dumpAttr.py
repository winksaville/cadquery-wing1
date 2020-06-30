"""
Dump attributes of an object
  From: https://blender.stackexchange.com/questions/1879/is-it-possible-to-dump-an-objects-properties-and-methods
"""

def dumpAttr(obj):
    """
    Dump attributes of the object
    """
    for attr in dir(obj):
        if hasattr( obj, attr ):
            print(f'obj.{attr} = {getattr(obj, attr)}')

