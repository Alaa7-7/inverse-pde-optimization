import numpy as np
from src.pde.solver import solve_pde
from src.inverse.optimizer import optimize

# grid setup
L = 1.0
Nx = 100
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

dt = 0.0005
Nt = 200

# true parameters
v_true = 0.8
D_true = 0.05

# generate observations
u_obs = solve_pde(v_true, D_true, x, dx, dt, Nt)

# add noise
u_obs += 0.01 * np.random.randn(len(u_obs))

# inverse estimation
v_est, D_est = optimize(u_obs, x, dx, dt, Nt)

print("True values:", v_true, D_true)
print("Estimated values:", v_est, D_est)