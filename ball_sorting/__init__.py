from gym.envs.registration import register

register(
    id='ball_sorting-v0',
    entry_point='ball_sorting.envs:BallSortingEnv',
)