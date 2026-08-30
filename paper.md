### Inverse PDE Optimization using Numerical Simulation

## Abstract

This project presents a computational modeling for solving an inverse parameter estimation problem governed by the one-dimensional Advection–Diffusion equation. The goal is to recover unknown physical parameters (advection velocity v and diffusion coefficient D) from synthetic observations using numerical simulation and optimization techniques.

The modeling integrates:

- Finite Difference Method (FDM) for PDE simulation
- Synthetic data generation
- Heuristic optimization algorithms (Genetic Algorithm GA, PSO-inspired methods)

The results demonstrate accurate parameter recovery with low error, showing the effectiveness of combining numerical PDE solvers with optimization techniques.


1. Introduction

Inverse problems in partial differential equations (PDEs) aim to determine unknown parameters of a physical system from observed data. These problems are typically posed and require regularization or optimization approaches.

In this work, we focus on estimating:

- Advection velocity v
- Diffusion coefficient D

from the Advection–Diffusion system.

This study provides a simplified but realistic computational modeling for inverse PDE problems.



2. Mathematical Model

The equation is:

u_t + v * u_x = D * u_xx

Where:

- u(x,t): transported scalar field
- v: advection velocity (unknown)
- D: diffusion coefficient (unknown)


3. Numerical Method

The PDE is solved using the Finite Difference Method (FDM).

3.1 Spatial derivatives

For the advection term, a backward difference is used:

u_x = (u_i - u_(i-1)) / dx

For the diffusion term, a central difference is used:

u_xx = (u_(i+1) - 2*u_i + u_(i-1)) / dx^2

Here, i represents the spatial grid point.


3.2 Time integration

An Explicit Euler scheme is used for time integration.

The update equation used in the numerical solver is:

u_i^(n+1) = u_i^n + dt * (
    -v * (u_i^n - u_(i-1)^n) / dx
    + D * (u_(i+1)^n - 2*u_i^n + u_(i-1)^n) / dx^2
)

Where:

- u_i^n is the solution at spatial point i and time step n
- u_i^(n+1) is the solution at the next time step
- dx is the spatial step
- dt is the time step

This equation is used in the numerical PDE solver to calculate the solution step by step.



4. Inverse Problem Formulation

The goal is to estimate v and D by minimizing the difference between the simulated solution and the observed synthetic data.

The objective function used in the implementation is:

J(v,D) = norm(u_sim(v,D) - u_obs)

Where:

- u_sim: simulated PDE solution
- u_obs: observed synthetic data
- J(v,D): error between the simulated and observed solutions

The optimization algorithms try to find the values of v and D that give the smallest value of J(v,D).

This is a nonlinear optimization problem.



5. Optimization Methods

5.1 Genetic Algorithm (GA)

A population-based search method involving:

- Selection
- Crossover
- Mutation

Used to explore the parameter space globally.


5.2 Particle Swarm Optimization (PSO-inspired)

A swarm-based optimization method that updates candidate solutions based on:

- Best personal position
- Best global position

Provides faster convergence compared to GA.


6. Experimental Setup

- True parameters:
  
  - v = 0.8
  - D = 0.05

- Domain:
  
  - 1D spatial grid
  - Gaussian initial condition

- Time stepping:
  
  - Explicit FDM solver

- Multiple runs to evaluate stability


7. Results

7.1 Parameter Estimation

Method| Estimated v| Estimated D
PSO| 0.80–0.803| 0.0502–0.0503
GA| ~0.78| ~0.0508



7.2 Error Analysis

- PSO shows:
  
  - Very low error in both parameters
  - High stability across runs

- GA shows:
  
  - Slightly higher variance
  - Still converges close to true values



7.3 Statistical Behavior

For multiple runs:

- Mean of v ~ 0.78–0.80 depending on method
- Standard deviation is small for PSO
- Diffusion coefficient D is consistently recovered with high accuracy



8. Discussion

The results show that combining numerical PDE solvers with heuristic optimization algorithms can effectively solve inverse parameter estimation problems.

Key observations:

- PSO outperforms GA in convergence speed and stability
- The system is robust under multiple runs
- The inverse problem is successfully solved despite being nonlinear

Limitations:

- Synthetic data only (no real experimental data)
- Simple 1D PDE model
- No noise modeling in observations



9. Conclusion

This work demonstrates a working framework for solving inverse PDE problems using numerical simulation and optimization techniques.

The integration of:

- Finite difference PDE solver
- Heuristic optimization methods

enables accurate recovery of unknown physical parameters.



10. Future Work

- Extension to 2D and 3D PDEs
- Addition of measurement noise
- Bayesian inference methods
- Neural surrogates
