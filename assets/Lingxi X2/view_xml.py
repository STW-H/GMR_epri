import mujoco
import mujoco_viewer
import os

# 切换到脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 加载模型
model = mujoco.MjModel.from_xml_path('scene.xml')
data = mujoco.MjData(model)

print(f"模型加载成功！")
print(f"身体数量：{model.nbody}")
print(f"几何体数量：{model.ngeom}")

# 关键步骤 1: 运行正向动力学，初始化机器人状态
mujoco.mj_forward(model, data)

# 创建查看器
viewer = mujoco_viewer.MujocoViewer(model, data)

print("成功加载模型！按 ESC 退出查看器")

# 关键步骤 2: 物理仿真 + 渲染循环
while viewer.is_alive:
    mujoco.mj_step(model, data)  # 物理仿真
    viewer.render()              # 渲染画面

viewer.close()