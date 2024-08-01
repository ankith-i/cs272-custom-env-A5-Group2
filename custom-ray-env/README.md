# Installation
- ray rllib
  - [Instruction](https://docs.ray.io/en/latest/ray-overview/installation.html)
  - pip example ```pip install -U "ray[rllib]"```
- tensorflow2
  - [Instruction](https://www.tensorflow.org/install?hl=en)

# ray rllib Configurations
- [Key concepts](https://docs.ray.io/en/latest/rllib/key-concepts.html)
- [Configuration options](https://docs.ray.io/en/latest/rllib/rllib-training.html#configuring-rllib-algorithms)
  - training options
  - environment options
  - deep learning framework options
  - rollout worker options
  - evaluation options
  - exploration options
  - options for training with offline data
  - options for training multiple agents
  - debugging options
  - options for experimental features


# ray rllib Environment Configuration
- [```register_env``` function](https://docs.ray.io/en/latest/rllib/rllib-env.html)

# ray rllib Results
- All the training results are stored under the respective algorithm folders

# Visualization via tensorboard
```tensorboard --logdir=~/APPO_2023-12-11_01-46-42``` for checking APPO algorithm results

```tensorboard --logdir=~/PPO_2023-12-11_00-15-54``` for checking PPO algorithm results

```tensorboard --logdir=~/DQN_2023-12-11_10-47-39``` for checking DQN algorithm results


# Custom Env Reference
- [Farama gymnasium](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/)
