import scoreDef
from scorelogin import login


from admin import do_by_admin
from student import do_by_student


students=[
    ['apple','홍길동',100,90,80,-1,-1,-1],
    ['banana','김세진',90,90,80,-1,-1,-1],
    ['cherry','고길동',80,90,80,-1,-1,-1],
    ['orange','마이콜',70,90,80,-1,-1,-1],
]


scoreDef.calc_total(students)
scoreDef.calc_average(students)
scoreDef.calc_rank(students)


if __name__ =='__main__':
    while True:
        user_id=login()

        if user_id: #로그인 성공
            if user_id=='admin':
                do_by_admin(students)
            else:
                do_by_student(students,user_id)
        else:
              print('로그인 실패-다시 실행하세요.')