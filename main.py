import inputIdentify
import screen as sr
import threading

thread = threading.Thread(target=sr.create_screen)
thread.start()

try:
    while True:
        if sr.WeNeedYou:
            inputIdentify.input_call(10)
        else:
            pass
except KeyboardInterrupt:
    print("Finished")

thread.join()
