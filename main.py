# programming by Ned Derdeyn
from evdev import InputDevice, ecodes
import RPi.GPIO as GPIO

# fill with button ecodes once found
# triggers control height by adjusting vertical propeller thrust, d-pad controls rotational motor's thrust and direction
lTrig = 0
rTrig = 0
left = 0
right = 0
up = 0
down = 0

# motor/servo pins
motorA = 0
motorB = 0
motorC = 0
motorD = 0
motorE = 0
servo = 0

# we didn't have time to actually work with our motors so who knows if this would've worked
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorA, GPIO.OUT)
GPIO.setup(motorB, GPIO.OUT)
GPIO.setup(motorC, GPIO.OUT)
GPIO.setup(motorD, GPIO.OUT)
GPIO.setup(motorE, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

# we need to somehow do analog controls on our Raspberry Pi, which we didn't get the chance to learn how to do
def turnCCW():
  # make the servo the directional motor is attached to turn in the counterclockwise direction

def turnCW():
  # same but clockwise

def thrustUp():
  # increase thrust on directional motor

def thrustDown():
  # decrease it

def moveUp():
  # increase thrust on the four up/down motors

def moveDown():
  # decrease it

gamepad = InputDevice('/dev/input/eventX') # replace w/ actual address

for event in gamepad.read_loop():
  if event.type == ecodes.___: # gotta find this
    while event.value == 1:

      if event.code == up:
        thrustUp()
      elif event.code == down:
        thrustDown()
      elif event.code == left:
        turnCCW()
      elif event.code == right:
        turnCW()
      elif event.code == lTrig:
        moveUp()
      elif event.code == rTrig:
        moveDown()
