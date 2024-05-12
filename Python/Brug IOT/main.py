import html_generator
import testing.sensor_simulation as sensor_simulation
import time

i = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while i == 0:
        sensor_simulation.generate_sensordata()
        html_generator.generate_html()
        time.sleep(5)
        sensor_simulation.reset_data_list()