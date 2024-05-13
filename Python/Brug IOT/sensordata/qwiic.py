from libraries import qwiicscale

qwiic = qwiicscale()
qwiic.begin()

sensorwaarde = qwiic.getReading()
