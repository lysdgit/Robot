import numpy as np
import time
import roboticstoolbox as rtb

# 创建 Panda 机器人模型
# panda = Panda()
panda = rtb.models.Panda()
print(panda)

# 定义末端执行器的目标位姿
target_pose = np.array([[0.2875, 0.9188, 0.2703, 16.99],
                        [-0.4135, 0.3736, -0.8303, -38.45],
                        [-0.8639, 0.1269, 0.4873, -114.7],
                        [0, 0, 0, 1]])

# 设置模拟的时间步长和总时间
dt = 0.01
total_time = 5.0

# 计算轨迹中的时间步数
num_steps = int(total_time / dt)

# 生成末端执行器轨迹
trajectory = np.linspace(panda.fkine(panda.q), target_pose, num_steps)

# 模拟机器人执行轨迹
for pose in trajectory:
    q = panda.ikine(pose)
    panda.q = q
    panda.plot(block=False)
    time.sleep(dt)

panda.plot(block=True)  # 最后保持可视化窗口打开
