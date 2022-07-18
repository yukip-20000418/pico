#micro python
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
cds = machine.ADC(2)
sw = machine.Pin(14, machine.Pin.OUT)

def func1(timer1):
    global led
    led.toggle()

def func2(timer2):
    global cds
    global sw
    v = cds.read_u16() * 3.3 / 65535
    sw.value(1 if v < 0.7 else 0)
    print("v={:.3f}".format(v))


led.value(1)
time.sleep(4)

timer1 = machine.Timer()
timer1.init(freq=1, mode=machine.Timer.PERIODIC, callback=func1)

timer2 = machine.Timer()
timer2.init(freq=2, mode=machine.Timer.PERIODIC, callback=func2)
