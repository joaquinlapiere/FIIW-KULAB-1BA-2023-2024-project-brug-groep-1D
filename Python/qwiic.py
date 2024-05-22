import qwiicscale
import time

Average_Amount: int = 500  #variabele die aanpast hoeveel getallen in de scale.getAverage() funcie gebruikt worden

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

    total /= averageAmount

    return total


def read_weight(scale, calibration_factor, nul_gewicht):
    raw_value = getAverage(scale, Average_Amount)
    gewicht = (raw_value - nul_gewicht) / calibration_factor
    return gewicht


def start_lijst(aantal_meetingen):
    lijst: list = [0]*(aantal_meetingen * 5)
    return lijst

def lijst_opschuiven(lijst, aantal_meetingen):
    for i in range(0, aantal_meetingen):
        lijst[i] = lijst[aantal_meetingen + i]
        lijst[aantal_meetingen + i] = lijst[2*aantal_meetingen + i]
        lijst[2*aantal_meetingen + i] = lijst[3*aantal_meetingen + i]
        lijst[3*aantal_meetingen + i] = lijst[4*aantal_meetingen + i]
        lijst[4*aantal_meetingen + i] = 0

    return lijst


def meeting(scale, calibration_factor, nul_gewicht, meeting, time_stamp_list, aantal_meetingen, reading_interval = None):
    lijst_opschuiven(meeting, aantal_meetingen)
    lijst_opschuiven(time_stamp_list, aantal_meetingen)

    for i in range(0, aantal_meetingen):
        gewicht: int = round(read_weight(scale, calibration_factor, nul_gewicht))
        #print(f"Weight: {gewicht:.0f} gram")
        if reading_interval:
            time.sleep(reading_interval)
        meeting[4*aantal_meetingen+i] = gewicht
        time_stamp_list[4*aantal_meetingen+i] = time.strftime('%H:%M:%S')
    #print(meeting)
    #print(time_stamp_list)
    return meeting, time_stamp_list

#while True:
#   sensorwaarde = qwiicscale.getReading()

    #raw_time = datetime.datetime.now()
    #tijd = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second)

#   print(sensorwaarde)
