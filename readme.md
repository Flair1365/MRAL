本次作业采用DDPG模型，使用演员-评论家（Actor-Critic）算法作为其基本框架，并使用双重神经网络架构，对于策略函数和价值函数均使用双重神经网络模型架构。具体可见https://blog.csdn.net/dgvv4/article/details/129479878

# 训练模型
`python rl_trainer/main.py`

运行上述代码对模型网络进行训练。

可以修改rl_trainer/main.py最后几行的所有参数，例如parser.add_argument('--max_episodes', default=10, type=int)语句代表训练的最大轮数，可以修改default=10为更大的数，使得模型更加收敛。

## 建议修改的参数（笨人能看懂的参数）：
max_episodes：最大训练轮数
episode_length：从第几轮开始输出奖励等相关信息
a_lr：actor的学习率
c_lr：评论家的学习率
save_interval：几轮保存一次.pth网络

训练好的网络将保存在`rl_trainer/models/snake_3v3`中，每个run文件夹对应训练的顺序，run文件夹内的trained_model文件夹内保存着具体的训练网络，例如actor_5.pth,critic_5.pth，选择一个作为最终训练好的网路复制粘贴到`submissions`中，并修改blue.py中的对应参数（文末有说），即可运行测试该网络模型

## 修改main.py中的如下参数实现对已存在网络的继续训练：
load_model：当默认值为True时加载已有网络进行训练
load_model_run：选择哪个文件夹的网络进行训练，例如load_model_run为4，则在run4文件夹内选择网络
load_model_run_episode：选择文件夹内训练了多少轮的网络进行再训练，例如load_model_run_episode=5，则actor和critic会分别选择actor_5.pth,critic_5.pth进行训练

# 提交
`python example.py`
在submissions文件夹中复制粘贴训练好的网络（例如actor_10.pth），并修改blue.py中actor_net对应的文件名称（例如actor_net = os.path.dirname(os.path.abspath(__file__)) + "/actor_10.pth"），执行上述指令即可操纵训练好的模型，作为蓝色方开始游戏。
example.py最后的输出是获胜的agent序号（蓝色方序号是2，3，4），此时红色方是随机算法，序号是5，6，7