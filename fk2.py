from roboticstoolbox import DHRobot, RevoluteDH
import numpy as np

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

# 定义末端执行器的目标姿态
target_pose = np.array([[0.2875, 0.9188, 0.2703, 16.99],
                        [-0.4135, 0.3736, -0.8303, -38.45],
                        [-0.8639, 0.1269, 0.4873, -114.7],
                        [0, 0, 0, 1]])

# 计算逆运动学，求解关节角度
q_solutions = robot.ikine_LMS(target_pose)

# 打印关节角度解
print("关节角度解：")
print(q_solutions)
