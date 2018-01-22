from threading import Thread
import time
    class TemperatureSensor(Thread):
        def __init__(self, value=0, displacement=None, interval=1, on_change=None):
            Thread.__init__(self)
            self.sensor = temperature(value, displacement)
            self.value = value
            self.interval = interval
            self.on_change = on_change

        def measure(self):
            return self.value

        def run(self): # interval 간격으로 센서 값 갱신
            for value in self.sensor:
                time.sleep(self.interval)
                if self.on_change:
                    self.on_change(value)

if __name__ == '__main__': # test 코드
    ts = TemperatureSensor(on_change=lambda v:print(v) )
    ts.start()

    v=ts.measure()
    print('센서 기동')