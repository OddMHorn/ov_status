from machine import Pin
import time

def blinky():
    counter = 5
    p = Pin(4, Pin.OUT)

    while counter > 0:
        p.value(1)
        time.sleep(0.5)
        p.value(0)
        time.sleep(0.25)
        counter -= 1

    print("Done")