import math

class Pin:
  def __init__(self, board, pin_no):
    self.pin = board.get_pin("d:"+str(pin_no)+":p")
    self.board = board
    
  def transition(self, a, b, secs):
    steps = math.fabs((b - a) * 100.0)
    wait_time = secs/float(steps)
    increment = (b-a) / 100.0
    position = a
    epsilon = .05
    while math.fabs(b-position) > epsilon :
      position = position + increment
      # Note: Value range for PWM is 0.0 till 1.0
      if position < 0.0 and position > 1.0:
        break
      self.pin.write(position)
      # print(position)
      self.board.pass_time(wait_time)
    self.pin.write(b)
    # print("###################")

  def set(self, a):
    self.pin.write(a)
    self.board.pass_time(.5)
