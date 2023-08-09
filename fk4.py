import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH
from spatialmath import SE3

# 创建关节对象
joints = [
    RevoluteDH(290.0, 0.0, 1.5707963267948966, offset=-165.0),
    RevoluteDH(0.0, 270.0, 0.0, offset=-110.0),
    RevoluteDH(0.0, 70.0, 1.5707963267948966, offset=-110.0),
    RevoluteDH(302.0, 0.0, -1.5707963267948966, offset=-160.0),
    RevoluteDH(0.0, 0.0, 1.5707963267948966, offset=-120.0),
    RevoluteDH(72.0, 0.0, 0.0, offset=-400.0)
]

# 创建机器人对象
robot = DHRobot(joints)

# 定义末端执行器姿态
ee_pose = SE3(
    0.2875, 0.9188, 0.2703, 16.99,
   -0.4135, 0.3736, -0.8303, -38.45,
   -0.8639, 0.1269, 0.4873, -114.7,
   0, 0, 0, 1
)

# 计算逆运动学
joint_angles = robot.ikine(ee_pose)

# 检查关节角度是否存在
if joint_angles is None:
    print("无法到达给定的末端执行器姿态。")
else:
    print("关节角度：", joint_angles)
