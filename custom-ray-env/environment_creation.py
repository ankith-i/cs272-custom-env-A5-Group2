import gymnasium as gym
from gymnasium import spaces
import numpy as np

class BalloonFlightEnv(gym.Env):
    def __init__(self):
        super(BalloonFlightEnv, self).__init__()
        self.target_altitude = 1000  # Target altitude to reach
        self.max_altitude = 1500     # Maximum possible altitude
        self.action_space = spaces.Discrete(3)  # Heat Up, Neutral, Cool Down
        self.observation_space = spaces.Box(low=0, high=self.max_altitude, shape=(1,), dtype=np.int64)

    def reset(self,*,seed=None,options=None):
        self.current_altitude = np.random.randint(0, 500)  # Start at a random altitude
        return np.array([self.current_altitude]),{}

    def step(self, action):
        wind_effect = np.random.randint(-50, 51)  # Random wind effect
        if action == 0:   # Heat Up
            self.current_altitude += 100
        elif action == 2: # Cool Down
            self.current_altitude -= 100

        self.current_altitude += wind_effect
        self.current_altitude = np.clip(self.current_altitude, 0, self.max_altitude)

        # Calculate reward
        reward = -abs(self.target_altitude - self.current_altitude)
        done = self.current_altitude == self.target_altitude

        return np.array([self.current_altitude]), reward, done,done, {}

    def render(self, *,seed=None, options=None):
        print(f"Current Altitude: {self.current_altitude}")

    def close(self):
        pass

if __name__ == "__main__":
    env = BalloonFlightEnv()
    obs = env.reset()
    for _ in range(100):
        action = env.action_space.sample()
        obs, reward, done,term, info = env.step(action)
        env.render()
        if done:
            break
    env.close()
