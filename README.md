#  Inverse PDE Optimization System

##  Overview
This project implements a numerical model for solving inverse problems in the one-dimensional advection-diffusion equation using a Genetic Algorithm.

The goal is to estimate unknown physical parameters (advection velocity and diffusion coefficient) from observed data.

---

##  Governing Equation

The system is based on the advection-diffusion equation:

\[
\frac{\partial u}{\partial t} + v \frac{\partial u}{\partial x} = D \frac{\partial^2 u}{\partial x^2}
\]

Where:
- *u(x,t)*: transported quantity
- *v*: advection velocity (unknown)
- *D*: diffusion coefficient (unknown)

---

##  Objective

The objective is to solve:

\[
\min_{v, D} \; \| u_{sim}(v,D) - u_{obs} \|_2^2
\]

Where:
- *u_{sim}*: solution from numerical PDE solver
- *u_{obs}*: noisy observed data

---

##  Methodology

The system consists of:

### 1. Forward Solver
- Finite Difference Method (FDM)
- Explicit time stepping
- Central difference for diffusion term

### 2. Inverse Solver
Two optimization methods are implemented:
- Genetic Algorithm (GA)
     .Population-based stochastic search
     .Selection, crossover, mutation
     .Constraint-based parameter bounds
- Particle Swarm Optimization (PSO)
     .Velocity-position update mechanism
     .Cognitive + social learning components
     .Improved convergence stability
---
### Experimental Setup

 .Domain: 1D spatial grid
 .Grid points: 80
 .Time steps: 150
 .Time step size: 0.0005
 .Initial condition: Gaussian pulse
 .Noise level: 1% Gaussian noise added to observations

---

##  Results

True parameters:
- v = 0.8  
- D = 0.05  

Estimated results (GA):

-  v = 0.7804  
-  D = 0.0508  

### Error Analysis:
- v error |v - v_true| ˜ 0.0236  
- D error |D - D_true| ˜ 0.0020  

The method shows stable convergence and accurate parameter recovery.

Estimated results (PSO):
-  v ~ 0.79 - 0.81  
-  D ~ 0.0499 - 0.0505  

### Error Analysis:
- v error |v - v_true| ˜ 0.0075 
- D error |D - D_true| ˜ 0.00026


##  PSO vs Genetic Algorithm (Performance Comparison)

The project now includes two optimization methods for solving the inverse PDE problem:

###  Methods Used

- Genetic Algorithm (GA)
- Particle Swarm Optimization (PSO)

---

###  Performance Results

| Method |  Error (v)     |  Error (D)     | Stability |
|--------|----------------|----------------|-----------|
| GA     | ~0.0236        | ~0.0020        | Moderate  |
| PSO    | ~0.0075        | ~0.00026       | High      |

---

###  Key Observation

- PSO converges faster than Genetic Algorithm.
- PSO provides more stable parameter estimation.
- GA is still useful as a baseline stochastic method.
- Both methods successfully recover true parameters under noisy observations

---

###  Conclusion

The comparison demonstrates that PSO outperforms the Genetic Algorithm in accuracy and stability for inverse PDE parameter estimation problems.

---

## Project Structure

- inverse-pde-optimization/
  - src/
    - pde/
      - solver.py              (Forward PDE solver - Advection/Diffusion)
    - inverse/
      - optimizer.py           (Genetic Algorithm optimizer)
      - cost_function.py       (Loss function)
    - ml/
      - problem_model.py       (Fitness evaluation model)

  - experiments/
    - run_inverse.py          (Main experiment runner)

  - results/
    - results_v_estimates.txt
    - results_D_estimates.txt

  - paper.tex                 (LaTeX paper)
  - paper.pdf                 (Final research paper)
  - README.md
  - requirements.txt
---

##  How to Run

### 1. Install requirements
```bash
pip install -r requirements.txt
PYTHONPATH=. python experiments/run_inverse.py

## Applications

This model can be applied in a wide range of scientific and engineering domains, including:

- Fluid dynamics and transport phenomena
- Environmental modeling (pollution and diffusion processes)
- Heat transfer and thermal systems
- Parameter estimation in physical systems
- Inverse problems in computational physics
- Scientific machine learning and hybrid AI-physics models

## Future Work

The current implementation can be extended in several directions to improve accuracy, scalability, and scientific impact:

- Replace Genetic Algorithm with more advanced optimizers such as Particle Swarm Optimization (PSO) or Bayesian Optimization.
- Extend the model to 2D and 3D partial differential equations.
- Improve numerical stability using higher-order discretization schemes.
- Introduce uncertainty quantification for estimated parameters.
- Integrate physics-informed neural networks for hybrid modeling.
- Reduce computational cost using surrogate models or machine learning approximations.
