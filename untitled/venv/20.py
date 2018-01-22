names={
    'marry':10999,'sam':2111,'tom':20145,'key':21343
}

def f1(x):
    return x[0]

def f2(x):
    return x[1]



ret2=sorted(names.items(),key=f1)
print(ret2)

ret3=sorted(names.items(),key=f2)
print(ret3)

ret4=sorted(names.items(),key=f2,reverse=True)
print(ret4)