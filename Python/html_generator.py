# functie want moet uitgevoerd worden in de main functie
def generate_html(value_position: int = 13, scale_position :int =31, xdata :list = None, ydata :list = None, xscale :int = 0, yscale :int = 300, debug :bool = False):  # value position indicates the position the values have in the html template
    template = open("../web/data display website (template).html", "r", newline="\n")
    generated_site = open("../web/generated_site.html", "w")

    # convert data from the files to lists
    template_lines = template.readlines()
    
    # convert template lines list to 3 string
    template_lines_first_half :str = ""
    template_lines_middel :str = ""
    template_lines_last_half :str = ""

    list_to_string_counter :int = 0

    for i in template_lines:
        if list_to_string_counter < value_position:
            template_lines_first_half += i
            list_to_string_counter += 1
        
        elif list_to_string_counter < scale_position:
            template_lines_middel += i
            list_to_string_counter += 1
        
        else:
            template_lines_last_half += i 

    if xdata == None:
    # convert raw sensordata to js list
        sensor_data = open("./sensordata.txt", "r")
        timestamped_data = sensor_data.readlines()
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

    # write scale string
    timestamp :str = "yAxes: [{ticks: {min: " + str(xscale) + ",max:" + str(yscale) +"}}],"
    # generate string of the site

    generated_site_string :str = template_lines_first_half + x_values + y_values + template_lines_middel + timestamp + template_lines_last_half

    # print debug vars
    if debug:
        debugprint(generated_site_string)
    
   # combine the string 
    return generated_site_string 

def debugprint(var1=None, var2=None, var3=None):
    if var1 != None:
        print("[type] tempalte lines: ",type(var1))
        print(var1)
    if var2 != None:
        print("[type] x values: ", type(var2))
        print(var2)
    if var3 != None:
        print("[type] y values: ", type(var3))
        print(var3)