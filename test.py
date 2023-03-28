from utility import Animations
from time import sleep
Animations.start(Animations.spinner, "test")
sleep(1)
Animations.kill()
print("asdf")
sleep(1)
Animations.start(Animations.spinner, "test2")
sleep(1)
Animations.kill()
sleep(2)
