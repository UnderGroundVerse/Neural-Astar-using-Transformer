import numpy as np


def generate_training_data(num_samples=1000, grid_size=(10, 10)):
    grids = []
    positions = []
    goals = []
    heuristics = []

    for _ in range(num_samples):
        grid = np.zeros(grid_size)
        # Add random obstacles
        for _ in range(np.random.randint(5, 15)):
            x, y = np.random.randint(0, grid_size[0]), np.random.randint(0, grid_size[1])
            grid[x, y] = 1

        start_pos = (np.random.randint(0, grid_size[0]), np.random.randint(0, grid_size[1]))
        goal_pos = (np.random.randint(0, grid_size[0]), np.random.randint(0, grid_size[1]))

        while grid[start_pos[0], start_pos[1]] == 1:
            start_pos = (np.random.randint(0, grid_size[0]), np.random.randint(0, grid_size[1]))
        while grid[goal_pos[0], goal_pos[1]] == 1:
            goal_pos = (np.random.randint(0, grid_size[0]), np.random.randint(0, grid_size[1]))

        h_manhattan = abs(start_pos[0] - goal_pos[0]) + abs(start_pos[1] - goal_pos[1])

        grids.append(grid.flatten())
        positions.append(start_pos)
        goals.append(goal_pos)
        heuristics.append(h_manhattan)

    grids = np.array(grids)
    positions = np.array(positions)
    goals = np.array(goals)
    heuristics = np.array(heuristics)

    inputs = np.hstack([grids, positions, goals])
    return inputs, heuristics