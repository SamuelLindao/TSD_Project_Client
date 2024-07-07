import keyboard, datetime, random, time, mouse
import pandas as pd
import screen as sr
import pygetwindow as gw



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
    'computer_name' : '',
    'hour': '',
    'mouseA': mouseA,
    'pressed': pressed,
    'active_app': ''
}

active_window = gw.getActiveWindow()


def input_call(computer_name, app):


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
    global active_window
    while time.time() - begin < 600:
        active_window = gw.getActiveWindow()
        if not app.WeNeedYou:
            break
        pass
    dfm = pd.DataFrame(mouseA)
    dfm.to_csv('mouse_identify.csv')
    print("Mouse Tracker Finished!")
    df = pd.DataFrame(pressed)
    df.to_csv('keyboard_identify.csv')
    print("Keyboard Track Finished!")

    track_info['id'] = str(random.randint(1,2141241244))
    track_info['hour'] = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    track_info['mouseA'] = mouseA
    track_info['computer_name'] = computer_name
    track_info['pressed'] = pressed
    if active_window is not None:
        track_info['active_app'] = active_window.title
    all_info = pd.DataFrame(track_info)
    all_info.to_csv('all_info')
    app.track_add(f"{len(pressed['key'])} - {len(mouseA['info'])}")
    print(track_info)



