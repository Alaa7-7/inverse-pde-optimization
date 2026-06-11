import random
from src.inverse.cost_function import loss

def optimize(u_obs, x, dx, dt, Nt, generations=40):

    # initial population (v, D)
    population = [
        (random.uniform(0, 1), random.uniform(0, 0.1))
        for _ in range(20)
    ]

    def fitness(ind):
        v, D = ind
        return -loss(v, D, x, dx, dt, Nt, u_obs)

    for _ in range(generations):

        population = sorted(population, key=fitness, reverse=True)
        parents = population[:5]

        children = []

        for _ in range(15):
            p1, p2 = random.sample(parents, 2)

            child = (
                (p1[0] + p2[0]) / 2,
                (p1[1] + p2[1]) / 2
            )

            children.append(child)

        population = parents + children

    return max(population, key=fitness)