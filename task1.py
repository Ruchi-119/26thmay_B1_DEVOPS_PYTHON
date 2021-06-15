import ctypes
i = 9
address = id(i)
print(address)
print(ctypes.cast(address,ctypes.py_object).value)