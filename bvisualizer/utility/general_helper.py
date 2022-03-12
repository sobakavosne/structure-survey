import pprint as P
import functools as F


def trace(x, *comments):
    P.pprint(x, comments) if comments else P.pprint(x)
    return x


def filter_empty_list(l):
    return list(filter(lambda x: len(x) != 0, l))


def head(l):
    return l[0]


def last(l):
    return l[-1]


def compose(*fns):
    return F.reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)
