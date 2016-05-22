# encoding: utf-8
# module coverage.tracer
# from /home/bill/Projects/DigiSanc/DigiSanc_RAP/env27/local/lib/python2.7/site-packages/coverage/tracer.so
# by generator 1.138
""" Fast coverage tracer. """
# no imports

# no functions
# classes

class CFileDisposition(object):
    """ CFileDisposition objects """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    canonical_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_tracer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_dynamic_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CTracer(object):
    """ CTracer objects """
    def get_stats(self, *args, **kwargs): # real signature unknown
        """ Get statistics about the tracing """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """ Start the tracer """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        """ Stop the tracer """
        pass

    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    check_include = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function indicating whether to include a file."""

    concur_id_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for determining concurrency context"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw dictionary of trace data."""

    file_tracers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Mapping from file name to plugin name."""

    should_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function indicating whether to trace a file."""

    should_trace_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary caching should_trace results."""

    trace_arcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should we trace arcs, or just lines?"""

    warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for issuing warnings."""



