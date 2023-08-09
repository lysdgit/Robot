from roboticstoolbox import DHRobot, RevoluteDH
import numpy as np
import roboticstoolbox as rtb

# 从CSV文件中加载DH参数
dh_params = np.genfromtxt('dh_parameters.csv', delimiter=',', skip_header=1)

# 创建RevoluteDH对象来表示每个链接的DH参数
links = []
for params in dh_params:
    a, alpha, d, theta, min_theta, max_theta = params
    link = RevoluteDH(d=d, a=a, alpha=alpha, offset=theta, qlim=[min_theta, max_theta])
    links.append(link)

# 创建机器人模型
robot = DHRobot(links)
print(robot)

# 创建示例关节角度
qz = np.array([90, 0, 0, 0, 0, 0])  # 这里使用零位置关节角度，根据您的需求进行更改

# 计算末端执行器的姿态
end_effector_pose = robot.fkine(qz)
print("末端执行器的姿态：")
print(end_effector_pose)
