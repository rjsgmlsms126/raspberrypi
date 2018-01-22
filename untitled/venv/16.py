def get_position(role):
 #   position=''
 #   if role == 'GK':
 ##       position ='골키퍼'
  #  elif role =='FW':
  ##      position='공격수'
   # elif role =='DF':
   #     position='수비수'
   # elif role =='GK':
   #     position ='골키퍼'
   # return position
   return{
       'GK':'골키퍼',
       'FW':'포워드',
       'MF':'미드필더',
       'DF':'수비수'
   }[role]


def f1(x):
    return x[0]


def f2(x):
    return x[1]


def print_team(what,**players):
    sortedPlayer=sorted(players.items(),key=what)
    print(sortedPlayer)

    for name,role in sortedPlayer:
        position=get_position(role)
        print('{0} = {1}'.format(position, name))

def get_sort_fn():
    print('선수 정렬 방법을 선택하세요')
    print('1) 이름순')
    print('2) 포지션순')
    what=input()
    if what=='1':
        return f1
    elif what=='2':
        return  f2
    else:
        return None

strategy=get_sort_fn()
print_team(strategy,카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF',
           카시야스2='GK', 호날두2='FW', 알론소2='MF', 페페2='DF',
           카시야스3 = 'GK', 호날두3 = 'FW', 알론소3 = 'MF', 페페3 = 'DF')



