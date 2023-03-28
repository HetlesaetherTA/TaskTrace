import sys
from time import sleep
from threading import Event, Thread
class Animations:
    global condition
    condition = Event()

    def spinner(message):
        frames = ["|", "/", "-", "\u005c"]
        frame = 0
        while not condition.is_set():
            print("\r" + message + frames[frame % len(frames)], end="")
            sleep(0.15)
            frame = frame + 1
        sys.stdout.write('\033[2K\033[1G')

    def start(function, message):
        global t 
        t = Thread(target=function, args=(message,))
        t.start()
    def kill():
        condition.set()
        t.join()
