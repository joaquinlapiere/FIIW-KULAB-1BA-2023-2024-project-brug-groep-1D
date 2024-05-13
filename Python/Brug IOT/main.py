import html_generator
import testing.sensor_simulation as sensor_simulation
import time

i = 0


if __name__ == '__main__':
    while i < 15:
        sensor_simulation.generate_sensordata()
        html_generator.generate_html(13)
        time.sleep(3) # wait 3 sec, site only reloads every 3sec
        sensor_simulation.reset_data_list()
        i += 1