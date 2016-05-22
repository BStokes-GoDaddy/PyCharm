# encoding: utf-8
# module appindicator._appindicator
# from /usr/lib/python2.7/dist-packages/appindicator/_appindicator.so
# by generator 1.138
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

CATEGORY_APPLICATION_STATUS = 0

CATEGORY_COMMUNICATIONS = 1
CATEGORY_HARDWARE = 3
CATEGORY_OTHER = 4

CATEGORY_SYSTEM_SERVICES = 2

STATUS_ACTIVE = 1
STATUS_ATTENTION = 2
STATUS_PASSIVE = 0

# functions

def app_indicator_get_type(*args, **kwargs): # real signature unknown
    pass

# classes

class Indicator(__gobject__gobject.GObject):
    """
    Object AppIndicator
    
    Signals from AppIndicator:
      scroll-event (gint, GdkScrollDirection)
      new-icon ()
      new-attention-icon ()
      new-status (gchararray)
      new-label (gchararray, gchararray)
      connection-changed (gboolean)
      new-icon-theme-path (gchararray)
    
    Properties from AppIndicator:
      id -> gchararray: The ID for this indicator
        An ID that should be unique, but used consistently by this program and its indicator.
      category -> gchararray: Indicator Category
        The type of indicator that this represents.  Please don't use 'other'. Defaults to 'ApplicationStatus'.
      status -> gchararray: Indicator Status
        Whether the indicator is shown or requests attention. Defaults to 'Passive'.
      icon-name -> gchararray: An icon for the indicator
        The default icon that is shown for the indicator.
      icon-desc -> gchararray: A description of the icon for the indicator
        A description of the default icon that is shown for the indicator.
      attention-icon-name -> gchararray: An icon to show when the indicator request attention.
        If the indicator sets it's status to 'attention' then this icon is shown.
      attention-icon-desc -> gchararray: A description of the icon to show when the indicator request attention.
        When the indicator is an attention mode this should describe the icon shown
      icon-theme-path -> gchararray: An additional path for custom icons.
        An additional place to look for icon names that may be installed by the application.
      connected -> gboolean: Whether we're conneced to a watcher
        Pretty simple, true if we have a reasonable expectation of being displayed through this object.  You should hide your TrayIcon if so.
      label -> gchararray: A label next to the icon
        A label to provide dynamic information.
      label-guide -> gchararray: A string to size the space available for the label.
        To ensure that the label does not cause the panel to 'jiggle' this string should provide information on how much space it could take.
      ordering-index -> guint: The location that this app indicator should be in the list.
        A way to override the default ordering of the applications by providing a very specific idea of where this entry should be placed.
      dbus-menu-server -> DbusmenuServer: The internal DBusmenu Server
        DBusmenu server which is available for testing the application indicators.
      title -> gchararray: Title of the application indicator
        A human readable way to refer to this application indicator in the UI.
    
    Signals from GObject:
      notify (GParam)
    """
    def build_menu_from_desktop(self, *args, **kwargs): # real signature unknown
        pass

    def get_attention_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_attention_icon_desc(self, *args, **kwargs): # real signature unknown
        pass

    def get_category(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_desc(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_theme_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_label(self, *args, **kwargs): # real signature unknown
        pass

    def get_label_guide(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu(self, *args, **kwargs): # real signature unknown
        pass

    def get_ordering_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_status(self, *args, **kwargs): # real signature unknown
        pass

    def set_attention_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_theme_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_label(self, *args, **kwargs): # real signature unknown
        pass

    def set_menu(self, *args, **kwargs): # real signature unknown
        pass

    def set_ordering_index(self, *args, **kwargs): # real signature unknown
        pass

    def set_status(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class IndicatorCategory(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    __gtype__ = None # (!) real value is ''


class IndicatorStatus(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
    }
    __gtype__ = None # (!) real value is ''


