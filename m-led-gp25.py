import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
timer = machine.Timer()

def func(timer):
    global led
    led.toggle()
    
led.value(1)
time.sleep(4)

timer.init(freq=1, mode=machine.Timer.PERIODIC, callback=func)
