import qwiic

aantal_meetingen = 50

scale = qwiic.start_scale()
calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
meeting = qwiic.start_lijst(aantal_meetingen)
time_stamp_list = qwiic.start_lijst(aantal_meetingen)

meeting = qwiic.meeting(scale, calibration_factor, nul_gewicht, meeting, time_stamp_list)
