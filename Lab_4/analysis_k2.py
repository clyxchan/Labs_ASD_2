import numpy as np
import matplotlib.pyplot as plt
from graph_generation_k2 import generate_matrices
from draw import draw_graph


adjacency_matrix = generate_matrices()
NUM_NODES = adjacency_matrix.shape[0]


print("\n--- Directed Graph Analysis ---")
for i in range(NUM_NODES):
    print(f"Node {i}:")
    print(f"  Degree: {np.sum(adjacency_matrix[i, :]) + np.sum(adjacency_matrix[:, i])}")
    print(f"  Incoming Edges (In-degree): {np.sum(adjacency_matrix[:, i])}")
    print(f"  Outgoing Edges (Out-degree): {np.sum(adjacency_matrix[i, :])}")


print("\n--- Directed Graph Paths ---")
adj_matrix_sq = np.linalg.matrix_power(adjacency_matrix, 2)
adj_matrix_cube = np.linalg.matrix_power(adjacency_matrix, 3)


paths_2 = [f"{i}->{j}" for i in range(NUM_NODES) for j in range(NUM_NODES) if adj_matrix_sq[i, j] > 0]
print("Paths of length 2:\n", ",".join(paths_2))


print("\nPaths of length 3:")
paths_3 = []
for i in range(NUM_NODES):
    for j in range(NUM_NODES):
        if adj_matrix_cube[i, j] > 0:
            for m in range(NUM_NODES):
                for n in range(NUM_NODES):
                    if adjacency_matrix[i, m] == 1 and adjacency_matrix[m, n] == 1 and adjacency_matrix[n, j] == 1:
                        paths_3.append(f"{i}->{m}->{n}->{j}")


print(",".join(paths_3))
print("----------------------------")


print("\n--- Reachability Matrix (Directed) ---")
reachability_matrix = np.copy(adjacency_matrix)
for i in range(NUM_NODES):
    reachability_matrix[i, i] = 1


for k in range(NUM_NODES):
    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            if reachability_matrix[i, k] == 1 and reachability_matrix[k, j] == 1:
                reachability_matrix[i, j] = 1


print(reachability_matrix)


print("\n--- Strongly Connected Components (Directed) ---")
print("Strongly Connected Components:")


visited_scc1 = [False] * NUM_NODES
stack = []


def fill_order(node):
    visited_scc1[node] = True
    for neighbor in range(NUM_NODES):
        if adjacency_matrix[node, neighbor] == 1 and not visited_scc1[neighbor]:
            fill_order(neighbor)
    stack.append(node)


for i in range(NUM_NODES):
    if not visited_scc1[i]:
        fill_order(i)


transpose_matrix = adjacency_matrix.T
visited_scc2 = [False] * NUM_NODES
strongly_connected_components = []


def dfs_transpose(node, component):
    visited_scc2[node] = True
    component.append(node)
    for neighbor in range(NUM_NODES):
        if transpose_matrix[node, neighbor] == 1 and not visited_scc2[neighbor]:
            dfs_transpose(neighbor, component)


while stack:
    node = stack.pop()
    if not visited_scc2[node]:
        component = []
        dfs_transpose(node, component)
        strongly_connected_components.append(sorted(component))


for i, scc in enumerate(strongly_connected_components, start=1):
    print(f"SCC {i}: {scc}")


print("---------------------------------------------")


print("\n--- Condensed Graph ---")
num_sccs = len(strongly_connected_components)


if num_sccs == 1:
    print("Graph is fully strongly connected, no condensation needed.")
   
    plt.figure(figsize=(6, 6))
    plt.text(0.5, 0.5, "No condensed graph", fontsize=14, ha="center", va="center", color="red")
    plt.axis("off")
    plt.title("Condensed Graph (Empty)")
    plt.show()
else:
    condensed_adj_matrix = np.zeros((num_sccs, num_sccs), dtype=int)
    scc_map = {node: i for i, scc in enumerate(strongly_connected_components) for node in scc}


    for i in range(NUM_NODES):
        for j in range(NUM_NODES):
            if adjacency_matrix[i, j] == 1:
                scc_i = scc_map[i]
                scc_j = scc_map[j]
                if scc_i != scc_j:
                    condensed_adj_matrix[scc_i, scc_j] = 1


    print("Condensed Graph Adjacency Matrix:")
    print(condensed_adj_matrix)
    print("----------------------------------")
    print("\n--- Drawing Condensed Directed Graph ---")
    draw_graph(condensed_adj_matrix, directed=True)
