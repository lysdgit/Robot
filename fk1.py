import numpy as np

# DH参数（以弧度为单位）
dh_params = [
    [0, 0, 495.5, np.deg2rad(55)],
    [-np.pi/2, 680.0, 0, np.deg2rad(55)],
    [0, 0, 680, np.deg2rad(55)],
    [-np.pi/2, 0, 0, np.deg2rad(55)],
    [np.pi/2, 0, 284.5, np.deg2rad(55)],
    [-np.pi/2, 0, 0, np.deg2rad(55)]
]

# 设置关节角度（均为55度）
joint_angles = np.deg2rad([55, 55, 55, 55, 55, 55])

# 进行正向运动学计算
position = np.zeros(3)  # 末端执行器的位置
orientation = np.eye(3)  # 末端执行器的姿态

for i in range(len(dh_params)):
    alpha, a, d, theta = dh_params[i]
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    cos_alpha = np.cos(alpha)
    sin_alpha = np.sin(alpha)

    # 计算变换矩阵
    T = np.array([
        [cos_theta, -sin_theta*cos_alpha, sin_theta*sin_alpha, a*cos_theta],
        [sin_theta, cos_theta*cos_alpha, -cos_theta*sin_alpha, a*sin_theta],
        [0, sin_alpha, cos_alpha, d],
        [0, 0, 0, 1]
    ])

    # 更新位置和姿态
    position = T[:3, 3]
    orientation = orientation @ T[:3, :3]

print("末端执行器位置：", position)
print("末端执行器姿态：", orientation)
