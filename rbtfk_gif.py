import numpy as np
from spatialmath import SE3

def kinematics(thetas):
    d1 = 495.5
    a2 = 680.0
    a3 = 0
    d4 = 680
    d5 = 0
    d6 = 284.5

    theta1 = float(thetas[0])
    theta2 = float(thetas[1])
    theta3 = float(thetas[2])
    theta4 = float(thetas[3])
    theta5 = float(thetas[4])
    theta6 = float(thetas[5])

    T1 = SE3.Rz(theta1) * SE3(0, 0, -d1)
    T2 = SE3.Rx(-np.pi/2) * SE3.Rz(theta2) * SE3(a2, 0, 0)
    T3 = SE3.Rx(np.pi/2) * SE3.Rz(theta3)
    T4 = SE3.Rz(theta4) * SE3(0, 0, -d4)
    T5 = SE3.Rx(np.pi/2) * SE3.Rz(theta5)
    T6 = SE3.Rz(theta6) * SE3(0, 0, d6)

    t1_t6 = T1 * T2 * T3 * T4 * T5 * T6
   
    return t1_t6

thetas = [0, 0, 0, 0, 0, 0]
print(kinematics(thetas))
