from random import  shuffle

listdata=list(range(1,11))
shuffle(listdata)
print(listdata)


result=[]
while listdata:
    min=listdata[0]
    minindex=0
    for i,value in enumerate(listdata):
        if min>value:
            min=value
            minindex=i


    result.append(min)
    listdata.pop(minindex)

print(result)