# encoding: utf-8
# module samba.dcerpc.lsa
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/lsa.so
# by generator 1.138
""" lsa DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class AuditLogInfo(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    maximum_log_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next_audit_record = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    percent_full = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    retention_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shutdown_in_progress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time_to_shutdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



