import scoreDef
import scorelogin

def print_menu(admin_mode=True):
   print("성적관리 메뉴")
   print("출력(P) | 비밀번호 변경(M) | ID 변경(I) | 종료(X)")


def change_password():
    old_password=input("이전 비밀번호:")
    new_password=input("새로운 비밀번호:")
    new_password2=input("새로운 비밀번호 확인")

    #이전 비밀번호 확인
    if scorelogin.check_user_password(userId,old_password):
        if new_password==new_password2:
            scorelogin.set_user_info(userId,new_password)
        else:
            print("새로운 비밀번호가 일치하지 않습니다.")
    else:
        print("이전 비밀번호가 일치하지 않습니다.")


def do_by_student(students,userId):
    while True:
        print_menu()
        select=input('메뉴 선택:')
        if select =='P':
            print('-----출력 선택')
            scoreDef.print_myscore(students,userId)
        elif select=='M':
            pass
        elif select=='I':
            pass
        elif select=='X':
            print('-----종료 선택')
            break
        else:
            print('올바르지 않은 입력입니다.')