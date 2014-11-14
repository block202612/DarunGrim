# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_DiffEngine', [dirname(__file__)])
        except ImportError:
            import _DiffEngine
            return _DiffEngine
        if fp is not None:
            try:
                _mod = imp.load_module('_DiffEngine', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _DiffEngine = swig_import_helper()
    del swig_import_helper
else:
    import _DiffEngine
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def GetDWORD(*args):
  return _DiffEngine.GetDWORD(*args)
GetDWORD = _DiffEngine.GetDWORD
class DBWrapper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DBWrapper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DBWrapper, name)
    __repr__ = _swig_repr
    def __init__(self, DatabaseName=None): 
        this = _DiffEngine.new_DBWrapper(DatabaseName)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _DiffEngine.delete_DBWrapper
    __del__ = lambda self : None;
DBWrapper_swigregister = _DiffEngine.DBWrapper_swigregister
DBWrapper_swigregister(DBWrapper)

class IDAController(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IDAController, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IDAController, name)
    __repr__ = _swig_repr
    def __init__(self, StorageDB=None): 
        this = _DiffEngine.new_IDAController(StorageDB)
        try: self.this.append(this)
        except: self.this = this
    def GetClientAnalysisInfo(self): return _DiffEngine.IDAController_GetClientAnalysisInfo(self)
    def GetClientFileInfo(self): return _DiffEngine.IDAController_GetClientFileInfo(self)
    def DumpAnalysisInfo(self): return _DiffEngine.IDAController_DumpAnalysisInfo(self)
    def DumpBlockInfo(self, *args): return _DiffEngine.IDAController_DumpBlockInfo(self, *args)
    def RemoveFromFingerprintHash(self, *args): return _DiffEngine.IDAController_RemoveFromFingerprintHash(self, *args)
    def GetBlockAddress(self, *args): return _DiffEngine.IDAController_GetBlockAddress(self, *args)
    def GetMappedAddresses(self, *args): return _DiffEngine.IDAController_GetMappedAddresses(self, *args)
    def GetDisasmLines(self, *args): return _DiffEngine.IDAController_GetDisasmLines(self, *args)
    def FreeDisasmLines(self): return _DiffEngine.IDAController_FreeDisasmLines(self)
    def ShowAddress(self, *args): return _DiffEngine.IDAController_ShowAddress(self, *args)
    __swig_destroy__ = _DiffEngine.delete_IDAController
    __del__ = lambda self : None;
IDAController_swigregister = _DiffEngine.IDAController_swigregister
IDAController_swigregister(IDAController)

class DiffMachine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DiffMachine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DiffMachine, name)
    __repr__ = _swig_repr
    def __init__(self, the_source=None, the_target=None): 
        this = _DiffEngine.new_DiffMachine(the_source, the_target)
        try: self.this.append(this)
        except: self.this = this
    def ShowDiffMap(self, *args): return _DiffEngine.DiffMachine_ShowDiffMap(self, *args)
    def PrintMatchMapInfo(self): return _DiffEngine.DiffMachine_PrintMatchMapInfo(self)
    def Analyze(self): return _DiffEngine.DiffMachine_Analyze(self)
    def AnalyzeFunctionSanity(self): return _DiffEngine.DiffMachine_AnalyzeFunctionSanity(self)
    def GetMatchAddr(self, *args): return _DiffEngine.DiffMachine_GetMatchAddr(self, *args)
    def GetUnidentifiedBlockCount(self, *args): return _DiffEngine.DiffMachine_GetUnidentifiedBlockCount(self, *args)
    def GetUnidentifiedBlock(self, *args): return _DiffEngine.DiffMachine_GetUnidentifiedBlock(self, *args)
    def Load(self, *args): return _DiffEngine.DiffMachine_Load(self, *args)
    def Save(self, *args): return _DiffEngine.DiffMachine_Save(self, *args)
    __swig_destroy__ = _DiffEngine.delete_DiffMachine
    __del__ = lambda self : None;
DiffMachine_swigregister = _DiffEngine.DiffMachine_swigregister
DiffMachine_swigregister(DiffMachine)

class DarunGrim(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DarunGrim, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DarunGrim, name)
    __repr__ = _swig_repr
    def SetLogParameters(self, *args): return _DiffEngine.DarunGrim_SetLogParameters(self, *args)
    def SetIDAPath(self, *args): return _DiffEngine.DarunGrim_SetIDAPath(self, *args)
    def AcceptIDAClientsFromSocket(self, storage_filename=None): return _DiffEngine.DarunGrim_AcceptIDAClientsFromSocket(self, storage_filename)
    def PerformDiff(self, *args): return _DiffEngine.DarunGrim_PerformDiff(self, *args)
    def SetSourceFilename(self, *args): return _DiffEngine.DarunGrim_SetSourceFilename(self, *args)
    def SetTargetFilename(self, *args): return _DiffEngine.DarunGrim_SetTargetFilename(self, *args)
    def Load(self, *args): return _DiffEngine.DarunGrim_Load(self, *args)
    def ShowAddresses(self, *args): return _DiffEngine.DarunGrim_ShowAddresses(self, *args)
    def ColorAddress(self, *args): return _DiffEngine.DarunGrim_ColorAddress(self, *args)
    def SetDatabase(self, *args): return _DiffEngine.DarunGrim_SetDatabase(self, *args)
    def StartIDAListener(self, *args): return _DiffEngine.DarunGrim_StartIDAListener(self, *args)
    def SetLogFilename(self, *args): return _DiffEngine.DarunGrim_SetLogFilename(self, *args)
    def GenerateSourceDGFFromIDA(self, *args): return _DiffEngine.DarunGrim_GenerateSourceDGFFromIDA(self, *args)
    def GenerateTargetDGFFromIDA(self, *args): return _DiffEngine.DarunGrim_GenerateTargetDGFFromIDA(self, *args)
    def GenerateDGFFromIDA(self, *args): return _DiffEngine.DarunGrim_GenerateDGFFromIDA(self, *args)
    def ConnectToDarunGrim(self, *args): return _DiffEngine.DarunGrim_ConnectToDarunGrim(self, *args)
    def GetIDALogFilename(self): return _DiffEngine.DarunGrim_GetIDALogFilename(self)
    def __init__(self): 
        this = _DiffEngine.new_DarunGrim()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _DiffEngine.delete_DarunGrim
    __del__ = lambda self : None;
DarunGrim_swigregister = _DiffEngine.DarunGrim_swigregister
DarunGrim_swigregister(DarunGrim)

# This file is compatible with both classic and new-style classes.


