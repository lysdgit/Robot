#BRTIRSE1506A
#authored by Tom Gong  gongal@163.com
import numpy as np
import math
from numpy import *


d1 = 495.5
a2 = 680.0
a3 = 0
d4 = 680
d5 = 0
d6 = 284.5

def kinematics(thetas):
    rtheta=np.array(thetas)
    theta1=float(rtheta[0][0])
    theta2=float(rtheta[0][1])
    theta3=float(rtheta[0][2])
    theta4=float(rtheta[0][3])
    theta5=float(rtheta[0][4])
    theta6=float(rtheta[0][5])
   

    global d1
    global a2   
    global a3  
    global d4
    global d5
    global d6

    T1=matrix([[cos(theta1),0,-sin(theta1),0],
               [sin(theta1),0,cos(theta1),0],
               [0,-1,0,d1],
               [0,0,0,1]])
    T2=matrix([[cos(theta2),-sin(theta2),0,a2*cos(theta2)],
               [sin(theta2),cos(theta2),0,a2*sin(theta2)],
               [0,0,1,0],
               [0,0,0,1]])
    T3=matrix([[cos(theta3),0,sin(theta3),0],
               [sin(theta3),0,-cos(theta3),0],
               [0,1,0,0],
               [0,0,0,1]])
    T4=matrix([[cos(theta4),0,-sin(theta4),0],
               [sin(theta4),0,cos(theta4),0],
               [0,-1,0,d4],
               [0,0,0,1]])
    T5=matrix([[cos(theta5),0,sin(theta5),0],
               [sin(theta5),0,-cos(theta5),0],
               [0,1,0,0],
               [0,0,0,1]])
    T6=matrix([[cos(theta6),-sin(theta6),0,0],
               [sin(theta6),cos(theta6),0,0],
               [0,0,1,d6],
               [0,0,0,1]])

    t1_t6=T1*T2*T3*T4*T5*T6
   
    return t1_t6

thetas=matrix([0,0,0,0,0,0])
print (kinematics(thetas))