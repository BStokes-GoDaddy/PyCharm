# encoding: utf-8
# module _blueman
# from /usr/lib/python2.7/dist-packages/_blueman.so
# by generator 1.138
# no doc

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import exceptions as exceptions # <module 'exceptions' (built-in)>

# Variables with simple values

RFCOMM_HANGUP_NOW = 2

RFCOMM_RELEASE_ONHUP = 1

RFCOMM_REUSE_DLC = 0

RFCOMM_TTY_ATTACHED = 3

# functions

def create_bridge(*args, **kwargs): # real signature unknown
    pass

def destroy_bridge(*args, **kwargs): # real signature unknown
    pass

def device_info(*args, **kwargs): # real signature unknown
    pass

def get_net_address(*args, **kwargs): # real signature unknown
    pass

def get_net_interfaces(*args, **kwargs): # real signature unknown
    pass

def get_net_netmask(*args, **kwargs): # real signature unknown
    pass

def get_special_dir(*args, **kwargs): # real signature unknown
    pass

def page_timeout(*args, **kwargs): # real signature unknown
    pass

def probe_modem(*args, **kwargs): # real signature unknown
    pass

def rfcomm_list(*args, **kwargs): # real signature unknown
    pass

def set_probe_debug(*args, **kwargs): # real signature unknown
    pass

# classes

class BridgeException(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class conn_info(object):
    # no doc
    def deinit(self, *args, **kwargs): # real signature unknown
        pass

    def get_lq(self, *args, **kwargs): # real signature unknown
        pass

    def get_rssi(self, *args, **kwargs): # real signature unknown
        pass

    def get_tpl(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class sn_launcher(object):
    # no doc
    def complete(self, *args, **kwargs): # real signature unknown
        pass

    def get_initiated(self, *args, **kwargs): # real signature unknown
        pass

    def get_initiated_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_last_active_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_startup_id(self, *args, **kwargs): # real signature unknown
        pass

    def initiate(self, *args, **kwargs): # real signature unknown
        pass

    def setup_child_process(self, *args, **kwargs): # real signature unknown
        pass

    def set_binary_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_description(self, *args, **kwargs): # real signature unknown
        pass

    def set_extra_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_wmclass(self, *args, **kwargs): # real signature unknown
        pass

    def set_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class SpecialDirType:
    # no doc
    DESKTOP = 0
    DOCUMENTS = 1
    DOWNLOAD = 2
    MUSIC = 3
    PICTURES = 4
    PUBLIC_SHARE = 5
    TEMPLATES = 6
    VIDEOS = 7


# variables with complex values

ERR = {
    -11: 'ERR_READ_PAGE_TIMEOUT',
    -10: 'ERR_CANT_READ_PAGE_TIMEOUT',
    -9: 'ERR_SOCKET_FAILED',
    -8: 'Getting rfcomm list failed',
    -7: 'Read Link quality failed',
    -6: 'Read transmit power level request failed',
    -5: 'Read RSSI failed',
    -4: 'Get connection info failed',
    -3: 'Not connected',
    -2: 'HCI device open failed',
    -1: "Can't allocate memory",
}

RFCOMM_STATES = [
    'unknown',
    'connected',
    'clean',
    'bound',
    'listening',
    'connecting',
    'connecting',
    'config',
    'disconnecting',
    'closed',
]

