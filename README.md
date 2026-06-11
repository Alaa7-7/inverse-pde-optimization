# Inverse PDE Optimization System

## Overview

This project solves an inverse problem for the 1D Advection–Diffusion equation using evolutionary optimization.

## Equation

?u/?t + v ?u/?x = D ?²u/?x²

## Goal

Estimate:

- velocity (v)
- diffusion coefficient (D)

from noisy observations.

## Method

- Finite Difference Method (FDM)
- Synthetic data generation
- Genetic Algorithm optimization
- L2 loss minimization

## Pipeline

1. Generate PDE solution (true parameters)
2. Add noise
3. Optimize parameters using GA
4. Compare estimated vs true values

## Output

- Estimated physical parameters
- Error analysis
- Convergence behavior

