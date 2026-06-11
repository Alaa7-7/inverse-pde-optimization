import numpy as np

from src.pde.solver import solve_pde
from src.inverse.optimizer import optimize
from src.inverse.pso_optimizer import optimize_pso


print("?? PROGRAM STARTED")


# ======================
# Grid setup
# ======================
L = 1.0
Nx = 80
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

dt = 0.0005
Nt = 150


print("?? Grid initialized")


# ======================
# True parameters
# ======================
v_true = 0.8
D_true = 0.05

print("?? True parameters set")


# ======================
# One experiment
# ======================
def run_single_experiment(i):
    print(f"\n?? Running experiment {i}")

    u_obs = solve_pde(v_true, D_true, x, dx, dt, Nt)

    # add noise
    u_obs = u_obs + 0.01 * np.random.randn(len(u_obs))

    print("   ?? Optimizing...")

    v_est, D_est = optimize(u_obs, x, dx, dt, Nt)
    v_est, D_est = optimize_pso(u_obs, x, dx, dt, Nt)

    print("   ? Done")

    return v_est, D_est


# ======================
# Multiple runs (small for debugging)
# ======================
runs = 3   # IMPORTANT: small for testing

v_errors = []
D_errors = []

v_estimates = []
D_estimates = []

print("\n?? STARTING LOOP...\n")

for i in range(runs):
    v_est, D_est = run_single_experiment(i)

    v_estimates.append(v_est)
    D_estimates.append(D_est)

    v_errors.append(abs(v_est - v_true))
    D_errors.append(abs(D_est - D_true))


# ======================
# Results
# ======================
print("\n========== FINAL RESULTS ==========")

print("True v:", v_true)
print("True D:", D_true)

print("\n--- Estimates ---")
print("Mean v:", np.mean(v_estimates))
print("Mean D:", np.mean(D_estimates))

print("\n--- Errors ---")
print("Mean error v:", np.mean(v_errors))
print("Mean error D:", np.mean(D_errors))
print("Std v:", np.std(v_errors))
print("Std D:", np.std(D_errors))



# ======================
# Save results
# ======================
np.savetxt("results_v_estimates.txt", v_estimates)
np.savetxt("results_D_estimates.txt", D_estimates)

np.savetxt("errors_v.txt", v_errors)
np.savetxt("errors_D.txt", D_errors)

print("\n?? Results saved successfully!")
print("? results_v_estimates.txt")
print("? results_D_estimates.txt")
print("? errors_v.txt")
print("? errors_D.txt")

print("\n?? PROGRAM FINISHED SUCCESSFULLY")