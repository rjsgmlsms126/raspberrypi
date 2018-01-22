while True:
    print('반복을 계속할까요?[예/아니요]:')
    answer=input()

    if answer=='예':
        print('반복을 계속합니다.')
    elif answer =='아니요':
        break
    else:
        print('정상적인 답변이 아닙니다')