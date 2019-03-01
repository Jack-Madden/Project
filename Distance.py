from gpiozero import DistanceSensor
from time import sleep

import pythonosc


sensor = DistanceSensor(echo=17, trigger=4)
#sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

while True:
    pitch = round(sensor.distance * 100 + 30)
#/    sender.send_message('/play_this', pitch)
    print(pitch)
    sleep(.1)