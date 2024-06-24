import ctypes
import os

rust_module = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'rust_module.so'))

class RustList(ctypes.Structure):
    _fields_ = [("ptr", ctypes.POINTER(ctypes.c_int)), ("len", ctypes.c_size_t), ("capacity", ctypes.c_size_t)]

def transform(data):
    data_array = (ctypes.c_int * len(data))(*data)
    data_list = RustList(data_array, len(data), len(data))
    rust_module.transform.argtypes = [RustList]
    rust_module.transform.restype = RustList
    result = rust_module.transform(data_list)
    return [result.ptr[i] for i in range(result.len)]

def aggregate(data):
    data_array = (ctypes.c_int * len(data))(*data)
    data_list = RustList(data_array, len(data), len(data))
    rust_module.aggregate.argtypes = [RustList]
    rust_module.aggregate.restype = ctypes.c_int
    return rust_module.aggregate(data_list)

def analyze(data):
    data_array = (ctypes.c_int * len(data))(*data)
    data_list = RustList(data_array, len(data), len(data))
    rust_module.analyze.argtypes = [RustList]
    rust_module.analyze.restype = ctypes.c_double
    return rust_module.analyze(data_list)
