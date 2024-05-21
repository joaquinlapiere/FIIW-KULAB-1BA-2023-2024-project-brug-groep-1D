# functie want moet uitgevoerd worden in de main functie
def generate_html(value_position: int = 13, xdata :list = None, ydata :list = None):  # value position indicates the position the values have in the html template
    sensor_data = open("./sensordata.txt", "r")
    template = open("web/data display website (template).html", "r", newline="\n")
    generated_site = open("web/generated_site.html", "w")

    # convert data from the files to lists
    timestamped_data = sensor_data.readlines()
    template_lines = template.readlines()

    if xdata == None:
    # convert raw sensordata to js list
        x_values :str = "var xValues = " + str(timestamped_data[0]) + ";"  # time data
        y_values :str = "var yValues = " + str(timestamped_data[1]) + ";" # sensor data
    else: # adds sensordata from list
        x_values :str = "var xValues = " + str(xdata) + ";"
        y_values :str = "var yValues = " + str(ydata) + ";"  


    # write html head and load the lib
    generated_site.writelines(template_lines[:value_position])

    # write sensordata in the javascript section
    generated_site.writelines(x_values)
    generated_site.writelines(y_values)

    # write rest of the site
    generated_site.writelines(template_lines[value_position + 1:])
    return generated_site

generate_html(13)