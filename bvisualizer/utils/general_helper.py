import pprint as P
import functools as F


def trace(x, *comments):
  print(x, comments) if comments else P.pprint(x)
  return x


def filter_empty_list(l): return list(filter(lambda x: len(x) != 0, l))


def head(l): return l[0]


def last(l): return l[-1]


def compose(*fns):
  return F.reduce(lambda f, g: lambda x: f(g(x)), fns, lambda x: x)


def list_it(l):
  """
  -- recursively apply list() to all elements in the collection
  """ 
  return list(map(lambda x: list_it(x), l)) if type(l) \
    == (map or list or filter) else l
