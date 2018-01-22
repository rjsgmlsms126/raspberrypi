def print_something(*args):
    min=args[0]
    for s in args:
        if s<min:
            min=s

    return min


def max_something(*args):
    max=args[0]
    for s in args:
        if s>max:
            max=s

    return max

def add_sum(*args):
    sum=0
    for s in args:
        sum=sum+s
    return sum


def divide_sum(*args):
    return int(add_sum(*args)/len(args))

def findMinMax(*args):
    return min(*args),max(*args)




data=[23,12,6,8,10,9]


min=print_something(*data)
max=max_something(*data)

#values=findMinMax(*data)
min,max=findMinMax(*data)
