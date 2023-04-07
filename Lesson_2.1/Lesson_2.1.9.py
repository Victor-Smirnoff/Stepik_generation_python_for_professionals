def spell(*args):
    if len(args) == 0:
        return {}
    else:
        d = {}
        for i in range(len(args)):
            if args[i][0].lower() not in d.keys():
                d[args[i][0].lower()] = len(args[i])
            else:
                if len(args[i]) > d[args[i][0].lower()]:
                    d[args[i][0].lower()] = len(args[i])
        return d
