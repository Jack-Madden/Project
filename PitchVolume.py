from gpiozero import DistanceSensor
from time import sleep


from pythonosc import osc_message_builder
from pythonosc import udp_client

sensor = DistanceSensor(echo=17, trigger=4)
sense = DistanceSensor(echo=22, trigger=27)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

while True:
    pitch = round(sensor.distance * 100 + 30)
    volume = sense.distance
    print(pitch)
    print(volume)
    sender.send_message('play_this', pitch, volume)
    sleep(.1)