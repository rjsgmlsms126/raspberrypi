class Car:
    def __init__(self,color=0xFF0000,wheel_size=12,displacement=1500):
        self.color = 0xFF0000 # 바디의 색
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 엔진 배기량

    def print(self):
        print('색상:0x{:02x}'.format(self.color))
        print("바퀴크기: %d"%self.wheel_size)
        print("배기량: %dcc"%self.displacement)



    def forward(self): # 젂진
        pass

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회젂
        pass

    def turn_right(self): # 우회젂
        pass


if __name__ == '__main__':
        my_car = Car()

        print('0x{:02X}'.format(my_car.color))
        print(my_car.wheel_size)
        print(my_car.displacement)

        my_car.forward()
        my_car.backward()
        my_car.turn_left()
        my_car.turn_right()
