import numpy as np
from scipy.optimize import minimize

# 从CSV文件中加载DH参数
dh_parameters = np.genfromtxt('dh_parameters.csv', delimiter=',', skip_header=1)

# 定义末端执行器的目标姿态
target_pose = np.array([[0.2875, 0.9188, 0.2703, 16.99],
                        [-0.4135, 0.3736, -0.8303, -38.45],
                        [-0.8639, 0.1269, 0.4873, -114.7],
                        [0, 0, 0, 1]])

# 正向运动学函数，计算末端位姿
def forward_kinematics(theta):
    transformation = np.eye(4)
    for i in range(len(theta)):
        a, alpha, d, theta_i = dh_parameters[i]
        t = np.array([[np.cos(theta_i), -np.sin(theta_i) * np.cos(alpha), np.sin(theta_i) * np.sin(alpha), a * np.cos(theta_i)],
                      [np.sin(theta_i), np.cos(theta_i) * np.cos(alpha), -np.cos(theta_i) * np.sin(alpha), a * np.sin(theta_i)],
                      [0, np.sin(alpha), np.cos(alpha), d],
                      [0, 0, 0, 1]])
        transformation = np.dot(transformation, t)
    return transformation

# 目标位姿的旋转矩阵和平移向量
target_rotation = target_pose[:3, :3]
target_translation = target_pose[:3, 3]

# 目标函数：计算当前关节角度下的末端位姿与目标位姿之间的差距
def objective_function(theta):
    current_pose = forward_kinematics(theta)
    error_rotation = np.dot(target_rotation, current_pose[:3, :3].T) - np.eye(3)
    error_translation = target_translation - current_pose[:3, 3]
    error = np.hstack((error_rotation.flatten(), error_translation))
    return np.sum(error**2)

# 逆解运动学函数，使用数值优化找到关节角度
def inverse_kinematics(target_rotation, target_translation):
    initial_guess = np.zeros(len(dh_parameters))
    
    result = minimize(objective_function, initial_guess, method='trust-constr')
    if result.success:
        theta = result.x
        return theta
    else:
        print("逆解运动学求解失败：", result.message)
        return None

# 调用逆解运动学函数并打印关节角度
joint_angles = inverse_kinematics(target_rotation, target_translation)
if joint_angles is not None:
    print("关节角度:", joint_angles)
