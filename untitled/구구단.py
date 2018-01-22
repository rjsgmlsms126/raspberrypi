x = 1
total = 0
print("숫자를 입력하세요")
num=int(input())


for i in range(1,num+1):
    total=total+i

print("1~{0} 까지의 합은 {1} 입니다.".format(num,total))