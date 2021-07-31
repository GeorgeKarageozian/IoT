# IoT
Course project tutorial
# Notification system for opened door and reporting current temperature
George Karageozian (gk222iq)
This tutorial if for my project for the course Introcution to IoT (1DT305). The purpose of the project is to use LoPy4 by Pycom with MicroPython alongside with ultrasound and tempreature sensors to get a notification on your mobile or smart watch when a door is opened. The  tempreature of the room is also reported in the notification.
If you have all the materials needed ready, the setup might take between 2 to 4 hours.


# Objective
I chose this project becuse i need this kind of device at home. I don't want my niece or nephew to go into my room and break my laptop or other things and unfortunately i cannot instal a lock to my door. This device will help me to get a notification on my mobile and my smart watch the moment they open the door. 

Anyone who is interested in knowing if someone is sneaking into their room can use this device to get a notification about it. The device is quite small as well so you can hide it and no one can see it but you still get the notification in case of an intruder wants to access your room. 

The idea of reporting the tempreature as an extra information was because i have installed the sensor while learning how to connect sensors to the Pycom and when i discovered that it is possible to include it in the notifications so i decided to keep it. It is possible to install any sensor and get the data inside the notification.

# Material
The materia needed for the project are the follows:
**-loPy4 with expansion board**
A programmable board that is simple to use and connect. It has a built in WiFi and you can connect an antenna to connect to other networks, for example, LoRa.
For more information about loPy4: https://pycom.io/product/lopy4/ 
![](https://i.imgur.com/oLwFP5X.png)


**-Temperature sensor MCP9700**
A tempreature sensor that you can connect to loPy4 that can read the temperature. It can measure tempreature between 0 and 70 degrees celsius. It has three pins and is easy to connect
![](https://i.imgur.com/sj7JV4i.jpg)

**-Ultrasonic sensor HC-SR04**
This sensor uses ultrasonic sound to measure the distance. It can measure between 2 cm to 4 meters distance. It has three pins and easy to connect.
![](https://i.imgur.com/sfhS513.jpg)

**Breadboard**
A device that allows you to connect wires and sensors without soldering. 
![](https://i.imgur.com/OQLdPdg.jpg)

**-Wires**
Wires are used to connect the loPy4 with the breadboard snd the sensors.
![](https://i.imgur.com/7x4Ledm.jpg)

**-Micro USB cable**
The cable is used to connect the loPy4 device to your computer so you can upload your code or update the firmware of the LoPy4.


I have bought the material from Elektrokit which was recommended by the univeristy course. The bundle costs 949 kronor and some some extra things which i am not using in my project, for example, an antenna and led lights. Here is the link for electrokit:
https://www.electrokit.com/produkt/lnu-1dt305-tillampad-iot-lopy4-and-sensors-bundle/

The ultrasound sensor was bought from Amazon and it costs 49 kronor. Here is the link:
https://www.amazon.se/ANGEEK-HC-SR04-Ultrasonic-Detector-Distance/dp/B07KPJNLSS/ref=sr_1_2?dchild=1&keywords=ultrasonic+sensor+arduino&qid=1625167015&sr=8-2

# Computer setup

In order to work with loPy4, you need to connect it to the extention board to be able to connect it to your computer using a USB cable. It is also recommended to upgrade the firmware to use the cloud service from Pycom. 

A detailed explanation about these steps along with instructions are provided on pycom website. https://docs.pycom.io/gettingstarted/
https://docs.pycom.io/updatefirmware/device/

You also need to download an IDE (integrated development environment), if you already don't have one. My choice of IDE is Visual Studio Code by Microsoft. You can download it here. https://code.visualstudio.com 
You can also choose different IDE, for example, atom.

You need to install Pymakr extention on your IDE in order to connect with loPy4. https://pycom.io/products/supported-networks/pymakr/

The Pymakr extention requires to install NodeJS on your machine. https://nodejs.org/en/

Now the software on your computer is ready to interact with loPy4. Once you connect the device with your computer using the USB cable and have the IDE open, you will see the Pymakr console that has buttons like run and upload. The upload button uploads your code onto loPy4. You can use the sample code provided on Pycom website to light the LEDs on your device. https://docs.pycom.io/gettingstarted/

Finally, you need to connect to pybytes in order to connect your device to WiFi https://docs.pycom.io/pybytes/gettingstarted/


# Putting everything together
We need to connect the temperature sensor and the ultrasound sensor with the loPy4 using the breadboard.
You can read the datasheets for the temperatre sensor here: https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf
You can read the datasheet for the ultrasound sensor here: https://datasheetspdf.com/pdf-file/1380136/ETC/HC-SR04/1

To connect the temperature sensor you need to connect the positive voltage to 3.3v pin, the ground into GND and the output to P16 (If you want, you can use other pins. Check https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf for full shecmatic of the pins)

To connect the ultrasound sensor you need to connect the Gnd to GND, Echo to P20, Trig to P21 and Vcc to Vin. (If you want, you can use other pins. Check https://docs.pycom.io/gitbook/assets/lopy4-pinout.pdf for full shecmatic of the pins)

The connection with the device and the sensors should look similar to this.

![](https://i.imgur.com/Wv4pXlD.png)



# Platform
The cloud platform I chose to use is IFTTT (If This Then That). This platform allows to create responses to events that occur. In our case we want to get a notification (response) when an event occurs (when the ultrasonic sensor reaches the threshold). 
The programs that you create are called applets and you can access it throught the IFTTT website or IOS and android applications.
It is possible to create webhooks which are automated messages that are sent when something happens (in our case is the ulstrasonic sensor reaches the threshold).

You have to create an account on https://ifttt.com/home then create applets. Then create an applet. You choose "webhooks" for if this and you type the event name, for example, door_opened. Then choose "notifications" for then that and add ingredient value 1 (We will add the temperature value here). You also need to get a token which is found in my services -> webhooks -> documentation. Copy your key because we will use it later in the code. Now you can make a POST request to IFTTT with the format https://maker.ifttt.com/trigger/{event}/with/key/dlETWmClEqZonOFN5h9sp6 

# Code
The ultrasonic sensor requires a library which you can find it here alongside with other sensors that you might want to add to your project. https://gitlab.lnu.se/1dt305/sensor-libs 

You can create a project folder which will include the files: config.py, main.py, urequests.py and wifi.py.

In the config.py file you can add your WiFi credentials and IFTTT token as follows:

``` python
NETWORK_NAME = 'Your wifi network name'
NETWORK_PASSWORD = 'Your wifi network passoword'
TOKEN = "Your IFTTT token" 

```

The urequests.py which is a library to send requests is obtained from this tutorial: https://help.ubidots.com/en/articles/961994-connect-any-pycom-board-to-ubidots-using-wi-fi-over-http 
You can copy the file here: https://github.com/jotathebest/micropython-lib/blob/master/urequests/urequests.py 

wifi.py is to connect your device to wifi. 
The code is obtained from the tutorial https://hackmd.io/@lnu-iot/r1bGPUOhu 

```python
from network import WLAN
import machine
import config

wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == config.NETWORK_NAME:
        print('Network found!')
        wlan.connect(net.ssid, auth=(
            net.sec, config.NETWORK_PASSWORD), timeout=5000)
        while not wlan.isconnected():
            machine.idle()  # save power while waiting
        print('WLAN connection succeeded!')
        print(wlan.ifconfig())
        break
```

The main file is where your program runs.

```python
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
    #You can change the distance (120) to suit your settings depending on how far you have placed the ultrasonic sensor from the door
    if(distance_measure()) > 120:
        print("the door is closed")
    else:
        #if the door is open send the HTTP request
        post_var()
        print("OPEN!!")
 
```

When you upload the project to your loPy4 device you should see in the console the messages "the door is closed" pr "OPEN!!" alogside with the temperature printed. You should receive a notification on IFTTT website, your mobile app or smart watch when "OPEN!!" is printed on the console. The notification will also include the temperature. The trigger happens in this case when the distance between the door and the ultrasonic sensor is less than 120cm. (The door is openening inwards).

# Transmitting the data / connectivity

The data is sent through WiFi everytime the threshold of the ultrasonic sensor passes the limit. I am using WiFi becuause i don't have other networks LoRa or Sigfox in my area of living. You can add any other communication method you like that is supported by the device. The data sent as webhooks in JSON format which includes the event name and the value of the temperature. The size of the data is very small and is suitable to use with other networks.


# Presenting the data
The data sent from the loPy4 device can be shown in the IFTTT website, your phone or watch if you installed the application. The data is saved once the webhook sends POST requets which includes the event name and the value of the temperature
The website looks like this:

![](https://i.imgur.com/FHsBIDx.png)

The notification from the appliction on the phone looks like this:


![](https://i.imgur.com/VbspkR4.jpg)


# Finalizing the design
The final design of the project looks like this: 

![](https://i.imgur.com/an0wKjb.jpg)

Now i have a notification system that send a notification to my mobile phone or my smart watch when someone is entering my room while i am not there. It also provides the temperature. To extend the project, one can add more sensors, for example, air quality sensor to send you a notification and you can open the window. One can also install a camera for exaple to know who is the person coming into the room.
