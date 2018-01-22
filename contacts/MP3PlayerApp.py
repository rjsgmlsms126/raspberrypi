from MP3Player import MP3Player
import glob

_BASE_DIR = 'c:/temp/mp3'

def create_player(base_dir=_BASE_DIR):
    file_list=glob.glob1(base_dir,'*.mp3')
    print(file_list)
    plyasr=MP3Player(file_list,_BASE_DIR)
    return plyasr



def print_menu(status):
    if status :
        print('곡선택(S) | 멈춤(U) | 다음(N) | 이전 (V) | 종료(X)')
    else:
        print('곡선택(S) | 재생(P) | 다음(N) | 이전 (V) | 종료(X)')


def load():
    if exists('config.dat'):
        with open('config.data','r')as file:
            mp3_player=create_player([])
            mp3_player.load(file)
    else:
        mp3_player=create_player()
    return  mp3_player()


def save():
    with open('config.data', 'w') as file:
       player.save(file)


def main():
    #mp3_player = create_player()
    mp3_player=load()
    while True :
        print_menu(mp3_player.get_status())
        select = input('선택 > ').upper()
        if select =='S':
            mp3_player.select_song()
        elif select =='P':
            mp3_player.play()
        elif select =='U':
            mp3_player.pause()
        elif select =='N':
            mp3_player.next()
        elif select =='V':
            mp3_player.prev()
        elif select =='X':
            return
        else:
            print_menu('잘못입력하였습니다.')

        # select에 따라 기능 호출

if __name__ == '__main__':
    main()