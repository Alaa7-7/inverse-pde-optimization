import random
import numpy as np
from src.inverse.cost_function import loss


def optimize(u_obs, x, dx, dt, Nt, generations=12):

    # initial population (v, D)
    population = [
        (random.uniform(0.6, 1.0), random.uniform(0.01, 0.08))
        for _ in range(6)
    ]

    def fitness(ind):
        v, D = ind
        return -loss(v, D, x, dx, dt, Nt, u_obs)

    for gen in range(generations):

        population = sorted(population, key=fitness, reverse=True)

        parents = population[:3]
        children = []

        for _ in range(5):

            p1, p2 = random.sample(parents, 2)

            v_child = (p1[0] + p2[0]) / 2
            D_child = (p1[1] + p2[1]) / 2

            # mutation
            v_child += random.uniform(-0.02, 0.02)
            D_child += random.uniform(-0.002, 0.002)

            # =========================
            # IMPORTANT: PHYSICAL BOUNDS
            # =========================
            v_child = max(0.1, min(1.5, v_child))
            D_child = max(0.001, min(0.2, D_child))

            children.append((v_child, D_child))

        population = parents + children

    best = max(population, key=fitness)

    return best