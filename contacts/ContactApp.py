from ContackBook import ContackBook
from Contacts import Contact
contack_book=ContackBook()
from deco import PerformanceDecorator
from deco import NotificationDecorator

for ontacts in contack_book:
    #contacts.print()
    print(contacts)

def print_menu():
    print('출력(P) | 추가(A) | 검색(S) | 수정(U) | 삭제(D) | 종료(X)')



def select_menu():
    select=input('메뉴를 선택하세요.>')
    return select.upper()

@PerformanceDecorator
@NotificationDecorator

def main():
    while True:
        print_menu()
        command=select_menu()
        if(command=='P'):
            contack_book.print()
        elif(command=='A'):
            contack_book.add_contack()
        elif (command == 'S'):
            pass
        elif (command == 'U'):
            contack_book.update_contact()
        elif (command == 'D'):
            contack_book.delete_contack()
        elif (command == 'X'):
            print('종료합니다.')
            break
        else:
            print('잘못된 메뉴입니다. 다시 입력하세요')

if __name__  == '__main__' :
    main()