from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/eventX') #replace w/ actual address

#replace w/ actual ecodes
lTrig = 0
rTrig = 0
up = 0
down = 0
left = 0
right = 0

def testController(gamepad):
  print(gamepad)

  for event in gamepad.read_loop():
    print(categorize(event))

def findEcodes(gamepad):
  print(gamepad)

  for event in gamepad.read_loop():
    if event.type == ecodes.___: #replace w/ event code (ecode) type
      print(categorize(event))

def testEcodes(gamepad):
  for event in gamepad.read_loop():
    if event.type == ecodes.___: #gotta find this
      while event.value == 1:

        if event.code == up:
          print("up")
        elif event.code == down:
          print("down")
        elif event.code == left:
          print("left")
        elif event.code == right:
          print("right")
        elif event.code == lTrig:
          print("left trigger")
        elif event.code == rTrig:
          print("right trigger")

#use these alternately to find relevant data
testController(gamepad) #view all data
findEcodes(gamepad) #filter relevant data to more easily find ecodes