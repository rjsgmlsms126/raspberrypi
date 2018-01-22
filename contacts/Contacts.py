class Contact:
    def __init__(self,name,cell_phone,email='',address='',birthday=''):
        self.__name=name
        self.__cell_phone=cell_phone
        self.__email=email
        self.__address=address
        self.__birthday=birthday

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name=name

    def get_cell_phone(self):
        return self.__cell_phone

    def set_cell_phone(self,cell_phone):
        self.__cell_phone=cell_phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email=email

    def set_address(self,address):
        self.set_address=address

    def get_address(self):
        return self.__address

    def get_birthday(self):
        return self.get_birthday

    def set_birthday(self,birthday):
        self.__birthday=birthday

    def print(self):
        print('%-5s %-15s %-20s' % (self.__name, self.__cell_phone, self.__email))

    def print_detail(self):
        print('이름   :', self.__name)
        print('전화번호:', self.__cell_phone)
        print('email  : ', self.__email)
        print('주소   : ', self.__address)
        print('생일   :', self.__birthday)

    def __str__(self) -> str:
        return 'name=%s,cell_phone=%s,email:%s,address=%s,birthday=%s'%(self.name,self.__cell_phone,self.__email,self.__address,self.__birthday)

    def __eq__(self, o):
        if not isinstance(o.Contact):
            return False

        if self.__email==o.__email:
            return  True
        else:
            return False

    def as_dict(self):
        return \
            dict(
                __class__ = "Contact",
                __args__ = [],
                __kw__ = dict (
                    name=self.__name,
                    cell_phone=self.__cell_phone,
                    email=self.__email, address=self.__address,
                    birthday=self.__birthday
                )
            )





