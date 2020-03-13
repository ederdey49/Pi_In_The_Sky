from evdev import InputDevice, ecodes
import RPi.GPIO as GPIO

#fill with button ecodes once found
#triggers control height by adjusting vertical propeller thrust, d-pad controls rotational motor's thrust and direction
lTrig = 0
rTrig = 0
left = 0
right = 0
up = 0
down = 0

#motor/servo pins
motorA = 0
motorB = 0
motorC = 0
motorD = 0
motorE = 0
servo = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(motorA, GPIO.OUT)
GPIO.setup(motorB, GPIO.OUT)
GPIO.setup(motorC, GPIO.OUT)
GPIO.setup(motorD, GPIO.OUT)
GPIO.setup(motorE, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

def turnLeft():
  GPIO.output(servo, GPIO.HIGH) #may need to be fipped

def turnRight():
  GPIO.output(servo, GPIO.LOW)

def thrustUp():
  GPIO.output(motorE, GPIO.HIGH)

def thrustDown():
  GPIO.output(motorE, GPIO.LOW)

def moveUp():
  GPIO.output(motorA, GPIO.HIGH)
  GPIO.output(motorB, GPIO.HIGH)
  GPIO.output(motorC, GPIO.HIGH)
  GPIO.output(motorD, GPIO.HIGH)

def moveDown():
  GPIO.output(motorA, GPIO.LOW)
  GPIO.output(motorB, GPIO.LOW)
  GPIO.output(motorC, GPIO.LOW)
  GPIO.output(motorD, GPIO.LOW)

gamepad = InputDevice('/dev/input/eventX') #replace w/ actual address

for event in gamepad.read_loop():
  if event.type == ecodes.___: #gotta find this
    while event.value == 1:

      if event.code == up:
        thrustUp()
      elif event.code == down:
        thrustDown()
      elif event.code == left:
        turnLeft()
      elif event.code == right:
        turnRight()
      elif event.code == lTrig:
        moveUp()
      elif event.code == rTrig:
        moveDown()