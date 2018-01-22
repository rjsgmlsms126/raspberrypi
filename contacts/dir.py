import os, glob
from os.path import getsize

def print_file_info(dir_path,file_list):
    total_size=0

    print('---------------------------')
    print('NO \t 파일명 \t \t크기')
    print('---------------------------')
    for ix, file in enumerate(file_list):
        size=getsize(dir_path+'/'+file)
        total_size+=size
        print('%d \t %s \t %d'%(ix+1, file ,size))

    print('---------------------------')
    print('총 %d 개의 파일, 총 %d 바이트'%(len(file_list),total_size))


def dir(dir_path,filter=None):
    if filter:
        file_list=glob.glob1(dir_path,filter)
    else:
        file_list = os.listdir(dir_path)

    print_file_info(dir_path,file_list)
    select_file=int(input('선택>'))
    return  file_list[select_file-1]

dir('c:/temp/mp3','*.mp3')
print(song)