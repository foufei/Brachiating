"""

Program to simulate brachiation control

"""
import matplotlib.pyplot as plt
import numpy as np
from pynput import Key, Listener
# import keyboard

from dc_motor_controller import DCMotorController
from ultrasonic_sensor import *

THRESHOLD = 10


class BrachiatingRobot():
    def __init__(self):
        # [length, rotation] for each arm
        self.arm1 = [30,np.radians(0)]
        self.arm2 = [60,np.radians(60)]
        self.stack = []
        self.trajectory1 = []
        self.trajectory2 = []
    
    def detect(self):
        detect = False
        distance = get_distance()
        while not detect:
            # revolutes
            new_distance = get_distance()
            delta_distance = distance - new_distance
            if delta_distance > THRESHOLD:
                detect = True

    def circulate(self):
        l1 = self.arm1[0]
        r2 = self.arm2[1]
        l2 = self.arm2[0]
        
        gap = l2*np.sin(r2)
        r = gap/2
        area = r*l1
        sample_circle = self.getVerticesOfCircle(x=r,r=r, srcAng=-2*r2, destAng=-2*np.arctan(r/l1),area=area,h=l1)
        for pt in sample_circle:
            self.stack.append(pt)
            plt.scatter(pt[0],pt[1])
     
        mid = self.stack.pop()
        offset = mid[0]
        while len(self.stack)!=0:
            pt = self.stack.pop()
            plt.scatter(2*offset-pt[0],pt[1])
        
        plt.show()

    def getVerticesOfCircle(self,area,h,r,x=0,y=0,srcAng=0,destAng=2*np.pi):
        #The lower this value the higher quality the circle is with more points generated
        stepSize = 0.01
        #Generated vertices
        positions = []

        while srcAng < destAng:
            positions.append((r*np.cos(srcAng)+x, r*np.sin(srcAng)+y))
            srcAng += stepSize
            self.update_trajectory(srcAng,area,h,r)

        return positions

    def update_trajectory(self,central_angle,area,h,r):
        self.l2 = 2*area/h
        self.r2 = central_angle/2
        self.trajectory2.append([self.l2, self.r2])

        self.l1 = 2*r*np.cos(np.arcsin(self.l2/2*r))
        self.r1 = np.arcsin(h/self.l1)
        self.trajectory1.append([self.l1, self.r1])

        return self.l1,self.r1,self.l2,self.r2

robot = BrachiatingRobot()
robot.circulate()

revolute_controller_1 = DCMotorController(21,20,16)
revolute_controller_2 = DCMotorController(7,25,8)

prismatic_controller_1 = DCMotorController(21,20,16)
prismatic_controller_2 = DCMotorController(21,20,16)

controller = revolute_controller_1

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))

        if key.char == "j":
            print("You chose the left revolute controller")
            controller = revolute_controller_1
            
        if key.char == "l":
            print("You chose the right revolute controller")
            controller = revolute_controller_2

        if key.char == "u":
            print("You chose the left prismatic controller")
            controller = prismatic_controller_1

        if key.char == "o":
            print("You chose the right prismatic controller")
            controller = prismatic_controller_2

        if key.char == "i":
            print("Forward")  
            controller.forward(10)

        if key.char == "k":
            print("Backward")  
            controller.backward(10)        

    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    print('Key released: {0}'.format(key))
    controller.stop()
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()












