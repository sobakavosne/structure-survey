def trace(x, *comments):
    print(x, comments) if comments else print(x)
    return x

def filterEmptyList(l):
    return list(filter(lambda x: len(x) != 0, l))

def head(l):
    return l[0]

def last(l):
    return l[-1]