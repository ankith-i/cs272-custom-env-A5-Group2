# import ray
# from ray import tune
# from ray.rllib.algorithms.ppo import PPO
# import balloon_flight_env
# from gym.envs.registration import register

# # Register the custom environment
# register(
#     id='BalloonFlight-v0',
#     entry_point='balloon_flight_env:BalloonFlightEnv'
# )

# def train_agent():
#     ray.init(ignore_reinit_error=True)

#     config = {
#         "env": "BalloonFlight-v0",  # Use the registered environment
#         "num_gpus": 0,
#         "num_workers": 1,
#         "framework": "tf",
#     }

#     stop_criteria = {
#         "training_iteration": 100,
#         "episode_reward_mean": 200,
#     }

#     results = tune.run(
#         PPO,
#         config=config,
#         stop=stop_criteria,
#         checkpoint_at_end=True
#     )

#     ray.shutdown()
#     return results

# if __name__ == "__main__":
#     train_results = train_agent()
#     print(train_results)

import ray
from ray import tune
from ray.rllib.algorithms.ppo import PPO
from ray.rllib.algorithms.dqn import DQN
from ray.rllib.algorithms.appo import APPO
import balloon_flight_env
# from gym.envs.registration import register

# Function to register the custom environment
# def register_environment():
#     print("Registering BalloonFlight-v0 environment")
#     register(
#         id='BalloonFlight-v0',
#         entry_point='balloon_flight_env:BalloonFlightEnv'
#     )
tune.register_env("BalloonFlight-v0", lambda config: balloon_flight_env.BalloonFlightEnv())

def train_agent():
    # Explicitly call the environment registration function
    # register_environment()

    ray.init(ignore_reinit_error=True)

    config = {
        "env": "BalloonFlight-v0",
        "num_gpus": 0,
        "num_workers": 1,
        "framework": "tf",
    }

    stop_criteria = {
        "training_iteration": 100,
        "episode_reward_mean": 200,
    }

    results = tune.run(
        DQN,
        config=config,
        stop=stop_criteria,
        checkpoint_at_end=True
    )

    ray.shutdown()
    return results

if __name__ == "__main__":
    train_results = train_agent()
    print(train_results)
