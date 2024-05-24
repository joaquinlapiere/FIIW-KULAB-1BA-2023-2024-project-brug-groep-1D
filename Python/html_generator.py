# Script die de webpagina samenstelt op basis van sensordata en een template
# note: dit script maakt ook een html generated bestand maar deze wordt niet meer gebruikt in de laaste versie
# enkel de return waarde wordt gebruikt om de html naar de webserver te schrijven

# functie want moet uitgevoerd worden in de main functie
# functie die veel parameters neemt
    # value position: de lijn in de html template waar de waarde geschreven moet worden
    # scale_position: de lijn in de html template waar de data die de scale instelt (en dus dynamisch maakt) geschreven moet worden
    # xdata: lijst voor data van de x-as (timestamps)
    # ydata: lijst voor data van de y-as (sensordata)
    # scale_min: minimum waarde voor de scale
    # scale_max: maximum waarde voor de scale
    # debug: bool om te bepalen als debug print moet gebeuren
def generate_html(value_position: int = 13, scale_position :int =31, xdata :list = None, ydata :list = None, scale_min :int = 0, scale_max :int = 300, debug :bool = False):  # value position indicates the position the values have in the html template
    template = open("../web/data display website (template).html", "r", newline="\n")
    generated_site = open("../web/generated_site.html", "w")

    # convert data from the files to lists
    template_lines = template.readlines()
    
    # convert template lines list to 3 string
    template_lines_first_half :str = ""
    template_lines_middel :str = ""
    template_lines_last_half :str = ""

    # counter om te zien op welke lijn in de template dat we zitten
    list_to_string_counter :int = 0

    # list to string converter (eerst type error problemen dus de lijst van strings wordt omgezet in de nodige string om het totaal terug samen te voegen 
    for i in template_lines:
        if list_to_string_counter < value_position:
            template_lines_first_half += i
            list_to_string_counter += 1
        
        elif list_to_string_counter < scale_position:
            template_lines_middel += i
            list_to_string_counter += 1
        
        else:
            template_lines_last_half += i 

    # Check als een lijst is mee gegeven in de functie die de sensordata bevat, anders default naar het sensordata bestand gegenereerd door het sensor data generator script
    if xdata == None:
    # convert raw sensordata to js list
    # neemt default data = data gegenereerd door sensordata generator
        sensor_data = open("./sensordata.txt", "r")
        timestamped_data = sensor_data.readlines()
        x_values :str = "var xValues = " + str(timestamped_data[0]) + ";"  # time data
        y_values :str = "var yValues = " + str(timestamped_data[1]) + ";" # sensor data
    else: # adds sensordata from list
        x_values :str = "var xValues = " + str(xdata) + ";"
        y_values :str = "var yValues = " + str(ydata) + ";"  


    # write html head
    generated_site.writelines(template_lines[:value_position])

    # write sensordata in the javascript section
    generated_site.writelines(x_values)
    generated_site.writelines(y_values)

    # write rest of the site
    generated_site.writelines(template_lines[value_position + 1:])

    # write scale string
    timestamp :str = "yAxes: [{ticks: {min: " + str(scale_min) + ",max:" + str(scale_max) +"}}],"

    # generate string of the site
    generated_site_string :str = template_lines_first_half + x_values + y_values + template_lines_middel + timestamp + template_lines_last_half

    # print debug vars
    if debug:
        debugprint(generated_site_string)
    
   # combine the string 
    return generated_site_string 

# function that prints vars and types (to resolve type errors)
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