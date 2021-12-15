"""

Program to simulate brachiation control

"""
import matplotlib.pyplot as plt
import numpy as np

class BrachiatingRobot():
    def __init__(self):
        # [length, rotation] for each arm
        self.arm1 = [30,np.radians(0)]
        self.arm2 = [60,np.radians(60)]
        self.stack = []
        self.trajectory1 = []
        self.trajectory2 = []

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









