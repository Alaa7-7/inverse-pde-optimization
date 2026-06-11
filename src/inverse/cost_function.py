import numpy as np
from src.pde.solver import solve_pde

def loss(v, D, x, dx, dt, Nt, u_obs):
    u_sim = solve_pde(v, D, x, dx, dt, Nt)
    return np.linalg.norm(u_sim - u_obs)