import qwiicscale
import datetime

Average_Amount: int = 100
Aantal_Iteraties: int = int(input('hoeveel iteraties?'))

scale = qwiicscale.QwiicScale()

while True:
    optie: int = int(input("welke optie? [1] rauwe sensordata, [2]rauwe sensordata + tijd, [3] Nulwaarde, [9] eind"))
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
        Nulwaarde: int = scale.getAverage(Average_Amount)

        print("nulwaarde gemeten: druk enter")
        input()
        waarde: int = 0
        for i in range(0, Aantal_Iteraties):
            waarde = scale.getReading() - Nulwaarde
            print(waarde)

    elif optie == 9:
        break