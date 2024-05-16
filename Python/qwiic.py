import qwiicscale
import time


def start_scale():
    scale = qwiicscale.QwiicScale()
    if not scale.begin():
        print("opstarten mislukt")
        return None
    print("opstarten gelukt")
    return scale


def calibrate_scale(scale, gekend_gewicht):
    print("als er geen gewicht op het plaatje hangt, duw op enter:")
    input()

    scale.zero()
    print("plaats een gekende massa op het plaatje en duw op enter")
    input()

    raw_value = scale.getAverage()
    calibration_factor = raw_value / gekend_gewicht
    print(f"Calibration factor: {calibration_factor}")

    return calibration_factor


def read_weight(scale, calibration_factor):
    raw_value = scale.getAverage()
    gewicht = raw_value / calibration_factor
    return gewicht


def main():
    scale = start_scale()
    if scale is None:
        return

    gekend_gewicht = float(input("hoe groot is het gewicht die zal gebruikt worden bij de kalibratie (in gram): "))
    calibration_factor = calibrate_scale(scale, gekend_gewicht)

    print("Starting weight measurement...")
    while True:
        gewicht = read_weight(scale, calibration_factor)
        print(f"Weight: {gewicht:.2f} grams")
        time.sleep(1)


if __name__ == "__main__":
    main()

""" while True:
    sensorwaarde = qwiicscale.getReading()

    #raw_time = datetime.datetime.now()
    #tijd = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second)

    print(sensorwaarde)
"""
