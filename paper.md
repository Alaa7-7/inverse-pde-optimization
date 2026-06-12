#  Inverse PDE Optimization using Numerical Simulation and Heuristic Algorithms

---

##  Abstract

This project presents a computational framework for solving an inverse parameter estimation problem governed by the one-dimensional Advection–Diffusion equation. The goal is to recover unknown physical parameters (advection velocity and diffusion coefficient) from synthetic observations using numerical simulation and optimization techniques.

The framework integrates:
- Finite Difference Method (FDM) for PDE simulation
- Synthetic data generation
- Heuristic optimization algorithms (Genetic Algorithm, PSO-inspired methods)

The results demonstrate accurate parameter recovery with low error, showing the effectiveness of combining numerical PDE solvers with optimization techniques.

---

## 1. Introduction

Inverse problems in partial differential equations (PDEs) aim to determine unknown parameters of a physical system from observed data. These problems are typically ill-posed and require regularization or optimization-based approaches.

In this work, we focus on estimating:

- Advection velocity \( v \)
- Diffusion coefficient \( D \)

from the Advection–Diffusion system.

This study provides a simplified but realistic computational framework for inverse PDE problems.

---

## 2. Mathematical Model

The governing equation is:

\[
\frac{\partial u}{\partial t} + v \frac{\partial u}{\partial x}
= D \frac{\partial^2 u}{\partial x^2}
\]

Where:

- \( u(x,t) \): transported scalar field
- \( v \): advection velocity (unknown)
- \( D \): diffusion coefficient (unknown)

---

## 3. Numerical Method (Forward Solver)

The PDE is solved using the Finite Difference Method (FDM).

### 3.1 Spatial derivatives

Advection term:

\[
\frac{\partial u}{\partial x} \approx \frac{u_i - u_{i-1}}{\Delta x}
\]

Diffusion term:

\[
\frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1} - 2u_i + u_{i-1}}{\Delta x^2}
\]

---

### 3.2 Time integration

Explicit Euler scheme:

\[
u^{n+1}_i = u^n_i + \Delta t \left( -v \frac{\partial u}{\partial x} + D \frac{\partial^2 u}{\partial x^2} \right)
\]

---

## 4. Inverse Problem Formulation

The goal is to estimate \( v \) and \( D \) by minimizing:

\[
J(v, D) = \| u_{sim}(v, D) - u_{obs} \|_2^2
\]

Where:

- \( u_{sim} \): simulated PDE solution
- \( u_{obs} \): observed synthetic data

This is a nonlinear optimization problem.

---

## 5. Optimization Methods

### 5.1 Genetic Algorithm (GA)

A population-based search method involving:

- Selection
- Crossover
- Mutation

Used to explore the parameter space globally.

---

### 5.2 Particle Swarm Optimization (PSO-inspired)

A swarm-based optimization method that updates candidate solutions based on:

- Best personal position
- Best global position

Provides faster convergence compared to GA.

---

## 6. Experimental Setup

- True parameters:
  - \( v = 0.8 \)
  - \( D = 0.05 \)

- Domain:
  - 1D spatial grid
  - Gaussian initial condition

- Time stepping:
  - Explicit FDM solver

- Multiple runs to evaluate stability

---

## 7. Results

### 7.1 Parameter Estimation

| Method | Estimated v | Estimated D |
|--------|------------|-------------|
| PSO    | 0.80–0.803 | 0.0502–0.0503 |
| GA     | ~0.78      | ~0.0508 |

---

### 7.2 Error Analysis

- PSO shows:
  - Very low error in both parameters
  - High stability across runs

- GA shows:
  - Slightly higher variance
  - Still converges close to true values

---

### 7.3 Statistical Behavior

For multiple runs:

- Mean of \( v \) ˜ 0.78–0.80 depending on method
- Standard deviation is small for PSO
- Diffusion coefficient \( D \) is consistently recovered with high accuracy

---

## 8. Discussion

The results show that combining numerical PDE solvers with heuristic optimization algorithms can effectively solve inverse parameter estimation problems.

Key observations:

- PSO outperforms GA in convergence speed and stability
- The system is robust under multiple runs
- The inverse problem is successfully solved despite being nonlinear

Limitations:

- Synthetic data only (no real experimental data)
- Simple 1D PDE model
- No noise modeling in observations

---

## 9. Conclusion

This project demonstrates a working framework for solving inverse PDE problems using numerical simulation and optimization techniques.

The integration of:
- Finite difference PDE solver
- Heuristic optimization methods

enables accurate recovery of unknown physical parameters.

---

## 10. Future Work

- Extension to 2D and 3D PDEs
- Addition of measurement noise
- Bayesian inference methods
- Neural surrogate models
- Real-world experimental validation

---

##  Applications

- Fluid dynamics
- Heat transfer systems
- Parameter estimation in physics
- Inverse problems in engineering
- Scientific machine learning

---

##  Summary

This project demonstrates that inverse problems governed by PDEs can be effectively solved using computational optimization techniques, bridging numerical simulation and intelligent search algorithms.