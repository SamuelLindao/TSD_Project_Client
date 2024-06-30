import inputIdentify
import screen as sr
import threading

thread = threading.Thread(target=sr.create_screen)
thread.start()

try:
    while True:
        if sr.WeNeedYou:
            inputIdentify.input_call()
        else:
            pass
except KeyboardInterrupt:
    print("Finished")

thread.join()
