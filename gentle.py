import pyfirmata
import subprocess
import time
from MD25 import MD25
from Pin import Pin

# drive controller
controller = MD25(0x58,1,True)

# arduino i/o
PORT  = '/dev/ttyACM0'
board = pyfirmata.Arduino(PORT)
pan   = Pin(board, 5)
tilt  = Pin(board, 3)
led   = Pin(board, 6)

subprocess.Popen(["mpg123", "startup.mp3"])
led.transition(0.0,1.0,2)
tilt.transition(.9, .4, 2)

controller.turn(22, -10)
time.sleep(1.0)
controller.turn(10, 20)
time.sleep(0.4)
controller.stop()

subprocess.Popen(["espeak", '"Hello. I am BayBot. I am the first developer friendly robot. I will soon be in homes, everywhere."'])
pan.transition(.7, .9, 1.0)
pan.transition(.9, .1, 3.0)
pan.transition(.1, .7, .5)
time.sleep(4)

controller.turn(-10,-20)
time.sleep(0.4)
controller.turn(-22, 10)
time.sleep(1.0)
controller.stop()

tilt.transition(.4, .9, 1)
led.transition(1.0, 0.0, 3)


board.exit()

