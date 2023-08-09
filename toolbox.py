from roboticstoolbox.robot.ERobot import ERobot
import numpy as np
import matplotlib.pyplot as plt

# 创建机器人模型
L1 = ERobot('Z', 495.5)
L2 = ERobot('X', 680.0)
L3 = ERobot('X', 0)
L4 = ERobot('Z', 680)
L5 = ERobot('X', 0)
L6 = ERobot('Z', 284.5)

robot = ERobot([L1, L2, L3, L4, L5, L6])

# 设置关节角度
thetas = np.array([0, 0, 0, 0, 0, 0])

# 计算机器人运动
T = robot.fkine(thetas)

# 绘制机器人模型
fig, ax = robot.plot(T)

# 显示图形
plt.show()

