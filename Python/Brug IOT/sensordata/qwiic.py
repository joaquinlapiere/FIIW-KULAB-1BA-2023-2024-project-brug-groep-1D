from libraries import qwiicscale
#import datetime

qwiic = qwiicscale()
qwiic.begin()

while True:
    sensorwaarde = qwiic.getReading()

    #raw_time = datetime.datetime.now()
    #tijd = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second)

    print(sensorwaarde)
