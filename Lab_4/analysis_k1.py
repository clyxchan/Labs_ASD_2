import numpy as np
# Function to calculate degree, incoming, and outgoing edges for a directed graph
from graph_generation_k1 import generate_matrices adjacency_matrix, adjacency_matrix_undir = generate_matrices()


def analyze_directed_graph(adj_matrix):
    num_nodes = adj_matrix.shape[0]
    degrees = {}
    in_degrees = {}
    out_degrees = {}
    leaf_nodes = []
    isolated_nodes = []


    print("\n--- Directed Graph Analysis ---")


    for i in range(num_nodes):
        out_degree = np.sum(adj_matrix[i, :])
        in_degree = np.sum(adj_matrix[:, i])
        degrees[i] = out_degree + in_degree
        in_degrees[i] = in_degree
        out_degrees[i] = out_degree


        print(f"Node {i}:")
        print(f"  Degree: {degrees[i]}")
        print(f"  Incoming Edges (In-degree): {in_degrees[i]}")
        print(f"  Outgoing Edges (Out-degree): {out_degrees[i]}")


        if out_degree == 0 and in_degree > 0:
            leaf_nodes.append(i)
            pass


        if degrees[i] == 0:
            isolated_nodes.append(i)


    # Перевірка на регулярність
    unique_degrees = set(degrees.values())
    if len(unique_degrees) == 1:
        regularity_degree = list(unique_degrees)[0]
        print(f"\nThe directed graph is regular with degree {regularity_degree}.")
    else:
        print("\nThe directed graph is not regular.")


    print("\nLeaf nodes (nodes with out-degree 0):", leaf_nodes)
    print("Isolated nodes (nodes with degree 0):", isolated_nodes)
    print("-------------------------------------")


def analyze_undirected_graph(adj_matrix):
    num_nodes = adj_matrix.shape[0]
    degrees = {}
    leaf_nodes = []
    isolated_nodes = []


    print("\n--- Undirected Graph Analysis ---")


    adj_matrix_undir = adj_matrix + adj_matrix.T
    adj_matrix_undir[adj_matrix_undir > 1] = 1


    for i in range(num_nodes):
        degree = np.sum(adj_matrix_undir[i, :])
        degrees[i] = degree
        print(f"Node {i}: Degree: {degree}")


        if degree == 1:
            leaf_nodes.append(i)
        elif degree == 0:
            isolated_nodes.append(i)


    #Перевірка на регулярність
    unique_degrees = set(degrees.values())
    if len(unique_degrees) == 1:
        regularity_degree = list(unique_degrees)[0]
        print(f"\nThe undirected graph is regular with degree {regularity_degree}.")
    else:
        print("\nThe undirected graph is not regular.")


    print("\nLeaf nodes (nodes with degree 1):", leaf_nodes)
    print("Isolated nodes (nodes with degree 0):", isolated_nodes)
    print("---------------------------------------")


analyze_directed_graph(adjacency_matrix)
analyze_undirected_graph(adjacency_matrix_undir)
