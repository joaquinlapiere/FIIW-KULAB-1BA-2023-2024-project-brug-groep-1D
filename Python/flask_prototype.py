from flask import Flask
import motor_control as motor
import html_generator as html
import sensor_simulation as sensor

app = Flask(__name__)

# get sensordata
sensor_data = sensor.generate_sensordata()  # temp testing (needs to get from qwiic)

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

    sensor_data = sensor.generate_sensordata()
    website = html.generate_html(13,sensor_data[0],sensor_data[1])
    
    return website

@app.route('/calibrate')
def calibrate():
    motor.calibrate()
    return show_main_page()

@app.route('/brug_open')
def brug_open():
    motor.brug_open() 
    return show_main_page()

@app.route('/brug_sluit')
def brug_sluit():
    motor.brug_sluit()
    return show_main_page()


####################
# temp for testing #
####################
brug_open()
brug_sluit()
calibrate()
show_main_page()