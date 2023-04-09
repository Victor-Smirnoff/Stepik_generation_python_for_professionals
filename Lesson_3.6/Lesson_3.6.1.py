import time

def calculate_it(func, *args):
    start_time = time.monotonic()
    a = func(*args)
    end_time = time.monotonic()
    res_time = end_time - start_time
    return a, res_time
