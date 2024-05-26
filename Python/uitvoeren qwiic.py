import qwiic

aantal_metingen = 5

scale = qwiic.start_scale()
calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
meetingen = qwiic.start_lijst(aantal_metingen)
time_stamp_list = qwiic.start_lijst(aantal_metingen)

for i in range(0, 6):
    meting, time_stamp_list = qwiic.meting(scale, calibration_factor, nul_gewicht, meetingen, time_stamp_list, aantal_metingen)
