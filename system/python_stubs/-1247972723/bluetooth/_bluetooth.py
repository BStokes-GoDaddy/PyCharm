# encoding: utf-8
# module bluetooth._bluetooth
# from /usr/lib/python2.7/dist-packages/bluetooth/_bluetooth.so
# by generator 1.138
"""
Implementation module for bluetooth operations.

See the bluetooth module for documentation.
"""

# imports
import _bluetooth as ___bluetooth


# Variables with simple values

ACL_LINK = 1

EVT_AUTH_COMPLETE = 6

EVT_AUTH_COMPLETE_SIZE = 3

EVT_CMD_COMPLETE = 14

EVT_CMD_COMPLETE_SIZE = 3

EVT_CMD_STATUS = 15

EVT_CMD_STATUS_SIZE = 4

EVT_CONN_COMPLETE = 3

EVT_CONN_COMPLETE_SIZE = 13

EVT_CONN_PTYPE_CHANGED = 29

EVT_CONN_PTYPE_CHANGED_SIZE = 5

EVT_CONN_REQUEST = 4

EVT_CONN_REQUEST_SIZE = 10

EVT_DISCONN_COMPLETE = 5

EVT_DISCONN_COMPLETE_SIZE = 4

EVT_ENCRYPT_CHANGE = 8

EVT_ENCRYPT_CHANGE_SIZE = 5

EVT_INQUIRY_COMPLETE = 1
EVT_INQUIRY_RESULT = 2

EVT_INQUIRY_RESULT_WITH_RSSI = 34

EVT_LINK_KEY_NOTIFY = 24

EVT_LINK_KEY_NOTIFY_SIZE = 23

EVT_LINK_KEY_REQ = 23

EVT_LINK_KEY_REQ_SIZE = 6

EVT_MODE_CHANGE = 20

EVT_MODE_CHANGE_SIZE = 6

EVT_NUM_COMP_PKTS = 19

EVT_NUM_COMP_PKTS_SIZE = 1

EVT_PIN_CODE_REQ = 22

EVT_PIN_CODE_REQ_SIZE = 6

EVT_QOS_SETUP_COMPLETE = 13

EVT_QOS_SETUP_COMPLETE_SIZE = 21

EVT_QOS_VIOLATION = 30

EVT_QOS_VIOLATION_SIZE = 2

EVT_READ_CLOCK_OFFSET_COMPLETE = 28

EVT_READ_CLOCK_OFFSET_COMPLETE_SIZE = 5

EVT_READ_REMOTE_FEATURES_COMPLETE = 11

EVT_READ_REMOTE_FEATURES_COMPLETE_SIZE = 11

EVT_READ_REMOTE_VERSION_COMPLETE = 12

EVT_READ_REMOTE_VERSION_COMPLETE_SIZE = 8

EVT_REMOTE_NAME_REQ_COMPLETE = 7

EVT_REMOTE_NAME_REQ_COMPLETE_SIZE = 255

EVT_ROLE_CHANGE = 18

EVT_ROLE_CHANGE_SIZE = 8

EVT_SI_DEVICE = 1

EVT_SI_DEVICE_SIZE = 4

EVT_STACK_INTERNAL = 253

EVT_STACK_INTERNAL_SIZE = 2

EVT_TESTING = 254
EVT_VENDOR = 255

HCI = 1
HCIDEVDOWN = 1074022602
HCIDEVRESET = 1074022603
HCIDEVRESTAT = 1074022604
HCIDEVUP = 1074022601
HCIGETCONNINFO = 2147764437
HCIGETCONNLIST = 2147764436
HCIGETDEVINFO = 2147764435
HCIGETDEVLIST = 2147764434
HCIINQUIRY = 2147764464
HCISETACLMTU = 1074022627
HCISETAUTH = 1074022622
HCISETENCRYPT = 1074022623
HCISETLINKMODE = 1074022626
HCISETLINKPOL = 1074022625
HCISETPTYPE = 1074022624
HCISETRAW = 1074022620
HCISETSCAN = 1074022621
HCISETSCOMTU = 1074022628

HCI_ACLDATA_PKT = 2

HCI_COMMAND_PKT = 1

HCI_DATA_DIR = 1

HCI_EVENT_HDR_SIZE = 2

HCI_EVENT_PKT = 4

HCI_FILTER = 2

HCI_MAX_EVENT_SIZE = 260

HCI_SCODATA_PKT = 3

HCI_TIME_STAMP = 3

L2CAP = 0

L2CAP_COMMAND_REJ = 1

L2CAP_CONF_REQ = 4
L2CAP_CONF_RSP = 5

L2CAP_CONN_REQ = 2
L2CAP_CONN_RSP = 3

L2CAP_DISCONN_REQ = 6
L2CAP_DISCONN_RSP = 7

L2CAP_ECHO_REQ = 8
L2CAP_ECHO_RSP = 9

L2CAP_INFO_REQ = 10
L2CAP_INFO_RSP = 11

L2CAP_LM = 3

L2CAP_LM_AUTH = 2
L2CAP_LM_ENCRYPT = 4
L2CAP_LM_MASTER = 1
L2CAP_LM_RELIABLE = 16
L2CAP_LM_SECURE = 32
L2CAP_LM_TRUSTED = 8

L2CAP_OPTIONS = 1

MSG_CTRUNC = 8
MSG_DONTROUTE = 4
MSG_DONTWAIT = 64
MSG_EOR = 128
MSG_OOB = 1
MSG_PEEK = 2
MSG_TRUNC = 32
MSG_WAITALL = 256

OCF_ACCEPT_CONN_REQ = 9

OCF_ADD_SCO = 7

OCF_AUTH_REQUESTED = 17

OCF_CHANGE_LOCAL_NAME = 19

OCF_CREATE_CONN = 5

OCF_DISCONNECT = 6

OCF_EXIT_PARK_MODE = 6

OCF_EXIT_PERIODIC_INQUIRY = 4

OCF_EXIT_SNIFF_MODE = 4

OCF_HOLD_MODE = 1

OCF_HOST_BUFFER_SIZE = 51

OCF_INQUIRY = 1

OCF_INQUIRY_CANCEL = 2

OCF_LINK_KEY_NEG_REPLY = 12

OCF_LINK_KEY_REPLY = 11

OCF_PARK_MODE = 5

OCF_PERIODIC_INQUIRY = 3

OCF_PIN_CODE_NEG_REPLY = 14

OCF_PIN_CODE_REPLY = 13

OCF_QOS_SETUP = 7

OCF_READ_AFH_MAP = 6
OCF_READ_AFH_MODE = 72

OCF_READ_AUTH_ENABLE = 31

OCF_READ_BD_ADDR = 9

OCF_READ_BUFFER_SIZE = 5

OCF_READ_CLASS_OF_DEV = 35

OCF_READ_CLOCK_OFFSET = 31

OCF_READ_CURRENT_IAC_LAP = 57

OCF_READ_ENCRYPT_MODE = 33

OCF_READ_FAILED_CONTACT_COUNTER = 1

OCF_READ_INQUIRY_MODE = 68

OCF_READ_INQ_ACTIVITY = 29

OCF_READ_LINK_POLICY = 12

OCF_READ_LINK_SUPERVISION_TIMEOUT = 54

OCF_READ_LOCAL_FEATURES = 3
OCF_READ_LOCAL_NAME = 20
OCF_READ_LOCAL_VERSION = 1

OCF_READ_PAGE_ACTIVITY = 27
OCF_READ_PAGE_TIMEOUT = 23

OCF_READ_REMOTE_FEATURES = 27
OCF_READ_REMOTE_VERSION = 29

OCF_READ_RSSI = 5

OCF_READ_TRANSMIT_POWER_LEVEL = 45

OCF_READ_VOICE_SETTING = 37

OCF_REJECT_CONN_REQ = 10

OCF_REMOTE_NAME_REQ = 25

OCF_RESET = 3

OCF_RESET_FAILED_CONTACT_COUNTER = 2

OCF_ROLE_DISCOVERY = 9

OCF_SET_CONN_ENCRYPT = 19
OCF_SET_CONN_PTYPE = 15

OCF_SET_EVENT_FLT = 5

OCF_SNIFF_MODE = 3

OCF_SWITCH_ROLE = 11

OCF_WRITE_AFH_MODE = 73

OCF_WRITE_AUTH_ENABLE = 32

OCF_WRITE_CLASS_OF_DEV = 36

OCF_WRITE_CURRENT_IAC_LAP = 58

OCF_WRITE_ENCRYPT_MODE = 34

OCF_WRITE_INQUIRY_MODE = 69

OCF_WRITE_INQ_ACTIVITY = 30

OCF_WRITE_LINK_POLICY = 13

OCF_WRITE_LINK_SUPERVISION_TIMEOUT = 55

OCF_WRITE_PAGE_ACTIVITY = 28
OCF_WRITE_PAGE_TIMEOUT = 24

OCF_WRITE_SCAN_ENABLE = 26

OCF_WRITE_VOICE_SETTING = 38

OGF_HOST_CTL = 3

OGF_INFO_PARAM = 4

OGF_LINK_CTL = 1
OGF_LINK_POLICY = 2

OGF_STATUS_PARAM = 5

OGF_TESTING_CMD = 62

OGF_VENDOR_CMD = 63

RFCOMM = 3

RFCOMM_LM = 3

RFCOMM_LM_AUTH = 2
RFCOMM_LM_ENCRYPT = 4
RFCOMM_LM_MASTER = 1
RFCOMM_LM_RELIABLE = 16
RFCOMM_LM_SECURE = 32
RFCOMM_LM_TRUSTED = 8

SCO = 2

SCO_LINK = 0
SCO_OPTIONS = 1

SOL_HCI = 0
SOL_L2CAP = 6
SOL_RFCOMM = 18
SOL_SCO = 17
SOL_SOCKET = 1

SOMAXCONN = 128
SO_ACCEPTCONN = 30
SO_BROADCAST = 6
SO_DEBUG = 1
SO_DONTROUTE = 5
SO_ERROR = 4
SO_KEEPALIVE = 9
SO_LINGER = 13
SO_OOBINLINE = 10
SO_RCVBUF = 8
SO_RCVLOWAT = 18
SO_RCVTIMEO = 20
SO_REUSEADDR = 2
SO_SNDBUF = 7
SO_SNDLOWAT = 19
SO_SNDTIMEO = 21
SO_TYPE = 3

# functions

def ba2str(data): # real signature unknown; restored from __doc__
    """
    ba2str(data)
    
    Converts a packed bluetooth address to a human readable string
    """
    pass

def btohl(integer): # real signature unknown; restored from __doc__
    """
    btohl(integer) -> integer
    
    Convert a 32-bit integer from bluetooth to host byte order.
    """
    return 0

def btohs(integer): # real signature unknown; restored from __doc__
    """
    btohs(integer) -> integer
    
    Convert a 16-bit integer from bluetooth to host byte order.
    """
    return 0

def cmd_opcode_ocf(opcode): # real signature unknown; restored from __doc__
    """
    cmd_opcode_ocf(opcode)
    
    Convenience function to extract and return the OCF value from an opcode
    """
    pass

def cmd_opcode_ogf(opcode): # real signature unknown; restored from __doc__
    """
    cmd_opcode_ogf(opcode)
    
    Convenience function to extract and return the OGF value from an opcode
    """
    pass

def cmd_opcode_pack(ogf, ocf): # real signature unknown; restored from __doc__
    """
    cmd_opcode_pack(ogf, ocf)
    
    packs an OCF and an OGF value together to form a opcode
    """
    pass

def fromfd(fd, family, type, proto=None): # real signature unknown; restored from __doc__
    """
    fromfd(fd, family, type[, proto]) -> socket object
    
    Create a socket object from the given file descriptor.
    The remaining arguments are the same as for socket().
    """
    pass

def getdefaulttimeout(): # real signature unknown; restored from __doc__
    """
    getdefaulttimeout() -> timeout
    
    Returns the default timeout in floating seconds for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    return timeout

def hci_close_dev(dev_id): # real signature unknown; restored from __doc__
    """
    hci_close_dev(dev_id)
    
    closes the specified device id.  Note:  device id is NOT a btoscket.
    You can also use btsocket.close() to close a specific socket.
    """
    pass

def hci_devid(address): # real signature unknown; restored from __doc__
    """
    hci_devid(address)
    
    get the device id for the local device with specified address.
    """
    pass

def hci_filter_all_events(*args, **kwargs): # real signature unknown
    """ all events! """
    pass

def hci_filter_all_ptypes(*args, **kwargs): # real signature unknown
    """ all packet types! """
    pass

def hci_filter_clear(*args, **kwargs): # real signature unknown
    """ clear filter """
    pass

def hci_filter_clear_event(*args, **kwargs): # real signature unknown
    """ clear event! """
    pass

def hci_filter_clear_opcode(*args, **kwargs): # real signature unknown
    """ clear opcode! """
    pass

def hci_filter_clear_ptype(*args, **kwargs): # real signature unknown
    """ clear ptype! """
    pass

def hci_filter_new(): # real signature unknown; restored from __doc__
    """
    hci_filter_new()
    
    Returns a new HCI filter suitable for operating on with the hci_filter_*
    methods, and for passing to getsockopt and setsockopt.  The filter is
    initially cleared
    """
    pass

def hci_filter_set_event(*args, **kwargs): # real signature unknown
    """ set event! """
    pass

def hci_filter_set_opcode(*args, **kwargs): # real signature unknown
    """ set opcode! """
    pass

def hci_filter_set_ptype(*args, **kwargs): # real signature unknown
    """ set ptype! """
    pass

def hci_filter_test_event(*args, **kwargs): # real signature unknown
    """ test event! """
    pass

def hci_filter_test_opcode(*args, **kwargs): # real signature unknown
    """ test opcode! """
    pass

def hci_filter_test_ptype(*args, **kwargs): # real signature unknown
    """ test ptype! """
    pass

def hci_inquiry(dev_id=0, duration=8, flush_cache=True, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    hci_inquiry(dev_id=0, duration=8, flush_cache=True
    
    Performs a device inquiry using the specified device (usually 0 or 1).
    The inquiry will last 1.28 * duration seconds.  If flush_cache is True, then
    previously discovered devices will not be returned in the inquiry.)
    """
    pass

def hci_open_dev(*args, **kwargs): # real signature unknown
    """ hci_open_dev """
    pass

def hci_read_remote_name(sock, bdaddr, timeout=5192): # real signature unknown; restored from __doc__
    """
    hci_read_remote_name(sock, bdaddr, timeout=5192)
    
    Performs a remote name request to the specified bluetooth device.
       sock - the HCI socket object to use
       bdaddr - the bluetooth address of the remote device
       timeout - maximum amount of time, in milliseconds, to wait
    
    Returns the name of the device, or raises an error on failure
    """
    pass

def hci_send_cmd(*args, **kwargs): # real signature unknown
    """
    hci_send_command(sock, ogf, ocf, params)
    
    Transmits the specified HCI command to the socket.
        sock     - the btoscket object to use
        ogf, pcf - see bluetooth specification
        params   - packed command parameters (use the struct module to do this)
    """
    pass

def hci_send_req(sock, ogf, ocf, event, rlen, params=None, timeout=0): # real signature unknown; restored from __doc__
    """
    hci_send_req(sock, ogf, ocf, event, rlen, params=None, timeout=0)
    
    Transmits a HCI cmomand to the socket and waits for the specified event.
       sock      - the btsocket object
       ogf, ocf  - see bluetooth specification
       event     - the event to wait for.  Probably one of EVT_*
       rlen      - the size of the returned packet to expect.  This must be
                   specified since bt won't know how much data to expect
                   otherwise
        params   - the command parameters
        timeout  - timeout, in milliseconds
    """
    pass

def htobl(integer): # real signature unknown; restored from __doc__
    """
    htobl(integer) -> integer
    
    Convert a 32-bit integer from host to bluetooth byte order.
    """
    return 0

def htobs(integer): # real signature unknown; restored from __doc__
    """
    htobs(integer) -> integer
    
    Convert a 16-bit integer from host to bluetooth byte order.
    """
    return 0

def sdp_advertise_service(socket, name): # real signature unknown; restored from __doc__
    """
    sdp_advertise_service( socket, name )
    
    Registers a service with the local SDP server.
    
    socket must be a bound, listening socket - you must have already
    called socket.listen().  Only L2CAP and RFCOMM sockets are supported.
    
    name is the name that you want to appear in the SDP record
    
    Registered services will be automatically unregistered when the socket is
    closed.
    """
    pass

def sdp_stop_advertising(socket): # real signature unknown; restored from __doc__
    """
    sdp_stop_advertising( socket )
    
    stop advertising services associated with this socket
    """
    pass

def setdefaulttimeout(timeout): # real signature unknown; restored from __doc__
    """
    setdefaulttimeout(timeout)
    
    Set the default timeout in floating seconds for new socket objects.
    A value of None indicates that new socket objects have no timeout.
    When the socket module is first imported, the default is None.
    """
    pass

def str2ba(string): # real signature unknown; restored from __doc__
    """
    str2ba(string)
    
    Converts a bluetooth address string into a packed bluetooth address.  The
    string should be of the form "XX:XX:XX:XX:XX:XX"
    """
    pass

# classes

class btsocket(object):
    """
    BluetoothSocket(proto=RFCOMM) -> bluetooth socket object
    
    Open a socket of the given protocol.  proto must be one of
    HCI, L2CAP, RFCOMM, or SCO.  SCO sockets have
    not been tested at all yet.
    
    A BluetoothSocket object represents one endpoint of a bluetooth connection.
    
    Methods of BluetoothSocket objects (keyword arguments not allowed):
    
    accept() -- accept a connection, returning new socket and client address
    bind(addr) -- bind the socket to a local address
    close() -- close the socket
    connect(addr) -- connect the socket to a remote address
    connect_ex(addr) -- connect, return an error code instead of an exception
    dup() -- return a new socket object identical to the current one
    fileno() -- return underlying file descriptor
    getpeername() -- return remote address
    getsockname() -- return local address
    getsockopt(level, optname[, buflen]) -- get socket options
    gettimeout() -- return timeout or None
    listen(n) -- start listening for incoming connections
    makefile([mode, [bufsize]]) -- return a file object for the socket
    recv(buflen[, flags]) -- receive data
    recvfrom(buflen[, flags]) -- receive data and sender's address
    sendall(data[, flags]) -- send all data
    send(data[, flags]) -- send data, may not send all of it
    sendto(data[, flags], addr) -- send data to a given address
    setblocking(0 | 1) -- set or clear the blocking I/O flag
    setsockopt(level, optname, value) -- set socket options
    settimeout(None | float) -- set or clear the timeout
    shutdown(how) -- shut down traffic in one or both directions
    """
    def accept(self): # real signature unknown; restored from __doc__
        """
        accept() -> (socket object, address info)
        
        Wait for an incoming connection.  Return a new socket representing the
        connection, and the address of the client.  For L2CAP sockets, the address
        is a (host, psm) tuple.  For RFCOMM sockets, the address is a (host, channel)
        tuple.  For SCO sockets, the address is just a host.
        """
        pass

    def bind(self, address): # real signature unknown; restored from __doc__
        """
        bind(address)
        
        Bind the socket to a local address.  address must always be a tuple.
          HCI sockets:    ( device number, )
                          device number should be 0, 1, 2, etc.
          L2CAP sockets:  ( host, psm )
                          host should be an address e.g. "01:23:45:67:89:ab"
                          psm should be an unsigned integer
          RFCOMM sockets: ( host, channel )
          SCO sockets:    ( host )
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        Close the socket.  It cannot be used after this call.
        """
        pass

    def connect(self, address): # real signature unknown; restored from __doc__
        """
        connect(address)
        
        Connect the socket to a remote address. For L2CAP sockets, the address is a 
        (host,psm) tuple.  For RFCOMM sockets, the address is a (host,channel) tuple.
        For SCO sockets, the address is just the host.
        """
        pass

    def connect_ex(self, address): # real signature unknown; restored from __doc__
        """
        connect_ex(address) -> errno
        
        This is like connect(address), but returns an error code (the errno value)
        instead of raising an exception when an error occurs.
        """
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """
        dup() -> socket object
        
        Return a new socket object connected to the same system resource.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> integer
        
        Return the integer file descriptor of the socket.
        """
        return 0

    def getpeername(self): # real signature unknown; restored from __doc__
        """
        getpeername() -> address info
        
        Return the address of the remote endpoint.  For HCI sockets, the address is a
        device number (0, 1, 2, etc).  For L2CAP sockets, the address is a 
        (host,psm) tuple.  For RFCOMM sockets, the address is a (host,channel) tuple.
        For SCO sockets, the address is just the host.
        """
        pass

    def getsockid(self, *args, **kwargs): # real signature unknown
        """ Gets socket id. """
        pass

    def getsockname(self): # real signature unknown; restored from __doc__
        """
        getsockname() -> address info
        
        Return the address of the local endpoint.
        """
        pass

    def getsockopt(self, level, option, buffersize=None): # real signature unknown; restored from __doc__
        """
        getsockopt(level, option[, buffersize]) -> value
        
        Get a socket option.  See the Unix manual for level and option.
        If a nonzero buffersize argument is given, the return value is a
        string of that length; otherwise it is an integer.
        """
        pass

    def gettimeout(self): # real signature unknown; restored from __doc__
        """
        gettimeout() -> timeout
        
        Returns the timeout in floating seconds associated with socket 
        operations. A timeout of None indicates that timeouts on socket 
        operations are disabled.
        """
        return timeout

    def listen(self, backlog): # real signature unknown; restored from __doc__
        """
        listen(backlog)
        
        Enable a server to accept connections.  The backlog argument must be at
        least 1; it specifies the number of unaccepted connection that the system
        will allow before refusing new connections.
        """
        pass

    def makefile(self, mode=None, buffersize=None): # real signature unknown; restored from __doc__
        """
        makefile([mode[, buffersize]]) -> file object
        
        Return a regular file object corresponding to the socket.
        The mode and buffersize arguments are as for the built-in open() function.
        """
        return file('/dev/null')

    def recv(self, buffersize, flags=None): # real signature unknown; restored from __doc__
        """
        recv(buffersize[, flags]) -> data
        
        Receive up to buffersize bytes from the socket.  For the optional flags
        argument, see the Unix manual.  When no data is available, block until
        at least one byte is available or until the remote end is closed.  When
        the remote end is closed and all data is read, return the empty string.
        """
        pass

    def recvfrom(self, buffersize, flags=None): # real signature unknown; restored from __doc__
        """
        recvfrom(buffersize[, flags]) -> (data, address info)
        
        Like recv(buffersize, flags) but also return the sender's address info.
        """
        pass

    def send(self, data, flags=None): # real signature unknown; restored from __doc__
        """
        send(data[, flags]) -> count
        
        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  Return the number of bytes
        sent; this may be less than len(data) if the network is busy.
        """
        pass

    def sendall(self, data, flags=None): # real signature unknown; restored from __doc__
        """
        sendall(data[, flags])
        
        Send a data string to the socket.  For the optional flags
        argument, see the Unix manual.  This calls send() repeatedly
        until all data is sent.  If an error occurs, it's impossible
        to tell how much data has been sent.
        """
        pass

    def sendto(self, data, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        sendto(data[, flags], address) -> count
        
        Like send(data, flags) but allows specifying the destination address.
        For IP sockets, the address is a pair (hostaddr, port).
        """
        pass

    def setblocking(self, flag): # real signature unknown; restored from __doc__
        """
        setblocking(flag)
        
        Set the socket to blocking (flag is true) or non-blocking (false).
        setblocking(True) is equivalent to settimeout(None);
        setblocking(False) is equivalent to settimeout(0.0).
        """
        pass

    def setsockopt(self, level, option, value): # real signature unknown; restored from __doc__
        """
        setsockopt(level, option, value)
        
        Set a socket option.  See the Unix manual for level and option.
        The value argument can either be an integer or a string.
        """
        pass

    def settimeout(self, timeout): # real signature unknown; restored from __doc__
        """
        settimeout(timeout)
        
        Set a timeout on socket operations.  'timeout' can be a float,
        giving in seconds, or None.  Setting a timeout of None disables
        the timeout feature and is equivalent to setblocking(1).
        Setting a timeout of zero is the same as setblocking(0).
        """
        pass

    def shutdown(self, flag): # real signature unknown; restored from __doc__
        """
        shutdown(flag)
        
        Shut down the reading side of the socket (flag == 0), the writing side
        of the socket (flag == 1), or both ends (flag == 2).
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class SDPSession(object):
    """
    SDPSession()
    
    TODO
    """
    def browse(self): # real signature unknown; restored from __doc__
        """
        browse()
        
        Browses all services advertised by connected SDP session
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """
        close()
        
        closes the connection with the SDP server.  No effect if a session is not open.
        """
        pass

    def connect(self, dest="localhost"): # real signature unknown; restored from __doc__
        """
        connect( dest = "localhost" )
        
        Connects the SDP session to the SDP server specified by dest.  If the
        session was already connected, it's closed first.
        
        dest specifies the bluetooth address of the server to connect to.  Special
        case is "localhost"
        
        raises _bluetooth.error if something goes wrong
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> integer
        
        Return the integer file descriptor of the socket.
        You can use this for direct communication with the SDP server.
        """
        return 0

    def search(self, UUID): # real signature unknown; restored from __doc__
        """
        search( UUID )
        
        Searches for a service record with the specified UUID.  If no match is found,
        returns None.  Otherwise, returns a dictionary
        
        UUID must be in the form "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", 
        where each X is a hexadecimal digit.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


class timeout(___bluetooth.error):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


