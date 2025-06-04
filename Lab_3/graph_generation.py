import numpy as np


def generate_matrices(SEED=4329, NUM_NODES=12):
    np.random.seed(SEED)
    random_matrix = 2.0 * np.random.rand(NUM_NODES, NUM_NODES)


    coeff_k = 1.0 - int(str(SEED)[2]) * 0.02 - int(str(SEED)[3]) * 0.005 - 0.25
    adjacency_matrix = (random_matrix * coeff_k >= 1.0).astype(int)


    adjacency_matrix_undir = adjacency_matrix + adjacency_matrix.T
    adjacency_matrix_undir[adjacency_matrix_undir > 1] = 1


    return adjacency_matrix, adjacency_matrix_undir


if __name__ == "__main__":
    adj_matrix_dir, adj_matrix_undir = generate_matrices()
    print("Directed Adjacency Matrix:\n", adj_matrix_dir)
    print("\nUndirected Adjacency Matrix:\n", adj_matrix_undir)
