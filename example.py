import numpy as np
import pdb
from env.snakes import SnakeEatBeans
from submissions.red import policy as red_policy
from submissions.blue import policy as blue_policy
from env.chooseenv import make

env = SnakeEatBeans()
# env = make('snakes_3v3',conf=None)

obs = env.reset(render=True)
# print(obs[0])


action_dim = env.get_action_dim()
num_player = len(env.players)



while not env.is_terminal():
    
    action_red = red_policy(obs[:3])
    # print(obs[:3])
    # action_blue_1 = blue_policy(obs[0])
    # action_blue_2 = blue_policy(obs[1])
    # action_blue_3 = blue_policy(obs[2])
    action_blue = red_policy(obs[3:])

    # all_actions = action_red + [action_blue_1] + [action_blue_2] + [action_blue_3]
    all_actions = action_red + action_blue
    # print(all_actions)

    next_obs, reward, terminal, info = env.step(all_actions)

    
    
print(env.check_win())

