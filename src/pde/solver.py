import numpy as np

def solve_pde(v, D, x, dx, dt, Nt):
    Nx = len(x)

    # initial condition (Gaussian)
    u = np.exp(-100 * (x - 0.3)**2)

    for _ in range(Nt):
        u_new = u.copy()

        for i in range(1, Nx - 1):
            advection = -v * (u[i] - u[i-1]) / dx
            diffusion = D * (u[i+1] - 2*u[i] + u[i-1]) / dx**2
            u_new[i] = u[i] + dt * (advection + diffusion)

        u = u_new

    return u
