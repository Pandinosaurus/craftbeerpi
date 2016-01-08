import os
from subprocess import Popen, PIPE, call
from random import randint, uniform

def getW1Thermometer():
    try:
        arr = []
        for dirname in os.listdir('/sys/bus/w1/devices'):
            if(dirname != "w1_bus_master1"):
                arr.append(dirname)

        return json.dumps(arr)
    except:
        return json.dumps({})

def tempData1Wire(tempSensorId):
    try:
        ## Test Mode
        print app.testMode
        if (app.testMode == True):
            print "READ TEMP FROM FILE"
            pipe = Popen(["cat","w1_slave"], stdout=PIPE)
        else:
            print "READ REAL TEMP"
            pipe = Popen(["cat","/sys/bus/w1/devices/w1_bus_master1/" + tempSensorId + "/w1_slave"], stdout=PIPE)
        result = pipe.communicate()[0]
        ## parse the file
        if (result.split('\n')[0].split(' ')[11] == "YES"):
            temp_C = float(result.split("=")[-1])/1000 # temp in Celcius
        else:
            temp_C = -99 #bad temp reading
    except Exception as e:
        print e
        temp_C = round(randint(0,50),2)

    return round(temp_C)
