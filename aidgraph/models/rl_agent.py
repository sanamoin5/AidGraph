"""Reinforcement Learning agent placeholder."""

from stable_baselines3 import PPO


class DeploymentAgent:
    """Wrapper around a PPO agent for resource deployment."""

    def __init__(self, env):
        self.model = PPO('MlpPolicy', env)

    def train(self, timesteps: int = 10000):
        """Train the agent."""
        self.model.learn(total_timesteps=timesteps)

    def predict(self, observation):
        """Return an action given an observation."""
        return self.model.predict(observation)
