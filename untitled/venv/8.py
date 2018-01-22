url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'
ret1= url.split('/')

print(ret1)
print(log)
ret2=log.split()
print(ret2)
person={}

for data in ret2:
    d1,d2=data.split(':')
    if d2.isnumeric():
        person[d1]=int(d2)
    else:
        person[d1]=d2

print(person)