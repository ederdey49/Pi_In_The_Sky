## Pi in the Sky

### Planning

#### Objective

The goal for this project is to get a raspberry pi zero into the air, while recording acceleration data. Also, the pi should make a sound at the apex of its flight. 

#### Idea 

Our basic idea is to make a drone with controlled flight. We will use four DC motors with propellers to control height, like a standard drone, but we will control the drone's horizontal movement with a fifth motor and propeller. We will use a wireless gamepad to increase and decrease the drone's altitude, rotate the directional motor, and change the speed of the directional motor.

#### Schedule

| Week  | Plan |
| ------------- | ------------- |
| Nov. 25th  | Finish proposal, submit, order parts?? |
| Dec. 2nd | Start working on CAD design, begin code/pseudocode |
| Dec. 9th | Wireless controller work, CAD design |
| Jan. 6th | Keep working on wireless controller and CAD design |
| Jan. 13th | Work on code and CAD design |
| Jan. 20th | Code work, CAD design |
| Jan. 27th | Cut drone frame, work on code |
| Feb. 3rd | Work on code |
| Feb. 10th | Finish code, test |
| Feb. 17th | Test, troubleshooting |
| Feb. 24 | Troubleshooting |
| Mar. 2 | Scheduled sad boi hours |
| Mar. 9 | Finish |

#### Materials

5 DC motors:
https://www.amazon.com/gp/product/B00UYT8ONC/ref=ox_sc_act_title_2?smid=ATVPDKIKX0DER&psc=1

Propellers:
https://www.amazon.com/gp/product/B0768L5515/ref=ox_sc_act_title_1?smid=A2LLMFSH95HUFH&psc=1

Bluetooth controller:
https://www.amazon.com/Controller-Mutop-Wireless-Bluetooth-Joystick/dp/B07SWYQSP5/ref=sr_1_10?keywords=bluetooth+controller&qid=1574094324&sr=8-10

Plus a Bluetooth dongle (100 m range):
https://www.amazon.com/gp/product/B017XML51A/ref=ox_sc_act_title_1?smid=A1RTIMDUPCBOKN&psc=1

Laser-cutter acrylic

Total price: $42.43

#### Sketches/plans

We don't know why this is upside down- the actual photo isn't and if you click on it it's not upside down.

![Image](https://user-images.githubusercontent.com/54591964/69558690-a65ea700-0f76-11ea-8940-c00c1edf29f5.jpg)

### Project

#### Timeline
| Week | Plan |
| ------------- | ------------- |
| Nov. 25th  | Finished and submitted our project proposal |
| Dec. 2nd | Ordered our parts, began CAD, parts arrive Monday. Made a mistake when ordering parts, need to test motors and probably need to return them in favor of bigger/more powerful ones. |
| Dec. 9th | Worked on SolidWorks model. Parts and controller arrived. Found that, despite part specifications to the contrary, the propellers did not fit on the motors. Looked for new motors and propellers. |
| Jan. 6th | Redesigned SolidWorks model to fit the new motors while waiting for motors and propellers to arrive. |
| Jan. 13th | Continued work on SolidWorks model. Motors and propellers arrived, so we ran a test: see if they could simply lift their own weight when connected to a battery. Test failed, fingers bruised by very fast propellers. |
| Jan. 20th | Having already wasted a lot of money on our project, we decided to pivot to focusing on communication between the controller and the Raspberry Pi. We scoured the internet for information regarding Python Bluetooth libraries. |
| Jan. 27th | We discovered a library called PyBluez and, using internet tutorials, started writing simple programs to test Bluetooth connection between the controller and the Pi. So far, so good. |
| Feb. 3rd | We continued working on Bluetooth using PyBluez, but ran into a dead end on how to communicate button presses. We asked Max and Elijah, who are also using a Bluetooth controller for their project, for their advice. They suggested we use a library called evdev instead, which allows for direct access to input data for all devices connected to the Pi. We started looking for online tutorials to help us get set up. |
| Feb. 10th | For some reason, our Bluetooth controller is refusing to turn on. We tried changing the battery, but that did not help. THe controller must have been very poorly made and just broken for absolutely no reason after next to no use. |
| Feb. 17th | We ordered a new controller and began writing a program, with button input codes to be filled in when we identify the relevant evdev data. We also began looking for new motors and propellers, much larger and more powerful this time, but still very light (hopefully light enough). |
| Feb. 24 | Our new controller arrived, and, although it connects to the Pi over Bluetooth, no data whatsoever appears in evdev. We borrowed Max and Elijah's controller, and it works perfectly with evdev, so we guess the controller we bought just doesn't work with Raspberry Pi or Linux for some reason. |
| Mar. 2 | We placed our orders for new parts and made SolidWorks models for the new motors and propellers. |
| Mar. 9 | We continued working on SolidWorks and began looking for a new controller to use. We are hesitant to spend too much money on one, but we are afraid of another cheap one breaking for no reason. Governor Northam cancelled school for two weeks over the coronavirus, and it is looking unlikely that we will return to school at all this year. We fleshed out our program as much as possible without any evdev data, knowledge of how analog motor control works on a Raspberry Pi, or opportunities to test anything. |
| Mar. 23 | Governor Northam cancelled school for the rest of the year. Our parts arrived, I assume. |

#### Updated Materials

4 DC Motors:
https://www.amazon.com/dp/B07YDJSF17/ref=sspa_dk_detail_1?pd_rd_i=B07FN64599&pd_rd_w=BijKd&pf_rd_p=45a72588-80f7-4414-9851-786f6c16d42b&pd_rd_wg=Ji2Xr&pf_rd_r=TQ1R7YFPHH02DQNTDE96&pd_rd_r=d67ff6b3-7265-4099-8a1e-3eeb3e74a98a&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyOE9QT05JNFdWSjVIJmVuY3J5cHRlZElkPUEwODE1MDgzMTFIM1lXTVFPNTQxMyZlbmNyeXB0ZWRBZElkPUEwMjU4MTk2MU5JTVZNWUtNOU9WNiZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1

Propellers:
https://www.amazon.com/NIDICI-Propellers-1103-1106-Brushless-Quadcopter/dp/B07TB2WKDH/ref=sr_1_3?keywords=65mm%2Bdrone%2Bpropeller%2B1.5mm%2Bshaft&qid=1583511657&s=electronics&sr=1-3-catcorr&th=1

#### Everything Is Terrible
We had nothing but problems in working on this project. After our first order, indicated above in Planning/Materials, we realized that the shafts of our motors were too small for the propellers (even though the specifications indicated they should fit). We were also concerned that these motors, which we had chosen for their lightness, would be unable to produce enough thrust, so we bought new, larger motors and propellers. Additionally, after a couple months, our controller simply refused to turn on. We bought a new controller, which happened to just not be compatible with Raspberry Pi.

We tested our second motor-propeller combination, which was unable to produce thrust to lift itself, so we found new motors and propellers that were much more powerful than the originals but still very light. However, before the parts arrived to the Sigma Lab, school was cancelled due to the coronavirus pandemic, leaving our project—and our parts—in a state of permanent limbo.
We learned that buying things from Amazon is risky, because a lot of documentation from sellers is poor, and sometimes things are just badly made. We definitely learned the importance of reading user reviews.

The code we included should be taken with a massive grain of salt. It's the best we can do with the stage our project was left at, but it's only a rough outline with a lot of blanks that need to be filled in.
