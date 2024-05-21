from flask import Flask
import html_generator as html
import sensor_simulation

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world"
      
@app.route('/generated_site.html')
def show_main_page():
    return html.generate_html()

@app.route('/new reading')
def new_readin():
    sensor_simulation.generate_sensordata()
    sensor_simulation.reset_data_list()
    return 'Get new sensor reading'

@app.route('/autoreading')
def autoreading():
    return "toggle autoreading"