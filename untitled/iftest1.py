members={
    'a':'1234',
    'b':'3234',
    'c':'4234',
    'd':'5234',
}


tryCounter=0;
userId=None

for tryCounter in range(3):
    if not userId:
        print('사용자 id를 입력하세요:', end='>')
        userId = input()

    print('비밀번호를 입력하세요:', end='>')
    userpassword = input()

    if userId in members.keys():
        password = members[userId]
        if userpassword ==password:
            print("로그인 성공")
            break
        else:
            print('비밀번호가 일치하지 않습니다.')
    else:
        print("%s는 존재하지 않는 사용자 ID입니다."%(userId))
        userId=None
    #tryCounter=tryCounter+1