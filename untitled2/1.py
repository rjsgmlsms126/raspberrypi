from tkinter import *
#from tkinter.ttk import *




class MyFrame(Frame):# Frame - 윈도우 관리 클래스
    def __init__(self, master):
        Frame.__init__(self, master) # master는 부모 윈도우
        self.master = master
        self.master.title("고객 입력")
        self.pack(fill=BOTH, expand=True) # 부모 윈도우 크기에 맞게 크기 조정
        #성명

        frameName = Frame(self)
        frameName.pack(fill=X, expand=True)
        lblName = Label(frameName, text="성명", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)
        self.entryName = Entry(frameName)
        self.entryName.pack(fill=X, padx=10, expand=True)
        #회사

        frameCompany = Frame(self)
        frameCompany.pack(fill=X)
        lblComp = Label(frameCompany, text="회사명", width=10)
        lblComp.pack(side=LEFT, padx=10, pady=10)
        self.entryComp = Entry(frameCompany)
        self.entryComp.pack(fill=X, padx=10, expand=True)
        #특징

        frameFeature = Frame(self, bg="blue")
        frameFeature.pack(fill=BOTH, expand=True)

        lblComment = Label(frameFeature, text="특징", width=10)
        lblComment.pack(side=LEFT, anchor=N, padx=10, pady=10)

        self.txtComment = Text(frameFeature, height=10)
        self.txtComment.pack(fill=BOTH, pady=10, padx=10,expand=True)
        # 저장

        frameSave = Frame(self)
        frameSave.pack(fill=X)

        self.btnSave = Button(frameSave, text="저장", command=lambda: self.on_click())
        self.btnSave.pack(side=LEFT, padx=10, pady=10)

    def on_click(self):
        print('[%s]' % self.entryName.get())
        print('[%s]' % self.entryComp.get())
        print('[%s]' % self.txtComment.get("1.0"))

        # print('[%s]'%self.txtComment.get("1.0",END))
        #print('[%s]' % self.txtComment.get("1.0", "end-1c"))



def main():
    root = Tk() # 메인 윈도우
    root.geometry("600x300+100+100") # 가로x세로+X위치+Y위치
    app = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
