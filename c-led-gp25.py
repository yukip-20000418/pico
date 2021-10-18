import digitalio
import board
import time

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

print(led.value)

while True:
    led.value = not led.value
    time.sleep(1)
