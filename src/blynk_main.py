import blynklib
import requests
import subprocess
from time import sleep

#initialize Blynk
BLYNK_AUTH = '[BLYNK_AUTH]'
blynk = blynklib.Blynk(BLYNK_AUTH)

#Switchbot requests links
OPEN_DOOR = 'https://maker.ifttt.com/trigger/open_door/with/key/[YOUR KEY]'
ANSWER_DOOR = 'https://maker.ifttt.com/trigger/answer_door/with/key/[YOUR KEY]'

#register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    #print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if pin == 4 and value[0] == '1':
        print("Opening the door...")
        x = requests.post(OPEN_DOOR)
        print(x.text)

#register handler for virtual pin V3 write event
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    if pin == 3 and value[0] == '1':
        print("Answering and opening the door...")
        y = requests.post(ANSWER_DOOR)
        print(y.text)
        sleep(3)
        x = requests.post(OPEN_DOOR)
        print(x.text)
        subprocess.call('omxplayer door_answer.mp3', shell=True)

#register handler for virtual pin V2 write event
@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    if pin == 2 and value[0] == '1':
        print("Request to hold")
        subprocess.call('omxplayer door_wait.mp3', shell=True)

while True:
    blynk.run()
