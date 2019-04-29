from gpiozero import DistanceSensor
from time import sleep


from pythonosc import osc_message_builder
from pythonosc import udp_client

sense = DistanceSensor(echo=22, trigger=27)
sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

while True:
    volume = sense.distance
    sender.send_message('/play_this', volume)
    print(volume)
    sleep(1)
