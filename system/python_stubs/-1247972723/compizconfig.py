# encoding: utf-8
# module compizconfig
# from /usr/lib/python2.7/dist-packages/compizconfig.so
# by generator 1.138
"""
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

Authors:
    Quinn Storm (quinn@beryl-project.org)
    Patrick Niklaus (marex@opencompositing.org)
    Guillaume Seguin (guillaume@segu.in)
Copyright (C) 2007 Quinn Storm
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import operator as operator # <module 'operator' (built-in)>

# Variables with simple values

ProcessEventsNoGlibMainLoopMask = 1

# functions

def StringSettingKeyFunc(*args, **kwargs): # real signature unknown
    """
    itemgetter(item, ...) --> itemgetter object
    
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    pass

# classes

class Backend(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    IntegrationSupport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LongDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ProfileSupport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShortDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Context(object):
    """
    A python representation of a CCSContext.
    
        This is the main entry-point into the compizconfig module.
        Typical usage:
    
        >>> context = Context()
        >>> plugin = context.Plugins['core']
        >>> setting = plugin.Screen['number_of_desktops']
        >>> print setting.Value
        1
    """
    def Export(self, *args, **kwargs): # real signature unknown
        pass

    def Import(self, *args, **kwargs): # real signature unknown
        pass

    def LoadPlugin(self, *args, **kwargs): # real signature unknown
        pass

    def ProcessEvents(self, *args, **kwargs): # real signature unknown
        pass

    def Read(self, *args, **kwargs): # real signature unknown
        pass

    def ResetProfile(self, *args, **kwargs): # real signature unknown
        pass

    def UpdateExtensiblePlugins(self, *args, **kwargs): # real signature unknown
        pass

    def UpdateProfiles(self, *args, **kwargs): # real signature unknown
        pass

    def Write(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    AutoSort = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Backends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Categories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ChangedSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CurrentBackend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CurrentProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Integration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Plugins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Profiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Plugin(object):
    """
    A python representation of a CCSPlugin.
    
        You should not construct this object directly.
        Use context.Plugins['pluginname'] instead
    """
    def ApplyStringExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def GetExtensionBasePlugins(self, *args, **kwargs): # real signature unknown
        pass

    def SortSingleStringSetting(self, *args, **kwargs): # real signature unknown
        pass

    def SortStringSettings(self, *args, **kwargs): # real signature unknown
        pass

    def Update(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DisableConflicts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EnableConflicts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Features = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Initialized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LongDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Ranking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Screen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShortDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Profile(object):
    # no doc
    def Delete(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Setting(object):
    """
    A python representation of a CCSSetting.
    
        You should not construct this object directly.
        Use plugin.Screen['settingname'] instead
    """
    def Reset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Hints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Integrated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LongDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShortDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SubGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SSGroup(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    Screen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

ConflictTypeString = [
    'RequiresPlugin',
    'RequiresFeature',
    'ConflictFeature',
    'ConflictPlugin',
    'FeatureNeeded',
    'PluginNeeded',
    'PluginError',
]

SettingTypeString = [
    'Bool',
    'Int',
    'Float',
    'String',
    'Color',
    'Action',
    'Key',
    'Button',
    'Edge',
    'Bell',
    'Match',
    'List',
    'Invalid',
]

