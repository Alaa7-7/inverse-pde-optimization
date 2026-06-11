import random
import numpy as np
from src.inverse.cost_function import loss


def optimize_pso(u_obs, x, dx, dt, Nt, particles=15, iterations=20):

    # initialize swarm: (v, D)
    swarm = [
        {
            "pos": np.array([
                random.uniform(0.5, 1.0),   # v
                random.uniform(0.01, 0.1)   # D
            ]),
            "vel": np.array([0.0, 0.0]),
            "best": None,
            "best_score": float("inf")
        }
        for _ in range(particles)
    ]

    global_best = None
    global_best_score = float("inf")

    w = 0.7   # inertia
    c1 = 1.5  # cognitive
    c2 = 1.5  # social

    def fitness(pos):
        v, D = pos
        return loss(v, D, x, dx, dt, Nt, u_obs)

    for _ in range(iterations):

        for p in swarm:

            score = fitness(p["pos"])

            if score < p["best_score"]:
                p["best_score"] = score
                p["best"] = p["pos"].copy()

            if score < global_best_score:
                global_best_score = score
                global_best = p["pos"].copy()

        for p in swarm:

            r1 = random.random()
            r2 = random.random()

            cognitive = c1 * r1 * (p["best"] - p["pos"])
            social = c2 * r2 * (global_best - p["pos"])

            p["vel"] = w * p["vel"] + cognitive + social
            p["pos"] = p["pos"] + p["vel"]

            # bounds (VERY IMPORTANT)
            p["pos"][0] = np.clip(p["pos"][0], 0.1, 1.5)   # v
            p["pos"][1] = np.clip(p["pos"][1], 0.001, 0.2) # D

    return global_best