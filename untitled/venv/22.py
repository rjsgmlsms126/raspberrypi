students=[
    ['홍길동',100,90,80,-1,-1,-1],
    ['김세진',90,90,80,-1,-1,-1],
    ['고길동',80,90,80,-1,-1,-1],
    ['마이콜',70,90,80,-1,-1,-1],

]

_NAME_IX=0
_KOR_IX=1
_ENG_IX=2
_MATH_IX=3
_TOTAL_IX=4
_AVG_IX=5
_RANK_IX=6
_SUBJECT_COUNT=3 #과목수

def calc_total(scores):
    for score in scores:
        score[_TOTAL_IX]=score[_KOR_IX]+score[_ENG_IX]+score[_MATH_IX]

def calc_average(scores):
    for score in scores:
        score[_AVG_IX]=score[_TOTAL_IX]/_SUBJECT_COUNT


def sort_fn(scores):
    return scores[_TOTAL_IX]

def sort_name(scores):
    return scores[_NAME_IX]

def calc_rank(scores):
    scores.sort(key=sort_fn,reverse=True)
    rank=0
    oldScore=-1
    for ix,score in enumerate(scores):
        if oldScore!=score[_TOTAL_IX]:
            rank=ix+1
            oldScore=score[_TOTAL_IX]

        scores[ix][_RANK_IX]=rank

def print_menu():
    print("성적관리 메뉴")
    print("출력(P) | 검색(S) | 종료(X)")

def get_average(scores):
    total=0
    for score in scores:
        total +=score[_AVG_IX]
    return total/len(scores)


def find_by_name(scores,name):
    result=[]
    for score in scores:
        if(name==score[_NAME_IX]):
            result.append(score)
    return result


def search(scores):
    name=input('검색할 이름')
    search_student=find_by_name(scores,name)
    if search_student:
       print_student(search_student)
    else:
        print("%s 학생이 없습니다"%name)


def print_student(scores,sort_fn=sort_name):
    print('------------------------------------------')
    print('   이름  국어  영어  수학  총점  평균  순위')
    print('------------------------------------------')
    for score in scores:
        print("%5s%5d%5d%5d  %5d %5d%5d"%(score[_NAME_IX],score[_KOR_IX],score[_ENG_IX],score[_MATH_IX],score[_TOTAL_IX],score[_AVG_IX],score[_RANK_IX]))
    print('------------------------------------------')


def print_scores(scores,sort_fn=sort_name):
    avg=get_average(scores)
    scores.sort(key=sort_fn)
    print_student(scores)
    print('전체 평균 : %.2f'%avg)



calc_total(students)
calc_average(students)
calc_rank(students)



while True:
    print_menu()
    select=input('메뉴 선택:')
    if select =='P':
        print('-----출력 선택')
        print_score(students)
    elif select =='S':
        print('----검색 선택')
        search(students)
    elif select=='X':
        print('-----종료 선택')
        break
    else:
        print('올바르지 않은 입력입니다.')
