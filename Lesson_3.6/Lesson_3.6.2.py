import time
#
def get_the_fastest_func(funcs, arg):
    res = []
    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        res.append((end_time - start_time, func))
    return min(res)[1]
