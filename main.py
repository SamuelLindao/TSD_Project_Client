import inputIdentify
import screen as sr
import threading
import platform
import datetime
import time

app_instance, app_root = sr.create_app()

computer_name = platform.node()
print(computer_name)


def external_worker():
    while True:
        if app_instance.WeNeedYou:
            inputIdentify.input_call(computer_name, app_instance)
        else:
            time.sleep(0.5)


thread = threading.Thread(target=external_worker)
thread.start()

app_root.mainloop()

thread.join()