# encoding: utf-8
# module yajl
# from /usr/local/lib/python2.7/dist-packages/yajl.so
# by generator 1.138
"""
Providing a pythonic interface to the yajl (Yet Another JSON Library) parser

The interface is similar to that of simplejson or jsonlib providing a consistent syntax for JSON
encoding and decoding. Unlike simplejson or jsonlib, yajl is **fast** :)

The following benchmark was done on a dual core MacBook Pro with a fairly large (100K) JSON document:
json.loads():		21351.313ms
simplejson.loads():	1378.6492ms
yajl.loads():		502.4572ms

json.dumps():		7760.6348ms
simplejson.dumps():	930.9748ms
yajl.dumps():		681.0221ms
"""
# no imports

# functions

def dump(obj, fp, indent=None): # real signature unknown; restored from __doc__
    """
    yajl.dump(obj, fp [, indent=None])
    
    Encodes the given `obj` and writes it to the `fp` stream-like object. 
    *Note*: It is expected that `fp` supports the `write()` method
    
    If `indent` is a non-negative integer, then JSON array elements 
    and object members will be pretty-printed with that indent level. 
    An indent level of 0 will only insert newlines. None (the default) 
    selects the most compact representation.
    """
    pass

def dumps(obj, indent=None): # real signature unknown; restored from __doc__
    """
    yajl.dumps(obj [, indent=None])
    
    Returns an encoded JSON string of the specified `obj`
    
    If `indent` is a non-negative integer, then JSON array elements 
    and object members will be pretty-printed with that indent level. 
    An indent level of 0 will only insert newlines. None (the default) 
    selects the most compact representation.
    """
    pass

def load(fp): # real signature unknown; restored from __doc__
    """
    yajl.load(fp)
    
    Returns a decoded object based on the JSON read from the `fp` stream-like
    object; *Note:* It is expected that `fp` supports the `read()` method
    """
    pass

def loads(string): # real signature unknown; restored from __doc__
    """
    yajl.loads(string)
    
    Returns a decoded object based on the given JSON `string`
    """
    pass

# classes

class Decoder(object):
    """ Yajl-based decoder """
    def decode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Encoder(object):
    """ Yajl-based encoder """
    def encode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


