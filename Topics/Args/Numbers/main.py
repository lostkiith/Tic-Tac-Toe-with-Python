# put your python code here


def multiply(*args):
    if len(args) == 1:
        return args[0] * 1
    else:
        total = 1
        for n in args:
            total *= n
        return total
