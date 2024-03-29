import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# PSO class
class Particle:
    def __init__(self):
        # Each particle's position is a binary vector representing if an item is included (1) or not (0)
        self.position = np.random.randint(2, size=len(item_values))
        self.velocity = np.random.rand(len(item_values)) - 0.5
        self.best_position = self.position.copy()
        self.best_value = self.objective(self.position)

    def objective(self, position):
        # Objective function: Total value of items in the knapsack
        # Penalising solutions that exceed the maximum weight
        total_weight = np.sum(position * item_weights)
        total_value = np.sum(position * item_values)
        if total_weight > max_weight:
            return 0  # Penalise for exceeding weight
        return total_value

    def update(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.rand(2)
        self.velocity = w * self.velocity + \
                        c1 * r1 * (self.best_position != self.position) + \
                        c2 * r2 * (global_best_position != self.position)
        # Sigmoid function to convert velocity to probability
        sigmoid = 1 / (1 + np.exp(-self.velocity))
        self.position = np.random.rand(len(item_values)) < sigmoid
        current_value = self.objective(self.position)
        if current_value > self.best_value:
            self.best_position = self.position.copy()
            self.best_value = current_value

def pso(w, c1, c2):
    particles = [Particle() for _ in range(n_particles)]
    global_best_position = max(particles, key=lambda p: p.best_value).best_position.copy()

    def animate(i):
        nonlocal global_best_position  # Declare as nonlocal
        for p in particles:
            p.update(global_best_position, w, c1, c2)
            if p.best_value > Particle().objective(global_best_position):
                global_best_position = p.best_position.copy()
        ax.clear()
        # Visualisation showing the value and weight of the current global best
        ax.bar(range(len(global_best_position)), global_best_position * item_values)
        ax.set_title(f'Iteration: {i+1}, Value: {Particle().objective(global_best_position)}')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=n_iterations, repeat=False)
    plt.show()

# Knapsack problem setup
item_values = [10, 5, 15, 7, 6, 18, 3, 1, 10, 5]    # values of items
item_weights = [2, 3, 5, 7, 1, 4, 1, 1, 1, 6]       # weights of items
max_weight = 15                                     # Maximum weight the knapsack can carry

# PSO parameters
n_particles = 20
n_iterations = 50

# pso update parameters
w = 0.2  # Inertia weight
c1 = 0.5  # Cognitive coefficient
c2 = 0.5  # Social coefficient

pso(w, c1, c2)
