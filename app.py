from maze_env import Maze
from RL_agent import QLearningTable
import matplotlib.pylab as plt

episode_count = 50
episodes = range(episode_count)
rewards = []
movements = []

def run_experiment():
    for episode in episodes:
        print("Episdoe {0}/{1}".format(episode, episode_count))
        observation = env.reset()
        moves = 0

        while True:
            env.render()
            action = q_learning_agent.choose_action(str(observation))
            observation_, reward, done = env.get_state_reward(action)
            moves +=1
            q_learning_agent.learn(str(observation), action, reward, str(observation_))
            observation = observation_

            if done:
                movements.append(moves)
                rewards.append(reward)
                print("Reward: {0}, Moves: {1}".format(reward, moves))
                break
    print("game over !")
    plot_reward_movements()


def plot_reward_movements():
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(episodes,movements)
    plt.xlabel("Episodes")
    plt.ylabel("Number of Movements")

    plt.subplot(2,1,2)
    plt.step(episodes,rewards)
    plt.xlabel("Episodes")
    plt.ylabel("Reward")

    plt.show()

if __name__=="__main__":
    env = Maze()
    q_learning_agent = QLearningTable(actions=list(range(env.n_action)))
    env.window.after(10, run_experiment)
    env.window.mainloop()
