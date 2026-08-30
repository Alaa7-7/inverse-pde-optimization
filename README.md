### Inverse PDE Optimization System

## Overview

This project implements a numerical model for solving inverse problems in the one-dimensional advection-diffusion equation using optimization methods.

The main idea is to estimate unknown physical parameters (advection velocity and diffusion coefficient) from observed data.

-----------------------------------------------------------------------------------
```
The system is based on the advection-diffusion equation:

u_t + v * u_x = D * u_xx

Where:

- u(x,t): transported quantity
- v: advection velocity (unknown)
- D: diffusion coefficient (unknown)
```
-------------------------------------------------------------------------------------------------

## Objective

The objective is to find the values of v and D that minimize the difference between the simulated solution and the observed data.
```
The objective function used in the implementation is:

J(v,D) = norm(u_sim(v,D) - u_obs)

Where:

- u_sim: solution from numerical PDE solver
- u_obs: observed synthetic data
- J(v,D): error between the simulated and observed solutions

The optimization methods search for the values of v and D that give the smallest value of J(v,D).
```
------------------------------------------------------------------------------------------------------

## Methodology

The system consists of:
```
1. PDE 

- Finite Difference Method (FDM)
- Explicit time stepping
- Backward difference for the advection term
- Central difference for the diffusion term

The spatial approximations used in the solver are:

u_x = (u_i - u_(i-1)) / dx

u_xx = (u_(i+1) - 2*u_i + u_(i-1)) / dx^2

The time update is:

u_i^(n+1) = u_i^n + dt * (
    -v * (u_i^n - u_(i-1)^n) / dx
    + D * (u_(i+1)^n - 2*u_i^n + u_(i-1)^n) / dx^2
)

Here, i represents the spatial grid point and n represents the time step.
```
```
2. Optimization

Two optimization methods are implemented:

Genetic Algorithm (GA)

- Population-based stochastic search
- Selection, crossover, mutation
- Constraint-based parameter bounds

Particle Swarm Optimization (PSO)

- Velocity-position update mechanism
- Cognitive and social learning components
- Improved convergence stability
```
---------------------------------------------------------------------------------
```
# Experiment

- Domain: 1D spatial grid
- Grid points: 80
- Time steps: 150
- Time step size: 0.0005
- Initial condition: Gaussian pulse
- Noise level: 1% Gaussian noise added to observations
- Multiple runs are used to evaluate stability

```

# Results
```
True parameters:

- v = 0.8
- D = 0.05

Estimated Results (GA)

- v = 0.7804
- D = 0.0508

Error Analysis

- v error |v - v_true| ~ 0.0236
- D error |D - D_true| ~ 0.0020

The method shows stable convergence and accurate parameter recovery.

Estimated Results (PSO)

- v ~ 0.79 - 0.81
- D ~ 0.0499 - 0.0505

Error Analysis

- v error |v - v_true| ~ 0.0075
- D error |D - D_true| ~ 0.00026
```
-----------------------------------------------------------------

## PSO and Genetic Algorithm Comparison

The project includes two optimization methods for solving the inverse PDE problem:
```
Methods Used

- Genetic Algorithm (GA)
- Particle Swarm Optimization (PSO)
```
---------------------------------------------------------------------------

## Results

- | Method         | Error (v)    | Error (D)   | Stability
  |----------------|--------------|-------------|-----------
  | GA             | ~0.0236      | ~0.0020     | medium
  | PSO            | ~0.0075      | ~0.00026    | High

------------------------------------------------------------------------------------------
## Main Result
```
- PSO converges faster than Genetic Algorithm.
- PSO provides more stable parameter estimation.
- GA is still useful as a baseline stochastic method.
- Both methods successfully recover the true parameters under noisy observations.
```
------------------------------------------------------------------------------------------------

## Conclusion

The comparison shows that PSO performs better than the Genetic Algorithm in accuracy and stability for the inverse PDE parameter estimation problem considered in this project.

The results show that optimization methods can be combined with a numerical PDE solver to estimate unknown physical parameters from observed data.

------------------------------------------------------------------------------------------------

## Project Structure
```
 inverse-pde-optimization/
¦
+-- src/
¦   +-- pde/
¦   ¦   +-- solver.py
¦   ¦       Forward PDE solver - Advection/Diffusion
¦   ¦
¦   +-- inverse/
¦   ¦   +-- optimizer.py
¦   ¦   ¦   Genetic Algorithm optimizer
¦   ¦   ¦
¦   ¦   +-- pso_optimizer.py
¦   ¦   ¦   Particle Swarm Optimization
¦   ¦   ¦
¦   ¦   +-- cost_function.py
¦   ¦       Loss function
¦   ¦
¦   +-- ml/
¦       +-- problem_model.py
¦           Fitness evaluation model
¦
+-- experiments/
¦   +-- run_inverse.py
¦       Main experiment runner
¦
+-- results/
¦   +-- results_v_estimates.txt
¦   +-- results_D_estimates.txt
¦
+-- paper.tex
¦   LaTeX paper
¦
+-- paper.pdf
¦   Final research paper
¦
+-- README.md
+-- requirements.txt
```
--------------------------------------------------------------------------------------

## How to Run

1. Install requirements

pip install -r requirements.txt

2. Run the experiment

PYTHONPATH=. python experiments/run_inverse.py

----------------------------------------------------------------------------------

## Applications
```
This model can be applied in a wide range of scientific and engineering domains, including:

- Fluid dynamics and transport phenomena
- Environmental modeling (pollution and diffusion processes)
- Heat transfer and thermal systems
- Parameter estimation in physical systems
- Inverse problems in computational physics
- Scientific machine learning and hybrid AI-physics models
```
-------------------------------------------------------------------------------------------

## Future Work

The current implementation can be extended in several directions to improve accuracy, scalability, and scientific impact:
```
- Test the optimization methods with different noise levels and parameter ranges.
- Extend the model to 2D and 3D partial differential equations.
- Improve numerical stability using higher-order discretization schemes.
- Introduce uncertainty quantification for estimated parameters.
- Integrate physics-informed neural networks for hybrid modeling.
- Reduce computational cost using surrogate models or machine learning approximations.
- Compare with additional optimization methods.
```