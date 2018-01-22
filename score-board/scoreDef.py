_USER_ID_IX=0
_NAME_IX=1
_KOR_IX=2
_ENG_IX=3
_MATH_IX=4
_TOTAL_IX=5
_AVG_IX=6
_RANK_IX=7
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


def find_by_user_id(scores,userId):
    for score in scores:
        if userId==score[_USER_ID_IX]:
            return score
    return None


def find_index(scores,userId):
    for ix,score in enumerate(scores):
        if userId ==score[_NAME_IX]:
            return ix
    return -1


def modify_score(scores,**args):
    ix=find_index(scores,args["user_id"])
    if ix ==-1:
        print("존재하지 않습니다."%args["user_id:"])
        return

    score=scores[ix]

    score[_KOR_IX]=args["kor"]
    score[_ENG_IX]=args["eng"]
    score[_MATH_IX]=args["math"]

    score[_TOTAL_IX]=score[_KOR_IX]+score[_ENG_IX]+score[_MATH_IX]
    score[_AVG_IX]=score[_TOTAL_IX]/_SUBJECT_COUNT


def print_myscore(scores,userId):
    myscore=find_by_user_id(scores,userId)
    print_student([myscore])


def search(scores):
    name=input('검색할 이름')
    search_student=find_by_name(scores,name)
    if search_student:
       print_student(search_student)
    else:
        print("%s 학생이 없습니다"%name)


def print_student(scores,sort_fn=sort_name):
    print('----------------------------------------------')
    print(' 아이디  이름  국어  영어  수학  총점  평균  순위')
    print('----------------------------------------------')
    for score in scores:
        print("%5s%5s%5d%5d%5d  %5d %5d%5d"%(score[_USER_ID_IX],score[_NAME_IX],score[_KOR_IX],score[_ENG_IX],score[_MATH_IX],score[_TOTAL_IX],score[_AVG_IX],score[_RANK_IX]))
    print('----------------------------------------------')


def print_scores(scores,sort_fn=sort_name):
    avg=get_average(scores)
    scores.sort(key=sort_fn)
    print_student(scores)
    print('전체 평균 : %.2f'%avg)