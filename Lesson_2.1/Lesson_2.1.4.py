def print_given(*args, **kwargs):
    if len(args) == 0 and len(kwargs) == 0:
        return None

    elif len(args) != 0 and len(kwargs) != 0:
        for arg in args:
            print(arg, type(arg))
        items = sorted(kwargs.items())
        for i in range(len(items)):
            print(items[i][0], items[i][1], type(items[i][1]))

    elif len(args) == 0 and len(kwargs) != 0:
        items = sorted(kwargs.items())
        for i in range(len(items)):
            print(items[i][0], items[i][1], type(items[i][1]))

    elif len(args) != 0 and len(kwargs) == 0:
        for arg in args:
            print(arg, type(arg))
