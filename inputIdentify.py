import keyboard
import datetime
import random
import pandas as pd
import time
import mouse


mouseA = {
    'id': [],
    'hour': [],
    'info': []
}
recorded_events = []
mouse_events = []
pressed = {
    'id': [],
    'hour': [],
    'key': []
}

track_info
{
    'id':
    'hour':
    'mouse_info':
    'keyboard_info': pressed
}


def input_call(duration):

    def key_assign(event):
        recorded_events.append(event)
        pressed['id'].append(str(random.randint(1, 13235235)))
        pressed['hour'].append(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        pressed['key'].append(str(event.name))

    def mouse_assign():
        mouseA['id'].append(str(random.randint(1, 13235235)))
        mouseA['hour'].append(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        mouseA['info'].append(str(mouse.get_position()))

    tracktime = duration * 60
    begin = time.time()
    keyboard.on_press(key_assign)
    mouse.on_click(mouse_assign, mouse_events)
    while time.time() - begin < tracktime:
            pass

    dfM = pd.DataFrame(mouseA)
    dfM.to_csv('mouseidentify.csv')
    print("Mouse Tracker Finished!")
    df = pd.DataFrame(pressed)
    df.to_csv('keyboardIdentify.csv')
    print("Keyboard Track Finished!")


