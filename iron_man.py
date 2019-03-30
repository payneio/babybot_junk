import pyfirmata
import subprocess
import time
from MD25 import MD25
from Pin import Pin

# drive controller
controller = MD25(0x58,1,True)

# arduino i/o
PORT = '/dev/ttyACM0'
board = pyfirmata.Arduino(PORT)
pan = Pin(board, 5)
tilt = Pin(board, 3)
led = Pin(board, 6)

controller.turn(22,-20)
time.sleep(1.0)
controller.stop()

led.transition(0.0,1.0,3)
subprocess.Popen(["mpg123", "demo.mp3"])
tilt.transition(.9, .4, 3)
pan.transition(.7, .9, .5)
pan.transition(.9, .1, 1.0)
pan.transition(.9, .7, .5)
time.sleep(8)
tilt.transition(.4, .9, 1)
led.transition(1.0, 0.0, 3)

board.exit()

