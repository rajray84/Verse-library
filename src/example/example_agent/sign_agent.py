from src.scene_verifier.agents.base_agent import BaseAgent
import numpy as np

class SignAgent(BaseAgent):
    def __init__(self, id, code = None, file_name = None):
        super().__init__(id, code, file_name)

    def TC_simulate(self, mode, init, time_horizon, map=None):
        time_step = 0.01
        number_points = int(np.ceil(float(time_horizon)/time_step))
        t = [i*time_step for i in range(0,number_points)]
        trace = [[0] + init] + [[i + time_step] + init for i in t]
        return trace
