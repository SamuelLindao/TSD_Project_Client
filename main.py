import inputIdentify
import screen as sr
import random

sr.create_screen()

try:
    while True:
        inputIdentify.input_call(10)
        pass
except KeyboardInterrupt:
    print("Finished")
