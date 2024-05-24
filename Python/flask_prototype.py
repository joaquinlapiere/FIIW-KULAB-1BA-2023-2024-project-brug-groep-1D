# Script die instaat voor het hosten van de webserver en die dient als "main" script

from flask import Flask  # Framework om een webserver op te zetten
import motor_control as motor  # Script die de GPIO pins gebruikt om zo signalen naar de arduino te sturen
import html_generator as html  # Script die een html bestand samensteld op basis van een template (het returnt ook een string)
import sensor_simulation as sensor  # Script om "sensordata" te generen (voor testen zonder de qwiic scale sensor)
import qwiic  # Uitbreiding op de qwiicscale library die het makkelijker maakt om metingen te maken

aantal_meetingen = 5  # Variable die het aantal meetingen aangeeft
signal_delay = 1  # Variable die aantal seconden dat de GPIO pin op hoog moet staan om een signaal door de sturen naar de arduino om de brug te besturen.

scale = qwiic.start_scale()
app = Flask(__name__)  # Maak een object aan van de flask module om de webserver aan te spreken

calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
sensor_data = qwiic.start_lijst(aantal_meetingen)  # maak een lijst aan voor de sensordata
time_stamp_list = qwiic.start_lijst(aantal_meetingen)  # maak een lijst aan voor de timestamps

# print enkele vars zodat kan gecheckt worden als ze juist zijn en check welk type ze zijn om type errors op te lossen
def debugprint():
    print("big list type: ",type(sensor_data))
    print("1 list type: ",type(sensor_data[0]))
    print("2 list type: ",type(sensor_data[1]))
    print("[0] list", sensor_data[0])
    print("[1] list", sensor_data[1])


# generate html with correct values
website = html.generate_html(13,31,time_stamp_list,sensor_data,min_sensor_data, max_sensor_data)

# deze functie wordt aangeroepen bij een http request naar de root pagina
@app.route('/')
def show_main_page():
    # Import global vars into function
    global website
    global sensor_data
    global time_stamp_list
    global aantal_meetingen

    # maak een nieuwe meting en sla de sensordata en timestamps op
    sensor_data, time_stamp_list = qwiic.meeting(scale, calibration_factor, nul_gewicht, sensor_data, time_stamp_list, aantal_meetingen)  #argument in functie = aantal meetingen in lijst
    
    # bepaal de grenzen voor de data
    max_sensor_data: int = round(max(sensor_data))
    min_sensor_data: int = round(min(sensor_data))
    
    # generate new html
    website = html.generate_html(13,31,time_stamp_list,sensor_data,min_sensor_data, max_sensor_data)
    # render de webpagina 
    return website

# hier onder zijn extra functies te vinden die aan te roepen zijn door de knoppen op de web pagina (deze zullen ook allemaal de main page tonen)

# deze functie wordt aangeroepen bij een http request naar de /calibrate pagina
@app.route('/calibrate')
def calibrate():
    # calibreer de sensor
    calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
    return show_main_page()

# deze functie wordt aangeroepen bij een http request naar de /brug_open pagina
@app.route('/brug_open')
def brug_open():
    # roep het motor_control script aan om een signaal naar de arduino te sturen
    motor.brug_open(signal_delay) 
    return show_main_page()

# deze functie wordt aangeroepen bij een http request naar /brug_sluiten
@app.route('/brug_sluit')
def brug_sluit():
    # roep het motor_control script aan om een signaal naar de arduino te sturen
    motor.brug_sluit(signal_delay)
    return show_main_page()

# deze functie roep het qwiic script aan om de lijsten te legen
@app.route('/clear')
def clear():
    qwiic.clear()
    return show_main_page()