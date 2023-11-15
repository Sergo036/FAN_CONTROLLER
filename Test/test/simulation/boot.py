import gc,micropython
micropython.alloc_emergency_exception_buf(100)
gc.collect()
