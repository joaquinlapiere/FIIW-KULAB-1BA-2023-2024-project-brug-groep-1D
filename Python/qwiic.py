import qwiicscale
import time

Average_Amount: int = 100  #variabele die aanpast hoeveel getallen in de scale.getAverage() funcie gebruikt worden


def start_scale():
    scale = qwiicscale.QwiicScale()
    if not scale.begin():
        print("opstarten mislukt")
        return None
    print("opstarten gelukt")
    return scale


def nul_waarde(scale):
    print("als er geen gewicht op het plaatje hangt, duw op enter:")
    input()

    nul_gewicht = getAverage(scale, Average_Amount)
    return nul_gewicht


def calibrate_scale(scale):
    nul_gewicht = nul_waarde(scale)
    gekend_gewicht = float(input("hoe groot is het gewicht die zal gebruikt worden bij de kalibratie (in gram): "))
    print("plaats een gekende massa op het plaatje en duw op enter")
    input()

    raw_value = getAverage(scale, Average_Amount)
    calibration_factor = (raw_value - nul_gewicht) / gekend_gewicht
    print(f"Calibration factor: {calibration_factor}")

    return calibration_factor, nul_gewicht

def getAverage(scale, averageAmount):
    total = 0

    for i in range(0, averageAmount):
        total += scale.getReading()
        i +=1

    total /= averageAmount

    return total


def read_weight(scale, calibration_factor, nul_gewicht):
    raw_value = getAverage(scale, Average_Amount)
    gewicht = (raw_value - nul_gewicht) / calibration_factor
    return gewicht


def meeting(scale, calibration_factor, nul_gewicht, aantal_meetingen, reading_interval: int = None):

    print("Starting weight measurement...")
    for i in range(0, aantal_meetingen):
        gewicht = read_weight(scale, calibration_factor, nul_gewicht)
        print(f"Weight: {gewicht:.2f} grams")
        time.sleep(reading_interval)
        meetingen: list = [None]*aantal_meetingen
        meetingen[i] = gewicht
        i += 1

    return meetingen

#while True:
#   sensorwaarde = qwiicscale.getReading()

    #raw_time = datetime.datetime.now()
    #tijd = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second)

#   print(sensorwaarde)
