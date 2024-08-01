# Balloon Flight: A Reinforcement Learning Module for Altitude Control Simulation - Group 2

## Project Summary

<!-- Around 200 Words -->
<!-- Cover (1) What problem you are solving, (2) Who will use this RL module and be happy with the learning, and (3) a brief description of the results -->

Balloon Flight is an innovative Reinforcement Learning (RL) module designed to simulate the challenge of controlling a balloon's altitude. The primary problem it addresses is navigating a balloon to a target altitude, considering various factors like wind effects and balloon heating or cooling mechanisms. This module is particularly useful for RL enthusiasts, researchers, and developers in the field of autonomous flight control systems. It offers a unique opportunity for users to explore and experiment with different RL algorithms in a dynamic and unpredictable environment. By providing a realistic simulation of balloon flight, this module helps in understanding the complexities of real-world flight control and decision-making processes. The results from this project demonstrate effective learning and adaptation strategies employed by the RL agents to achieve the goal of maintaining the balloon at the desired altitude under varying conditions.

## State Space

<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

The state space of the Balloon Flight environment consists of a single dimension representing the current altitude of the balloon. This altitude value ranges from 0 to a maximum of 1500 units, corresponding to the balloon's height above the ground.

## Action Space

<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

The action space in this environment is discrete, comprising three possible actions:

Heat Up: Increases the balloon's altitude.
Neutral: No change in the balloon's altitude.
Cool Down: Decreases the balloon's altitude.

## Rewards

<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

The reward system in Balloon Flight is designed to guide the agent towards the target altitude. The reward at each step is calculated as the negative absolute difference between the current altitude and the target altitude of 1000 units. Therefore, the closer the balloon is to the target altitude, the higher the reward.

## RL Algorithm

The RL algorithms used in this project include Proximal Policy Optimization (PPO), Deep Q-Network (DQN), and Asynchronous Proximal Policy Optimization (APPO) from the Ray RLlib library. These algorithms were chosen for their effectiveness in handling discrete action spaces and their ability to learn complex policies.

## Starting State [if applicable]

<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

The starting state of each episode is randomly initialized with the balloon's altitude ranging between 0 and 500 units. This randomization introduces variability and challenges the RL agent to adapt to different starting conditions.

## Episode End [if applicable]

<!-- See the Cart Pole Env example https://gymnasium.farama.org/environments/classic_control/cart_pole/ -->

An episode ends when the balloon reaches the target altitude of 1000 units. The environment also includes a random wind effect, which adds an element of unpredictability to the altitude control challenge.

## Results
The episodic returns of PPO algorithm are as follows - 

<img src="/results/ppo_run.png" width="1000">

The episodic returns of DQN algorithm are as follows - 

<img src="/results/dqn_run.png" width="1000">

The episodic returns of APPO algorithm are as follows - 

<div>
  <img src="/results/appo_max.png" alt="APPO Max Results" width="500" />
  <img src="/results/APPO.png" alt="APPO Results" width="500" />
</div>

## Conclusion

* The results show that the APPO's mean episodic return shows significant volatility, with some peaks that surpass the mean rewards of the PPO algorithm. This suggests that while APPO can achieve high rewards, it may not be as stable or consistent as PPO.
* PPO appears to be the most consistent and stable in terms of learning performance, followed by APPO which shows higher variance in its learning performance.
* DQN does not seem to be performing well in this particular task, as indicated by the lack of an improving trend.
