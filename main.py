import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# PSO class
class Particle:
    def __init__(self):
        self.position = np.random.rand(2) * problem_space_size - problem_space_size / 2  # Random start position
        self.velocity = np.random.rand(2) * 2 - 1     # Random start velocity
        self.best_position = self.position.copy()
        self.best_value = self.objective(self.position)

    def objective(self, position):
        # Objective function: Euclidean distance from the target point
        return np.linalg.norm(position - target)

    def update(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.rand(2)
        self.velocity = w * self.velocity + \
                        c1 * r1 * (self.best_position - self.position) + \
                        c2 * r2 * (global_best_position - self.position)
        self.position += self.velocity
        current_value = self.objective(self.position)
        if current_value < self.best_value:
            self.best_position = self.position.copy()
            self.best_value = current_value

def pso(w, c1, c2):
    particles = [Particle() for _ in range(n_particles)]
    global_best_position = min(particles, key=lambda p: p.best_value).best_position.copy()

    def animate(i):
        nonlocal global_best_position  # Declare as nonlocal
        for p in particles:
            p.update(global_best_position, w, c1, c2)
            if p.best_value < Particle().objective(global_best_position):
                global_best_position = p.best_position.copy()
        ax.clear()
        ax.scatter([p.position[0] for p in particles], [p.position[1] for p in particles])
        ax.scatter(target[0], target[1], color='red')  # Target point
        ax.set_xlim(-problem_space_size / 2, problem_space_size / 2)
        ax.set_ylim(-problem_space_size / 2, problem_space_size / 2)
        ax.set_title(f'Iteration: {i+1}')

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate, frames=n_iterations, repeat=False)
    plt.show()

# PSO parameters
n_particles = 50
n_iterations = 50
target = np.array([0, 0])  # Target point at the centre

# size of problem space
problem_space_size = 20

# pso update parameters
w = 0.9  # Inertia weight
c1 = 0.0  # Cognitive coefficient
c2 = 0.2  # Social coefficient

pso(w, c1, c2)
