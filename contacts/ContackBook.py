from Contacts import Contact
from math import ceil #올림함수 import

def sort_by_name(contact):
    return  contact.get_name()

_COUNT_PER_PAGE = 5

class ContackBook:
    def __init__(self):
        self.contact_list=[
            Contact('홍길동','010-1811-2222','hong@naver.com'),
            Contact('고길동', '010-1611-2222', 'qweng@naver.com'),
            Contact('마이컬', '010-5111-2222', 'hqrfag@naver.com'),
            Contact('백원우', '010-5411-2222', 'ho112@naver.com'),
            Contact('방정석', '010-7411-2222', '2ho112@naver.com'),
            Contact('최영환', '010-8471-2222', 'h3o112@naver.com'),
            Contact('정유진', '010-4785-2222', 'ho4112@naver.com'),
            Contact('이미주', '010-4161-2222', 'oho5112@naver.com'),
            Contact('최해란', '010-4131-2222', 'iho6112@naver.com'),
            Contact('김강열', '010-4121-2222', 'uho7112@naver.com'),
            Contact('지상훈', '010-4111-2222', 'lho8112@naver.com'),
            Contact('김민재', '010-4411-2222', 'kho9112@naver.com'),
            Contact('정수진', '010-5411-2222', 'jho0112@naver.com'),
            Contact('김종혁', '010-6411-2222', 'hho0112@naver.com'),
            Contact('김종희', '010-7411-2222', 'gho0112@naver.com'),
        ]
        self.contact_list.sort(key=sort_by_name)


    def add_contack(self):
        print("주소록 정보를 입력하세요")
        name=input("이름: ")
        cell_phone=input("전화번호: ")
        email=input("email: ")
        address=input("주소: ")
        birthday=input("생일:  ")
        contact=Contact(name, cell_phone, email, address, birthday)
        self.contact_list.append(contact)


    def print_page(self):
        start=(self.page-1)*_COUNT_PER_PAGE
        end=start+_COUNT_PER_PAGE

        print('------------------------------------------')
        print('No   이름     전화번호        email')
        print('------------------------------------------')
        for ix,contact in enumerate(self.contact_list[start:end]):
            print('%-5d'%(start+ix+1),end='')
            contact.print()
        print('------------------------------------------')
        print('[%d/%d], 총 %d 명'%(self.page, self.total_page, self.total_count))


    def previous_page(self):
        if self.page>1:
            self.page-=1
        self.print_page()

    def move_next_page(self):
        if self.page<self.total_page:
            self.page+=1
        self.print_page()

    def move_page(self):
        if self.page<1:
            self.page=1
        elif self.page>self.total_page:
            self.page=self.page
        self.print_page()


    def print(self):
        self.page=1
        self.total_count=len(self.contact_list)
        self.total_page= int(ceil(self.total_count/_COUNT_PER_PAGE))


        self.print_page()
        while True:
            select =input('>')
            if select =='P' or select=='p':
                pass
            elif select=='N' or select=='n':
                pass
            elif select=='Q' or select =='q':
                return
            else:
                if select.isnumeric():
                    page=int(select)


    def search(self):
        name=input('검색할이름: ')
        name=name.strip()
        if not name:
            print('검색할 이름이 없습니다.')
            return
        for contact in self.contact_list:
            if name== contact.get_name():
                return #break
        #else:
        print("%s는 주소록에 없습니다."%name)


    def print_detail(self,contact):
        print('##############################################################')
        contact.print_detail()
        print('##############################################################')


    def update_contact(self):
        name=input("수정할 이름 :")
        for contact in self.contact_list:
            if name== contact.get_name():
                break
        else:
            print("%s 는 주수록에 없습니다."%name)
            return

        print("전화번호: ",contact.get_cell_phone())
        call_phone=input("새 전화번호: ").strip()
        if cell_phone:
            contact.set_cell_phone(cell_phone)

        print("email: ",contact.get_email())
        email=input("새 email: ").strip()
        if email:
            contact.set_email(email)

        print("주소: ",contact.get_address())
        address=input("새 주소: ").strip()
        if address:
            contact.set_address(address)

        print("생일: ",contact.get_birthday())
        birthday=input("새 생일: ").strip()
        if birthday:
            contact.set_birthday(birthday)



    def delete_contack(self):
        name=input("삭제할 이름: ")
        index= -1
        for ix,contact in enumerate(self.contact_list):
            if name== contact.get_name():
                index=ix
                break

        if index!=-1:
            self.contact_list.pop(index)
            print('$s 주소록을 삭제했습니다'%name)

        else:
            print("%s는 주소록에 없습니다"%name)


    def __iter__(self):
        self.current=0
        return  self

    def __next__(self):
        total=len(self.contact_list)
        if self.current<total:
            current=self.current
            self.current+=1
            return self.contact_list[current]
        else:
            raise StopIteration()
