import graph_generation
import draw


adj_matrix_dir, adj_matrix_undir = graph_generation.generate_matrices()


print("Directed Adjacency Matrix:\n", adj_matrix_dir)
print("\nUndirected Adjacency Matrix:\n", adj_matrix_undir)


draw.draw_graph(adj_matrix_undir, directed=False)
draw.draw_graph(adj_matrix_dir, directed=True)
