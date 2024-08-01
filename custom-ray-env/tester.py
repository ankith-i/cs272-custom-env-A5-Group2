import gym
import balloon_flight_env
from gym.envs.registration import register
register(
    id='BalloonFlight-v0',
    entry_point='balloon_flight_env:BalloonFlightEnv'
)
def test_env():
    env = gym.make('BalloonFlight-v0')
    env.reset()
    for _ in range(100):
        action = env.action_space.sample()
        obs, reward, done,term, _ = env.step(action)
        if done:
            print("Goal reached!")
            break

if __name__ == '__main__':
    test_env()
