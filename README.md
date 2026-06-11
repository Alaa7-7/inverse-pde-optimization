#  Inverse PDE Optimization System

##  Overview
This project implements a numerical framework for solving inverse problems in the one-dimensional advection-diffusion equation using a Genetic Algorithm.

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

We aim to solve the inverse problem:

\[
\min_{v, D} \; \| u_{sim}(v,D) - u_{obs} \|_2^2
\]

---

##  Methodology

The system consists of:

### 1. Forward Solver
- Finite Difference Method (FDM)
- Explicit time stepping

### 2. Inverse Solver
- Genetic Algorithm optimization
- Population-based search
- Mutation + crossover strategy

---

##  Results

True parameters:
- v = 0.8  
- D = 0.05  

Estimated results:

- Mean v = 0.7804  
- Mean D = 0.0508  

### Error Analysis:
- v error ˜ 0.0236  
- D error ˜ 0.0020  

The method shows stable convergence and accurate parameter recovery.

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

This framework can be applied in a wide range of scientific and engineering domains, including:

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
- Integrate physics-informed neural networks (PINNs) for hybrid modeling.
- Reduce computational cost using surrogate models or machine learning approximations.
