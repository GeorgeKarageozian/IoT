import time
import utime
import pycom
import config
import machine
from machine import Pin
import urequests as requests


#initialise tempreature sensor pins
adc = machine.ADC()
apin = adc.channel(pin='P16')


# initialise Ultrasonic Sensor pins
echo = Pin('P20', mode=Pin.IN)
trigger = Pin('P21', mode=Pin.OUT)
trigger(0)

#read the tempretature from the temperature sensor
millivolts = apin.voltage()
celsius = (millivolts - 500.0) / 10.0
string_celsius = str(celsius)

    
# Send the HTTP request to FTTT. 
def post_var():
    try:
        url = "https://maker.ifttt.com/trigger/door_opened/with/key/" + config.TOKEN
        headers = {"X-Auth-Token": config.TOKEN, "Content-Type": "application/json"}
        data = {"value1": string_celsius}
        req = requests.post(url=url, headers=headers, json=data)
        return req.json()
    except:
        pass



# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(20)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2

    return distance * -1




while True:
    
    print(celsius)
    time.sleep(2)
    #check the distance from the ultrasonic sensor
    if(distance_measure()) > 120:
        print("the door is closed")
    else:
        #if the door is open send the HTTP request
        post_var()
        print("OPEN!!")
 