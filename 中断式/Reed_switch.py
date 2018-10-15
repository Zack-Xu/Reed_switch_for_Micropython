import machine
import time
Reed=machine.Pin(4,machine.Pin.IN)
LED=machine.Pin(2,machine.Pin.OUT)


def callback1(p):
    print("磁铁接近")
    LED.value(0)
    Reed.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback2)
    
def callback2(p):
    print("磁铁远离")
    LED.value(1)
    Reed.irq(trigger=machine.Pin.IRQ_RISING, handler=callback1)
    


def start():
    Reed.irq(trigger=machine.Pin.IRQ_RISING, handler=callback1)
