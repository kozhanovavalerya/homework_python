from math import ceil


def square(a):
    if a == int(a):
        return a*a
    else:
        return ceil(a*a)
