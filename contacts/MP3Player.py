from pygame import mixer
class MP3Player :

    def __init__(self, list,base_dir):
        self.current=0
        self.status = False
        self.mp3_list = list
        self.base_dir=base_dir
        self.position=0
        mixer.init()

    def get_status(self):
        return self.status

    def play(self):
        print('%s를 재생합니다.'%self.mp3_list[self.current])
        mp3_file=self.base_dir+'/'+self.mp3_list[self.current]

        if self.position==0:
            mixer.music.load(mp3_file)
            mixer.music.play()
        else:
            mixer.music.unpause()
        self.status=True


    def pause(self):
        if self.status:
            self.position=mixer.music.get_pos()
            mixer.music.pause()
        print('%s 재생을 멈춤니다.' % self.mp3_list[self.current])
        self.status=False


    def next(self):
        self.current = (self.current+1)%len(self.mp3_list)
        self.play()

    def prev(self):
        if self.current == 0:
            self.current = len(self.mp3_list)-1
        else:
            self.current -= 1
        self.play()


    def select_song(self):
        print('----------------------------')
        for ix,son in enumerate(self,mp3_list):
            print(ix+1,song)
        print('----------------------------')
        self.current=int(input('음악선택:'))-1
        self.play()

    def shuffle(self):
        self.mode = not self.mode

        if self.mode:
            shuffle(self.mp3_list)
        else:
            self.mp3_list.sort()

        pass

