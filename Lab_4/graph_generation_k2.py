import numpy as np


def generate_matrices(SEED=4329, NUM_NODES=12):
    np.random.seed(SEED)
    random_matrix = 2.0 * np.random.rand(NUM_NODES, NUM_NODES)


    coeff_k = 1.0 - int(str(SEED)[2]) * 0.005 - int(str(SEED)[3]) * 0.005 - 0.27
    adjacency_matrix = (random_matrix * coeff_k >= 1.0).astype(int)


    return adjacency_matrix


if __name__ == "__main__":
    adj_matrix_dir = generate_matrices()
    print("Directed Adjacency Matrix:\n", adj_matrix_dir)
