import numpy as np
import matplotlib.pyplot as plt
NUM_NODES = 12


def draw_graph(adj_matrix, directed):


# Parameters for visualization
    NODE_RADIUS = 0.05
    LINE_THICKNESS = 1.5


    NUM_NODES = adj_matrix.shape[0]


    center_node = np.array([[1, 1]])


    num_boundary_nodes = NUM_NODES - 1


    nodes_per_side = num_boundary_nodes // 4


    remainder_nodes = num_boundary_nodes % 4


    boundary_nodes = []


    sides = [0, 1, 2, 3]
    side_node_counts = [nodes_per_side] * 4


    for i in range(remainder_nodes):
      side_node_counts[i] += 1


    for side, count in zip(sides, side_node_counts):
      if count > 0:


        spacing = np.linspace(0.3, 1.7, count)


        if side == 0:
          boundary_nodes.extend([[x, 0] for x in spacing])
        elif side == 1:
          boundary_nodes.extend([[2, y] for y in spacing])
        elif side == 2:
          boundary_nodes.extend([[x, 2] for x in spacing])
        elif side == 3:
          boundary_nodes.extend([[0, y] for y in spacing])


    all_nodes = np.array(boundary_nodes)


    if NUM_NODES > 0:
      all_nodes = np.vstack((center_node, all_nodes))




    plt.figure(figsize=(8, 8))


# Draw edges first
    focus_point = np.array([1, 1])


    if directed:
      title = 'Directed Graph Representation'
      for i in range(NUM_NODES):
        for j in range(NUM_NODES):
          if adj_matrix[i, j] == 1:
            node1 = all_nodes[i]
            node2 = all_nodes[j]


            if i == j:
                x, y = node1
                r = NODE_RADIUS * 1.5
                theta = np.linspace(-np.pi/2, 3*np.pi/2, 100)
                circle_x = x + r * np.cos(theta)
                circle_y = y + r + r * np.sin(theta)
                plt.plot(circle_x, circle_y, 'r-', linewidth=LINE_THICKNESS)


                arrow_point_idx = np.argmin(np.abs(theta + np.pi/2))
                arrow_point = np.array([circle_x[arrow_point_idx], circle_y[arrow_point_idx]])
                direction = np.array([ -np.sin(theta[arrow_point_idx]), np.cos(theta[arrow_point_idx])])
                direction = direction / np.linalg.norm(direction)


                arrow_base = arrow_point - direction * NODE_RADIUS * 0.5
                plt.arrow(arrow_base[0], arrow_base[1], direction[0] * 0.01, direction[1] * 0.01,
                          head_width=0.05, head_length=0.08, fc='r', ec='r', linewidth=0, length_includes_head=True)
            else:
              # Draw a quadratic Bezier curve with arrow
              midpoint = (node1 + node2) / 2
              control_point = midpoint * 0.3 + focus_point * 0.7 
              t = np.linspace(0, 1, 100)
              # Bezier curve formula: B(t) = (1-t)^2 * P0 + 2*(1-t)*t * P1 + t**2 * P2
              curve_x = (1-t)**2 * node1[0] + 2*(1-t)*t * control_point[0] + t**2 * node2[0]
              curve_y = (1-t)**2 * node1[1] + 2*(1-t)*t * control_point[1] + t**2 * node2[1]


              plt.plot(curve_x, curve_y, 'r-', linewidth=LINE_THICKNESS)


              end_point_idx = -2 
              arrow_point = np.array([curve_x[end_point_idx], curve_y[end_point_idx]])
              direction = np.array([curve_x[-1] - curve_x[end_point_idx], curve_y[-1] - curve_y[end_point_idx]])
              direction = direction / np.linalg.norm(direction)


              arrow_base = np.array([curve_x[-1], curve_y[-1]]) - direction * NODE_RADIUS * 1.4 


              plt.arrow(arrow_base[0], arrow_base[1], direction[0] * 0.01, direction[1] * 0.01, 
                        head_width=0.05, head_length=0.08, fc='r', ec='r', linewidth=0, length_includes_head=True)


    else: # Undirected graph
      title = 'Undirected Graph Representation'
      adj_matrix_undir = adj_matrix + adj_matrix.T
      adj_matrix_undir[adj_matrix_undir > 1] = 1


      for i in range(NUM_NODES):
        for j in range(i, NUM_NODES):
          if adj_matrix_undir[i, j] == 1:
            node1 = all_nodes[i]
            node2 = all_nodes[j]


            if i == j:
                x, y = node1
                r = NODE_RADIUS * 1.5


                theta = np.linspace(-np.pi/2, 3*np.pi/2, 100)
                circle_x = x + r * np.cos(theta)
                circle_y = y + r + r * np.sin(theta)
                plt.plot(circle_x, circle_y, 'r-', linewidth=LINE_THICKNESS)
            else:
              midpoint = (node1 + node2) / 2
              control_point = midpoint * 0.3 + focus_point * 0.7 
              t = np.linspace(0, 1, 100)
              # Bezier curve formula: B(t) = (1-t)^2 * P0 + 2*(1-t)*t * P1 + t**2 * P2
              curve_x = (1-t)**2 * node1[0] + 2*(1-t)*t * control_point[0] + t**2 * node2[0]
              curve_y = (1-t)**2 * node1[1] + 2*(1-t)*t * control_point[1] + t**2 * node2[1]
              plt.plot(curve_x, curve_y, 'r-', linewidth=LINE_THICKNESS)


    for i, (x, y) in enumerate(all_nodes):
        circle = plt.Circle((x, y), NODE_RADIUS, color='skyblue', zorder=5)
        plt.gca().add_patch(circle)
        plt.text(x, y, str(i), ha='center', va='center', color='black', fontsize=8, zorder=6) 


    plt.axis('off')


    plt.xlim(-0.2, 2.2)
    plt.ylim(-0.2, 2.2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)


    plt.show()
