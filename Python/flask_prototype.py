from flask import Flask
import motor_control as motor
import html_generator as html
import sensor_simulation as sensor
import qwiic

aantal_meetingen = 5

scale = qwiic.start_scale()
app = Flask(__name__)

calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
sensor_data = qwiic.start_lijst(aantal_meetingen)
time_stamp_list = qwiic.start_lijst(aantal_meetingen)

# print enkele vars zodat kan gecheckt worden als ze juist zijn
def debugprint():
    print("big list type: ",type(sensor_data))
    print("1 list type: ",type(sensor_data[0]))
    print("2 list type: ",type(sensor_data[1]))
    print("[0] list", sensor_data[0])
    print("[1] list", sensor_data[1])


# generate html with correct values
website = html.generate_html(13,sensor_data[0],sensor_data[1])

@app.route('/')
def show_main_page():
    global website
    global sensor_data
    global time_stamp_list
    global aantal_meetingen
    sensor_data, time_stamp_list = qwiic.meeting(scale, calibration_factor, nul_gewicht, sensor_data, time_stamp_list, aantal_meetingen)  #argument in functie = aantal meetingen in lijst
    max_sensor_data: int = round(max(sensor_data))
    min_sensor_data: int = round(min(sensor_data))
    website = html.generate_html(13,31,time_stamp_list,sensor_data,min_sensor_data, max_sensor_data)
    
    return website

@app.route('/calibrate')
def calibrate():
    calibration_factor, nul_gewicht = qwiic.calibrate_scale(scale)
    return show_main_page()

@app.route('/brug_open')
def brug_open():
    motor.brug_open() 
    return show_main_page()

@app.route('/brug_sluit')
def brug_sluit():
    motor.brug_sluit()
    return show_main_page()

@app.route('/clear')
def clear():
    qwiic.clear()
    return show_main_page()