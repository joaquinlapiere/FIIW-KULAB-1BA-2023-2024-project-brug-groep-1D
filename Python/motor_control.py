# Script die de GPIO pinnen aanroept en zo de arduino aanstuurt

from gpiozero import LED  # Lib voor GPIO aansturing
import time  # lib voor alles wat met tijd te maken heeft

# de GPIO pinnen die gebruikt zullen worden
brug_open_pin = LED(17)
brug_sluit_pin = LED(18)

# functie om de brug te openen (en om eventueel een tijdsduur in te stellen hoe lang het signaal gegeven kan worden)
def brug_open(delay = None):
    print("brug opening...")  # temp testing
    brug_open_pin.on()
    if delay:
        time.sleep(delay)
    brug_open_pin.off()

# functie om de brug te sluiten (en om eventueel een tijdsduur in te stellen hoe lang het signaal gegeven kan worden)
def brug_sluit(delay = None):
    print("brug closing...")  # temp testing
    brug_sluit_pin.on()
    if delay:
        time.sleep(delay)
    brug_sluit_pin.off()