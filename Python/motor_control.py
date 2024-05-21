from gpiozero import LED

brug_open_pin = LED(17)
brug_sluit_pin = LED(18)

def brug_open():
    print("brug opening...")  # temp testing
    brug_open_pin.on()
    brug_open_pin.off()

def brug_sluit():
    print("brug closing...")  # temp testing
    brug_sluit_pin.on()
    brug_sluit_pin.off()

# temp for testing
def calibrate():
    print("calibrating...")