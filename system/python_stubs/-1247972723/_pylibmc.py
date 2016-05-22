# encoding: utf-8
# module _pylibmc
# from /usr/local/lib/python2.7/dist-packages/_pylibmc.so
# by generator 1.138
"""
Hand-made wrapper for libmemcached.

You should really use the Python wrapper around this library.

    c = _pylibmc.client([(_pylibmc.server_type_tcp, 'localhost', 11211)])

Three-tuples of (type, host, port) are used. If type is `server_type_unix`,
no port should be given. libmemcached can parse strings as well::

   c = _pylibmc.client('localhost')

See libmemcached's memcached_servers_parse for more info on that. I'm told 
you can use UNIX domain sockets by specifying paths, and multiple servers 
by using comma-separation. Good luck with that.
"""
# no imports

# Variables with simple values

distribution_consistent = 1

distribution_consistent_ketama = 2

distribution_modula = 0

hash_crc = 2
hash_default = 0

hash_fnv1a_32 = 6
hash_fnv1a_64 = 4

hash_fnv1_32 = 5
hash_fnv1_64 = 3

hash_md5 = 1
hash_murmur = 8

libmemcached_version = '1.0.8'

server_type_tcp = 1
server_type_udp = 2
server_type_unix = 4

support_compression = True
support_sasl = False

__version__ = '1.2.3'

# no functions
# classes

class MemcachedError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class AllocationError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 17


class BadKeyProvided(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 33


class client(object):
    """ memcached client type """
    def add(self, *args, **kwargs): # real signature unknown
        """ Set a key only if doesn't exist. """
        pass

    def add_multi(self, *args, **kwargs): # real signature unknown
        """ Add multiple keys at once. """
        pass

    def append(self, *args, **kwargs): # real signature unknown
        """ Append data to a key. """
        pass

    def cas(self, *args, **kwargs): # real signature unknown
        """ Attempt to compare-and-store a key by CAS ID. """
        pass

    def clone(self, *args, **kwargs): # real signature unknown
        """ Clone this client entirely such that it is safe to access from another thread. This creates a new connection. """
        pass

    def decr(self, *args, **kwargs): # real signature unknown
        """ Decrement a key by a delta. """
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        """ Delete a key. """
        pass

    def delete_multi(self, *args, **kwargs): # real signature unknown
        """ Delete multiple keys at once. """
        pass

    def disconnect_all(self, *args, **kwargs): # real signature unknown
        """ Disconnect from all servers and reset own state. """
        pass

    def flush_all(self, *args, **kwargs): # real signature unknown
        """ Flush all data on all servers. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Retrieve a key from a memcached. """
        pass

    def gets(self, *args, **kwargs): # real signature unknown
        """ Retrieve a key and cas_id from a memcached. """
        pass

    def get_behaviors(self, *args, **kwargs): # real signature unknown
        """ Get behaviors dict. """
        pass

    def get_multi(self, *args, **kwargs): # real signature unknown
        """ Get multiple keys at once. """
        pass

    def get_stats(self, *args, **kwargs): # real signature unknown
        """ Retrieve statistics from all memcached servers. """
        pass

    def incr(self, *args, **kwargs): # real signature unknown
        """ Increment a key by a delta. """
        pass

    def incr_multi(self, *args, **kwargs): # real signature unknown
        """ Increment more than one key by a delta. """
        pass

    def prepend(self, *args, **kwargs): # real signature unknown
        """ Prepend data to  a key. """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Set a key only if it exists. """
        pass

    def set(self, *args, **kwargs): # real signature unknown
        """ Set a key unconditionally. """
        pass

    def set_behaviors(self, *args, **kwargs): # real signature unknown
        """ Set behaviors dict. """
        pass

    def set_multi(self, *args, **kwargs): # real signature unknown
        """ Set multiple keys at once. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ClientError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 9


class ConnectionBindError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 4


class ConnectionError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 3


class DataDoesNotExist(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 13


class DataExists(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 12


class Failure(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 1


class FetchNotFinished(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 30


class HostLookupError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 2


class InvalidHostProtocolError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 34


class NoServers(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 20


class NotFound(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 16


class NotSupportedError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 28


class ProtocolError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 8


class ReadError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 6


class ServerDead(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 35


class ServerError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 10


class SocketCreateError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 11


class SomeErrors(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 19


class UnixSocketError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 27


class UnknownReadFailure(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 7


class UnknownStatKey(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 36


class WriteError(MemcachedError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    retcode = 5


# variables with complex values

all_behaviors = [
    'no_block',
    'tcp_nodelay',
    'hash',
    'ketama_hash',
    'ketama',
    'ketama_weighted',
    'distribution',
    'cas',
    'buffer_requests',
    'verify_keys',
    'connect_timeout',
    'send_timeout',
    'receive_timeout',
    'num_replicas',
    'auto_eject',
    'retry_timeout',
    'remove_failed',
    'failure_limit',
    '_io_msg_watermark',
    '_io_bytes_watermark',
    '_io_key_prefetch',
    '_hash_with_prefix_key',
    '_noreply',
    '_sort_hosts',
    '_poll_timeout',
    '_socket_send_size',
    '_socket_recv_size',
]

exceptions = [
    (
        'Error',
        MemcachedError,
    ),
    (
        'Failure',
        Failure,
    ),
    (
        'HostLookupError',
        HostLookupError,
    ),
    (
        'ConnectionError',
        ConnectionError,
    ),
    (
        'ConnectionBindError',
        ConnectionBindError,
    ),
    (
        'WriteError',
        WriteError,
    ),
    (
        'ReadError',
        ReadError,
    ),
    (
        'UnknownReadFailure',
        UnknownReadFailure,
    ),
    (
        'ProtocolError',
        ProtocolError,
    ),
    (
        'ClientError',
        ClientError,
    ),
    (
        'ServerError',
        ServerError,
    ),
    (
        'SocketCreateError',
        SocketCreateError,
    ),
    (
        'DataExists',
        DataExists,
    ),
    (
        'DataDoesNotExist',
        DataDoesNotExist,
    ),
    (
        'NotFound',
        NotFound,
    ),
    (
        'AllocationError',
        AllocationError,
    ),
    (
        'SomeErrors',
        SomeErrors,
    ),
    (
        'NoServers',
        NoServers,
    ),
    (
        'UnixSocketError',
        UnixSocketError,
    ),
    (
        'NotSupportedError',
        NotSupportedError,
    ),
    (
        'FetchNotFinished',
        FetchNotFinished,
    ),
    (
        'BadKeyProvided',
        BadKeyProvided,
    ),
    (
        'InvalidHostProtocolError',
        InvalidHostProtocolError,
    ),
    (
        'ServerDead',
        ServerDead,
    ),
    (
        'UnknownStatKey',
        UnknownStatKey,
    ),
]

