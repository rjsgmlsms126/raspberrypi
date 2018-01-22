import time

class PerformanceDecorator:
    def __init__(self,f):
        print('Initilizing performance')
        self.func=f

    def __call__(self):
        start_time=time.time()
        self.func()
        print("------%s secondes -----"%(time.time() - start_time))



class NotificationDecorator:

    def __init__(self,f):
        self.func=f

    def __call__(self):
        print('********************************************')
        print('*공지사항: 오늘은 수업이 없습니다.*')
        print('********************************************')
        self.func()