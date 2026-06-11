import numpy as np


def solve_pde(v, D, x, dx, dt, Nt):
    """
    Solves 1D Advection-Diffusion equation:
    du/dt + v du/dx = D d2u/dx2
    """

    # initial condition (Gaussian pulse)
    u = np.exp(-100 * (x - 0.3) ** 2)

    Nx = len(x)

    for n in range(Nt):
        u_new = u.copy()

        for i in range(1, Nx - 1):

            # advection term (upwind scheme)
            advection = -v * (u[i] - u[i - 1]) / dx

            # diffusion term (central difference)
            diffusion = D * (u[i + 1] - 2 * u[i] + u[i - 1]) / dx**2

            # update
            u_new[i] = u[i] + dt * (advection + diffusion)

        u = u_new

    return u


def save_solution(x, u, filename="results/final_profile.txt"):
    np.savetxt(filename, u)
    print("Saved solution to:", filename)