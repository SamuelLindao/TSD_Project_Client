import inputIdentify
import screen as sr
import threading
import platform

computer_name = platform.node()
print(computer_name)
thread = threading.Thread(target=sr.create_screen)
thread.start()

try:
    while True:
        if sr.WeNeedYou:
            inputIdentify.input_call(computer_name)
        else:
            pass
except KeyboardInterrupt:
    print("Finished")

thread.join()
