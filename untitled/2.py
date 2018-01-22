dataList=['a','b','c','d','e']

print("인덱스 값을 입력하세요")
index=int(input())

if index >=0 and index < len(dataList):
    print(dataList[index])
else:
    print('잘못된 인덱스입니다')
    print('0~{0} 사이의 값을 입력하세요'.format(len(dataList)-1))