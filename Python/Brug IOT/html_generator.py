def generate_html():  # function because should be called in main.py
    sensor_data = open("./sensordata.txt", "r")
    template = open("web/data display website (template).html", "r", newline="\n")
    generated_site = open("web/generated_site.html", "w")

    # convert data from the files to lists
    timestamped_data = sensor_data.readlines()
    template_lines = template.readlines()

    # convert raw sensordata to js list
    x_values :str = "var xValues = " + timestamped_data[0] + ";"  # time data
    y_values :str = "var yValues = " + timestamped_data[1] + ";" # sensor data



    # write html head and load the lib
    generated_site.writelines(template_lines[:7])
    generated_site.writelines(template_lines[20:23])

    # write sensordata in the javascript section
    generated_site.writelines(x_values)
    generated_site.writelines(y_values)

    # write rest of the site
    generated_site.writelines(template_lines[26:])