import gym
import numpy as np
import util
import random
import math
import matplotlib.pyplot as plt

env = gym.make('CliffWalking-v0')
q_values = util.Counter()
epsilon = 0.1
alpha = 0.5
discount = 1

def computeValueFromQValues(state):
    value = 0.0
    max_q_value = -10000

    for action in range(4):
        q_value = q_values[state, action]
        if q_value > max_q_value:
            max_q_value = q_value
            value = q_value

    return value

def computeActionFromQValues(state):
    best_action = None
    max_q_value = -10000
    for action in range(4):
        q_value = q_values[state, action]
        if q_value > max_q_value:
            max_q_value = q_value
            best_action = action

    return best_action

def getAction(state):
    action = None
    if (util.flipCoin(epsilon)):
        action = random.choice(range(4))
    else:
        action = computeActionFromQValues(state)

    return action

def update(state, action, nextState, reward):
    q_values[state, action] = q_values[state, action] + alpha * (reward + discount * computeValueFromQValues(nextState) - q_values[state, action])

def getPolicy(state):
    return computeActionFromQValues(state)

def getValue(state):
    return computeValueFromQValues(state)

def eval_agent():
    state, _ = env.reset()
    terminated = False
    i_step = 0
    ep_reward = 0
    while not terminated:
        action = computeActionFromQValues(state)
        nextState, reward, terminated, truncated, _ = env.step(action)
        terminated |= truncated
        i_step += 1
        ep_reward += reward
        if i_step > 100:
            break
        state = nextState
    return ep_reward

n_episodes = 50

# Train the agent
rewards = []
for i_episode in range(n_episodes):
    terminated = False
    i_step = 0
    state, _ = env.reset()
    while not terminated:
        action = getAction(state)
        nextState, reward, terminated, truncated, _ = env.step(action)
        terminated |= truncated
        i_step += 1
        if i_step > 200:
            break
        update(state, action, nextState, reward)
        state = nextState
    ep_reward = eval_agent()
    rewards.append(ep_reward)
    # print("ep_reward: ", ep_reward)
    '''
    if ep_reward == -13:
        break
    '''
print(i_episode)
plt.plot(rewards) 
plt.xlabel("Episodio")  
plt.ylabel("Reward")  
plt.title("Reward x Episodio")  
plt.show() 

# Evaluate the agent
state, _ = env.reset()
terminated = False
i_step = 0
actions_dict = {
    0: 'Move up',
    1: 'Move right',
    2: 'Move down',
    3: 'Move left'
}

while not terminated:
    action = computeActionFromQValues(state)
    nextState, reward, terminated, truncated, _ = env.step(action)
    terminated |= truncated
    i_step += 1
    if i_step > 200:
        break
    state_row = math.floor(state / 12)
    state_column = state % 12
    print('State_Row: ', state_row, ' State_Column: ', state_column, ' Action: ', actions_dict[action])
    state = nextState
