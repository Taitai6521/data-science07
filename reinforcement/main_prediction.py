import gym
from prediction import Agent

if __name__ == '__main__':
    env = gym.make('BlackJack-v0')
    agent = Agent()
    n_episodes = 50000
    for i in range(n_pisodes):
        if i % 5000:
            print('starting episode', i)
        observation = env.reset()
        done = False
        while not done:
            acionn = agent.policy(observatio)
            observation_, reward, done, info=env.step(action)
            agent.memory.append((observation, reward))

            observation = observation
        agent.update_V()
    print(agent.V[(21,3,True)])
    print(agent.V[(4, 1,False)])