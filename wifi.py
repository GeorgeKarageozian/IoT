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



