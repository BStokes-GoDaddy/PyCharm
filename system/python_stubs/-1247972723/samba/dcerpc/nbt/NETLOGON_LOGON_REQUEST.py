# encoding: utf-8
# module samba.dcerpc.nbt
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/nbt.so
# by generator 1.138
""" nbt DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class NETLOGON_LOGON_REQUEST(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    computer_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lm20_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lmnt_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mailslot_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    request_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    user_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



