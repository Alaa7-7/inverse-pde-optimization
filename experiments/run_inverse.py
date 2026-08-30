import numpy as np

from src.pde.solver import solve_pde
from src.inverse.optimizer import optimize
from src.inverse.pso_optimizer import optimize_pso


print("PROGRAM STARTED")


# Grid setup
L = 1.0
Nx = 80
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

dt = 0.0005
Nt = 150

print("Grid initialized")


# True parameters
v_true = 0.8
D_true = 0.05

print("True parameters set")


# One experiment
def run_single_experiment(i):

    print("\nRunning experiment", i)

    u_obs = solve_pde(v_true, D_true, x, dx, dt, Nt)

    # add 1% noise
    u_obs = u_obs + 0.01 * np.random.randn(len(u_obs))

    print("Running GA...")

    v_ga, D_ga = optimize(
        u_obs, x, dx, dt, Nt
    )

    print("Running PSO...")

    v_pso, D_pso = optimize_pso(
        u_obs, x, dx, dt, Nt
    )

    print("Experiment finished")

    return v_ga, D_ga, v_pso, D_pso


# Multiple runs
runs = 3

ga_v_estimates = []
ga_D_estimates = []

pso_v_estimates = []
pso_D_estimates = []


print("\nSTARTING EXPERIMENTS\n")


for i in range(runs):

    v_ga, D_ga, v_pso, D_pso = run_single_experiment(i)

    ga_v_estimates.append(v_ga)
    ga_D_estimates.append(D_ga)

    pso_v_estimates.append(v_pso)
    pso_D_estimates.append(D_pso)


# GA results
ga_v_error = [
    abs(v - v_true)
    for v in ga_v_estimates
]

ga_D_error = [
    abs(D - D_true)
    for D in ga_D_estimates
]


# PSO results
pso_v_error = [
    abs(v - v_true)
    for v in pso_v_estimates
]

pso_D_error = [
    abs(D - D_true)
    for D in pso_D_estimates
]


# Print results
print("\n========== GA RESULTS ==========")

print("Mean v:", np.mean(ga_v_estimates))
print("Mean D:", np.mean(ga_D_estimates))

print("Mean error v:", np.mean(ga_v_error))
print("Mean error D:", np.mean(ga_D_error))


print("\n========== PSO RESULTS ==========")

print("Mean v:", np.mean(pso_v_estimates))
print("Mean D:", np.mean(pso_D_estimates))

print("Mean error v:", np.mean(pso_v_error))
print("Mean error D:", np.mean(pso_D_error))


# Save results

np.savetxt(
    "results/ga_v_estimates.txt",
    ga_v_estimates
)

np.savetxt(
    "results/ga_D_estimates.txt",
    ga_D_estimates
)

np.savetxt(
    "results/pso_v_estimates.txt",
    pso_v_estimates
)

np.savetxt(
    "results/pso_D_estimates.txt",
    pso_D_estimates
)

np.savetxt(
    "results/ga_v_errors.txt",
    ga_v_error
)

np.savetxt(
    "results/ga_D_errors.txt",
    ga_D_error
)

np.savetxt(
    "results/pso_v_errors.txt",
    pso_v_error
)

np.savetxt(
    "results/pso_D_errors.txt",
    pso_D_error
)


print("\nResults saved successfully!")

print("PROGRAM FINISHED")