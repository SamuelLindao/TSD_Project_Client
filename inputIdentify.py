import keyboard, datetime, random, time, mouse
import pandas as pd
import screen as sr

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

track_info = {
    'id': '',
    'hour': '',
    'mouseA': mouseA,
    'pressed': pressed,
}


def input_call():

    def key_assign(event):
        recorded_events.append(event)
        pressed['id'].append(str(random.randint(1, 13235235)))
        pressed['hour'].append(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        pressed['key'].append(str(event.name))

    def mouse_assign():
        mouseA['id'].append(str(random.randint(1, 13235235)))
        mouseA['hour'].append(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        mouseA['info'].append(str(mouse.get_position()))

    begin = time.time()
    keyboard.on_press(key_assign)
    mouse.on_click(mouse_assign, mouse_events)
    while time.time() - begin < 600:
        print(time.time() - begin)
        if not sr.WeNeedYou:
            break
        pass
    dfM = pd.DataFrame(mouseA)
    dfM.to_csv('mouseidentify.csv')
    print("Mouse Tracker Finished!")
    df = pd.DataFrame(pressed)
    df.to_csv('keyboardIdentify.csv')
    print("Keyboard Track Finished!")
    track_info['id'] = str(random.randint(1,2141241244))
    track_info['hour'] = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    track_info['mouseA'] = mouseA
    track_info['pressed'] = pressed
    print(track_info)



