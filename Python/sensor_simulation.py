import random
import datetime



readings :int = 10  # amount of "readings this wil generate"
minimum :int = 0  # minimum value a reading could be
maxium :int = 32  # max value a reading could be

time_list :list = [] # list for time data
data_list :list = [] # list for sensor data


#readings :int = int(input("what amount of readings?"))

def generate_sensordata():
    global time_list
    global data_list

    data_file = open("./sensordata.txt","w")

    # get time
    raw_time = datetime.datetime.now()



    # generate and write data and time for {reading} times 
    for i in range(readings):
        # generate fake sensor data
        sensor_data :int = random.randint(minimum, maxium)  # generate fake sensor reading
        data_list.append(sensor_data)
    
        # generate timestamp list
        processed_time = str(raw_time.hour) + ":" + str(raw_time.minute) + ":" + str(raw_time.second + i)
        time_list.append(processed_time)

    # write data and time to datafile
    data_file.writelines(str(time_list))
    data_file.writelines("\n")
    data_file.writelines(str(data_list))

    data_file.close()

# clear global lists
def reset_data_list():
    global data_list
    global time_list
    data_list = []
    time_list = []

generate_sensordata() # call function for testing