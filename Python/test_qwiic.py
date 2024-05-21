import qwiic
import datetime

Average_Amount: int = 10
Aantal_Iteraties: int = int(input('hoeveel iteraties?'))

scale = qwiic.start_scale()

while True:
    optie: int = int(input("welke optie? \n"
                           "[1] rauwe sensordata [2] rauwe sensordata + tijd, [3] Nulwaarde,\n"
                           "[4] waarde Nulwaarde [5] read_value functie       [9] eind"))
    if optie == 1:
        i: int = 0
        for i in range(0, Aantal_Iteraties):
            i = i + 1
            sensorwaarde = scale.getReading()
            print(sensorwaarde)

    elif optie == 2:
        i: int = 0
        for i in range(0, Aantal_Iteraties):
            i = i + 1
            sensorwaarde = scale.getReading()
            raw_time = datetime.datetime.now()
            tijd = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second)
            print(sensorwaarde, tijd)

    elif optie == 3:
        i: int = 0
        print("plaats geen gewicht en duw op enter")
        input()
        Nulwaarde: int = scale.getReading()

        print("nulwaarde gemeten: druk enter")
        input()
        waarde: int = 0
        for i in range(0, Aantal_Iteraties):
            waarde = scale.getReading() - Nulwaarde
            print(waarde)

    elif optie == 4:
        Nulwaarde: int = scale.getReading()
        print(f"1 meting: {Nulwaarde}")
        Nulwaarde = qwiic.getAverage(scale, Average_Amount)
        print(f"gemiddelde: {Nulwaarde}")

    elif optie == 5:
        calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
        for i in range(0, Aantal_Iteraties):
            sensorwaarde = qwiic.read_weight(scale, calibration_factor, nul_gewicht)

    elif optie == 9:
        break