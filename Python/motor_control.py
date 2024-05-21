from gpiozero import LED
import time

brug_open_pin = LED(17)
brug_sluit_pin = LED(18)

def brug_open(delay = None):
    print("brug opening...")  # temp testing
    brug_open_pin.on()
    if delay:
        time.sleep(delay)
    brug_open_pin.off()

def brug_sluit(delay = None):
    print("brug closing...")  # temp testing
    brug_sluit_pin.on()
    if delay:
        time.sleep(delay)
    brug_sluit_pin.off()