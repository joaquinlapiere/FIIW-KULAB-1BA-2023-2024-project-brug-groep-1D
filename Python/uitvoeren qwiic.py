"""
Dit bestand dient als template hoe de "qwiic" bibliotheek toegepast moet worden in andere bestanden.
Eerst moet de "qwiic" bibliotheek geimporteerd worden. de globale variabele "aantal_metingen" moet ook op voorhand
gedefinieërd worden en de scale opgestart worden via de qwiic.start_scale() functie

De 3 stappen (callibration..., metingen..., time_stamp_list...) moeten worden uitgevoerd voordat metingen kunnen
uitgevoerd worden maar de volgorde is niet van belang.

De qwiic.meting() functie kan nu overal in het programma uitgevoerd worden. de for loop is ter illustratie en om te
testen of de template werkt. de time_interval parameter kan weggelaten worden maar None kan ook vervangen worden door
een getal die de tijd in seconden weergeeft van hoelang het programma zal wachten tussen 2 metingen.
"""

import qwiic

aantal_metingen = 5

scale = qwiic.start_scale()

calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
metingen = qwiic.start_lijst(aantal_metingen)
time_stamp_list = qwiic.start_lijst(aantal_metingen)

for i in range(0, 6):
    metingen, time_stamp_list = qwiic.meting(scale, calibration_factor, nul_gewicht, metingen, time_stamp_list,
                                           aantal_metingen, time_interval=None)
