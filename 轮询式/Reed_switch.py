import machine
Reed=machine.Pin(4,machine.Pin.IN)
LED=machine.Pin(2,machine.Pin.OUT)
def start():
    while(1):
        if(Reed.value()==1):
            LED.value(0)
            print('检测出磁铁')
        else:
            LED.value(1)
            print('未检测')
