import qwiic

scale = qwiic.start_scale()
calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
meeting = qwiic.meeting(scale, calibration_factor, nul_gewicht, 100)  #argument in functie = aantal meetingen in lijst
