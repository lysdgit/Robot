from roboticstoolbox import RevoluteDH, DHRobot
import spatialmath as sm
import numpy as np
import matplotlib.pyplot as plt

# 定义机器人的DH参数
dh_params = [
    RevoluteDH(290.0,0.0,1.5707963267948966,-165.0),
    RevoluteDH(0.0,270.0,0.0,-110.0),
    RevoluteDH(0.0,70.0,1.5707963267948966,-110.0),
    RevoluteDH(302.0,0.0,-1.5707963267948966,-160.0),
    RevoluteDH(0.0,0.0,1.5707963267948966,-120.0),
    RevoluteDH(72.0,0.0,0.0,-400.0,)
]

# 创建机器人对象
robot = DHRobot(dh_params)

# 设置初始关节角度和终止关节角度
joint_angles_start = np.deg2rad([0, 0, 0, 0, 0, 0])  # 初始关节角度
joint_angles_end = np.deg2rad([45, 90, -45, -45, -85, 90])  # 终止关节角度

# 设置时间步长和插值数量
time_steps = 100  # 时间步长
num_interp = time_steps + 1

# 计算关节角度的插值
joint_angles_interp = np.linspace(joint_angles_start, joint_angles_end, num=num_interp)

# 计算末端执行器的位姿
positions = np.zeros((num_interp, 3))
orientations = np.zeros((num_interp, 3, 3))

for i in range(num_interp):
    robot.q = joint_angles_interp[i]
    pose = robot.fkine(joint_angles_interp[i])  # 将插值的关节角度作为参数传递给fkine函数
    positions[i] = pose.t
    orientations[i] = pose.R

# 绘制运动轨迹
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Robot End Effector Trajectory')

plt.show()
