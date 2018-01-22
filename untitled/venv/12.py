#solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
#ret = list(enumerate(solarsys))
#print(ret)
#for i, body in enumerate(solarsys):
#    print('태양계의 %d번째 천체: %s' %(i, body))

from random import shuffle
listdata = list(range(1, 11))
shuffle(listdata)
print(listdata)

min=listdata[0]
minindex=0


for i,value in enumerate(listdata):
    if min>value:
        min=value
        minindex=i

max=listdata[0]
maxindex=0
for i,value in enumerate(listdata):
        if max<value:
            max=value
            maxindex=i

print("최소값은 %d (인덱스:%d)입니다"%(min,minindex))
print("최대값은 %d (인덱스:%d)입니다"%(max,maxindex))