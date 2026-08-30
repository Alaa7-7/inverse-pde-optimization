### Inverse PDE Optimization System

## Overview

In this project, I solve a simple inverse problem using a numerical model.

The model is based on the one-dimensional advection-diffusion equation.

```
My idea is to find two unknown values:

- "v": advection velocity
- "D": diffusion coefficient
```
I first create a numerical solution using known values of "v" and "D".

Then I add random noise with a scale of 0.01 to create noisy observed data to the solution to make the data closer to observed data.
```
After that, I use two optimization methods to find values close to the original values:

- Genetic Algorithm (GA)
- Particle Swarm Optimization (PSO)
```


--------------------------------------------------------------------------------------------


## Inverse Problem

In this project, I use an inverse problem to find unknown values from observed data.

```
The unknown values are:

- "v": advection velocity
- "D": diffusion coefficient
```

First, I use known values of "v" and "D" in the PDE solver to create a solution.


```
Then I add noise to this solution and use it as observed data:

u_obs = u_true + noise
```


After that, I do not give the optimization methods the true values of "v" and "D".

Instead, GA and PSO try different values of "v" and "D".

```
For each try, the PDE solver creates a new simulated solution:

u_sim = solve_pde(v, D)

Then I compare the simulated solution with the observed data:

J(v,D) = norm(u_sim - u_obs)
```

If the value of "J" is small, the simulated result is close to the observed data.

The optimization methods continue searching for values that give a small "J".

```
So, the main idea of the inverse problem in my project is:

Observed data
      |
      v
Try v and D
      |
      v
PDE solver
      |
      v
Simulated data
      |
      v
Calculate error
      |
      v
Find better v and D
```


This is called an inverse problem because I start with the observed result and try to find the unknown parameters that produced a similar result.

I use this approach because the main goal of my project is to estimate "v" and "D" from observed data.


-----------------------------------------------------------------------------------------------



## Main Equation
```
The model uses the following equation:

u_t + v * u_x = D * u_xx

Here:

- "u" is the value being transported.
- "v" is the advection velocity.
- "D" is the diffusion coefficient.
- "u_t" means change of "u" with time.
- "u_x" means change of "u" with position.
- "u_xx" is the second position change.

I use this equation because it is a simple model for studying transport and diffusion.
```


-------------------------------------------------------------------------------



## Idea

The main goal is to find "v" and "D" from observed data.

The code compares the simulated result with the observed result.


```
The loss used in the code is:

J(v,D) = norm(u_sim(v,D) - u_obs)

Here:

- "u_sim" is the result from my PDE solver.
- "u_obs" is the observed data.
- "J" is the difference between the two results.
- "norm" gives the size of this difference.

The optimization methods try to find values of "v" and "D" that give a small loss.

I use this loss because I need a simple way to compare the simulated solution with the observed data.
```

-------------------------------------------------------



## Numerical Method

I use the Finite Difference Method (FDM) to solve the equation.

I chose FDM because it is simple to implement and works well for this one-dimensional problem.

```
Advection

For the advection part, I use an upwind difference:

u_x = (u[i] - u[i-1]) / dx

In the code, the advection part is:

-v * (u[i] - u[i-1]) / dx

I use the upwind method because it is simple and follows the direction of the transport in the code.
```


```
Diffusion

For the diffusion part, I use a central difference:

u_xx = (u[i+1] - 2*u[i] + u[i-1]) / dx^2

I use the central difference because it is a simple way to calculate the second position change.

Time Update

The code updates the solution using:

u_new[i] = u[i] + dt * (advection + diffusion)

I use this simple time update because the project is focused on parameter estimation and not on using a complicated numerical solver.
```

---------------------------------------------------------------------------------------


## Initial Condition

I start the simulation with a Gaussian Funcion.


```
The code uses:

u = exp(-100 * (x - 0.3)^2)

I use a simple bell-shaped function because it gives a simple shape that can move and spread during the simulation.
```

--------------------------------------------------------------------------------------------------


## Model Setup


```
The main values used in the program are:

Grid points = 80
Time steps = 150
dt = 0.0005

The spatial domain is:

0 <= x <= 1

The true parameter values are:

v = 0.8
D = 0.05

I use these values to create the original simulated data.
```

----------------------------------------------------------------------------


## Noise

```
After creating the original solution, I add random noise with a scale of 0.01:

u_obs = u_obs + 0.01 * random_noise

I add noise because real observations are usually not exactly equal to the numerical solution.

The noise also gives the optimization methods a more realistic test.
```

--------------------------------------------------------------------------


## Optimization Methods

I use two methods in the project.

# Genetic Algorithm (GA)

GA means Genetic Algorithm.

I start with random values for "v" and "D". Then I keep the best solutions and use them to create new solutions.

```
The new value is calculated using the two selected parents:

v_new = (v1 + v2) / 2

D_new = (D1 + D2) / 2

Then I add a small random change called mutation:

v_new = v_new + random(-0.02, 0.02)

D_new = D_new + random(-0.002, 0.002)

I use this step to create new solutions and search for better values of "v" and "D".

The code also keeps the values inside fixed limits.
```

```
I use a small population of possible values for "v" and "D".

The code starts with random values:

v = 0.6 to 1.0
D = 0.01 to 0.08

For each generation, I:

1. Calculate the loss for each solution.
2. Sort the solutions by their loss.
3. Keep the best solutions.
4. Choose two parent solutions.
5. Create a new solution from the parents.
6. Add a small random change called mutation.
7. Keep the values inside the allowed limits.

I chose GA because it is simple and gives me a population-based search.
```

-----------------------------------------------------------------------------------------


# PSO Method

PSO means Particle Swarm Optimization.

```
Each particle has a position and a velocity.

The velocity is updated using:

velocity = w * velocity
         + c1 * r1 * (best - position)
         + c2 * r2 * (global_best - position)

Then the position is updated using:

position = position + velocity

Here:

- "w = 0.7" controls the old velocity.
- "c1 = 1.5" uses the particle's own best position.
- "c2 = 1.5" uses the best position found by all particles.
- "r1" and "r2" are random values between 0 and 1.

```

```
I use particles that contain values for "v" and "D".

Each particle also has a velocity.

The code uses:

w = 0.7
c1 = 1.5
c2 = 1.5

The particles use their own best result and the best result found by the group.

The position is then updated using the velocity.

I use PSO because it gives another simple optimization method to compare with GA.
```

--------------------------------------------------------------------------------


## Experiment

```
I run the experiment 3 times.

For every run, I:

1. Create the original PDE solution.
2. Add 1% Gaussian noise.
3. Run the Genetic Algorithm.
4. Run the PSO method.
5. Save the estimated values.
6. Calculate the error.

I use 3 runs to check if the results are reasonably stable.

Because the optimization methods use random values, the results can be different from one run to another.

```

---------------------------------------------------------------------------------------

## Error Calculation

I calculate the error by comparing the estimated value with the true value.

```
For "v", I use:

v_error = |v_est - v_true|

For "D", I use:

D_error = |D_est - D_true|

The "| |" means absolute value.

For example, if:

v_true = 0.8
v_est = 0.7957

then:

v_error = |0.7957 - 0.8|
        = 0.0043
```

```
I calculate the error for each run.

Then I calculate the mean error:

mean_error = sum of errors / number of runs

In the code, I use "np.mean()" to calculate the mean.

I use the absolute error because it is simple and shows how far the estimated value is from the true value.

```

----------------------------------------------------------------------------------------


## Results

```
The true values are:

v = 0.8
D = 0.05
```

```
GA Results

The mean results from the 3 runs are:

v = 0.7957
D = 0.04993

The mean errors are:

v error = 0.01499
D error = 0.000261

These values are close to the true values.
```


```
PSO Results

The mean results from the 3 runs are:

v = 0.7977
D = 0.04963

The mean errors are:

v error = 0.01266
D error = 0.000365

These values are also close to the true values.
```

--------------------------------------------------------------------


## GA and PSO Comparison

I compare GA and PSO using the estimated values and the errors from each method.

```
For both methods, I calculate the error using:

v_error = |v_est - v_true|

D_error = |D_est - D_true|

Then I calculate the mean error over the 3 runs:

mean_error = sum of errors / number of runs

I use the same noisy data and the same PDE solver for both methods.

This makes the comparison easier because both methods are tested in the same way.

```

The results are:

- | Method          | Mean v        | Mean D      | Mean v Error          | Mean D Error
  |-----------------|---------------|-------------|-----------------------|--------------
  | GA              | 0.7957        | 0.04993     | 0.01499               | 0.000261
  | PSO             | 0.7977        | 0.04963     | 0.01266               | 0.000365

```
From these 3 runs:

- PSO gives a smaller error for "v".
- GA gives a smaller error for "D".
- Both methods give values close to the true values.
- The difference between the two methods is small.
- The results can change because the methods use random values.
I use the same error calculation for both methods so the comparison is fair.

```

--------------------------------------------------------------------------------------


```
Why I Used These Steps

I used a numerical PDE solver first because I need a simulated solution before I can solve the inverse problem.

I then added noise because I want to test the optimization methods with data that is not perfect.

I used GA and PSO because both methods can search for unknown parameters without needing a complicated mathematical optimization method.

I used the same PDE solver and the same noisy data for both methods so I can make a simple comparison.

I used 3 runs because the optimization methods contain random steps and I want to see if the results stay close to the true values.
```

-------------------------------------------------------------------------------------------


```
 Project Structure

inverse-pde-optimization/
|
+-- src/
|   +-- pde/
|   |   +-- solver.py
|   |       PDE solver
|   |
|   +-- inverse/
|       +-- optimizer.py
|       |   Genetic Algorithm
|       |
|       +-- pso_optimizer.py
|       |   PSO method
|       |
|       +-- cost_function.py
|           Loss function
|
+-- experiments/
|   +-- run_inverse.py
|       Main experiment
|
+-- results/
|   +-- ga_v_estimates.txt
|   +-- ga_D_estimates.txt
|   +-- ga_v_errors.txt
|   +-- ga_D_errors.txt
|   +-- pso_v_estimates.txt
|   +-- pso_D_estimates.txt
|   +-- pso_v_errors.txt
|   +-- pso_D_errors.txt
|
+-- paper/
|   +-- paper.tex
|   +-- paper.pdf
|   +-- paper.md
|   +-- sections/
|
+-- README.md
+-- requirements.txt
+-- .gitignore

```

------------------------------------------------------------------------


## How to Run

```
First, install the required packages:

pip install -r requirements.txt

From the main project folder, run:

PYTHONPATH=. python experiments/run_inverse.py

On Git Bash, the command above should be used from:

/c/project4/inverse-pde-optimization

The program runs the experiments and saves the results in the "results" folder
```

------------------------------------------------------------------------------


## Applications


```
This type of model can be useful for:

- Fluid and transport problems
- Pollution and diffusion models
- Heat transfer
- Physical parameter estimation
- Inverse problems in computational physics

This project is a simple educational example of an inverse PDE problem.

```


## Future Work
```
In the future, I can:

- Run more experiments.
- Test different noise levels.
- Test different parameter ranges.
- Extend the model to 2D and 3D.
- Try other optimization methods.
- Improve the numerical solver.
- Use machine learning methods for inverse PDE problems
```