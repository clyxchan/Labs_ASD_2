def draw_graph(adj_matrix, directed):
    import numpy as np
    import matplotlib.pyplot as plt


    NODE_RADIUS = 0.05
    LINE_THICKNESS = 1.5


    NUM_NODES = adj_matrix.shape[0]


    center_node = np.array([[1, 1]])


    num_boundary_nodes = NUM_NODES - 1


    nodes_per_side = num_boundary_nodes // 4


    # Calculate the remainder nodes
    remainder_nodes = num_boundary_nodes % 4


    boundary_nodes = []


    # Distribute nodes to sides
    sides = [0, 1, 2, 3] # 0: bottom, 1: right, 2: top, 3: left
    side_node_counts = [nodes_per_side] * 4


    # Distribute remainder nodes
    for i in range(remainder_nodes):
      side_node_counts[i] += 1


    # Place nodes on each side
    for side, count in zip(sides, side_node_counts):
      if count > 0:
        # Calculate spacing between nodes (between 0.5 and 1.5)
        spacing = np.linspace(0.3, 1.7, count)


        if side == 0: # bottom side (y=0)
          boundary_nodes.extend([[x, 0] for x in spacing])
        elif side == 1: # right side (x=2)
          boundary_nodes.extend([[2, y] for y in spacing])
        elif side == 2: # top side (y=2)
          boundary_nodes.extend([[x, 2] for x in spacing])
        elif side == 3: # left side (x=0)
          boundary_nodes.extend([[0, y] for y in spacing])


    all_nodes = np.array(boundary_nodes)
    # Combine center and boundary nodes, if center node exists
    if NUM_NODES > 0:
      all_nodes = np.vstack((center_node, all_nodes))




    plt.figure(figsize=(8, 8)) # Increased figure size


    # Draw edges first
    focus_point = np.array([1, 1])


    if directed:
      title = 'Directed Graph Representation'
      for i in range(NUM_NODES):
        for j in range(NUM_NODES):
          if adj_matrix[i, j] == 1:
            node1 = all_nodes[i]
            node2 = all_nodes[j]


            if i == 0 or j == 0: # If either node is the center node (index 0)
              plt.arrow(node1[0], node1[1], node2[0] - node1[0], node2[1] - node1[1],
                        head_width=0.05, head_length=0.08, fc='k', ec='k', linewidth=LINE_THICKNESS, length_includes_head=True)
            else:
              # Draw a quadratic Bezier curve with arrow
              midpoint = (node1 + node2) / 2
              control_point = midpoint * 0.3 + focus_point * 0.7 # Adjust weights for desired curve shape


              t = np.linspace(0, 1, 100)
              # Bezier curve formula: B(t) = (1-t)^2 * P0 + 2*(1-t)*t * P1 + t^2 * P2
              curve_x = (1-t)**2 * node1[0] + 2*(1-t)*t * control_point[0] + t**2 * node2[0]
              curve_y = (1-t)**2 * node1[1] + 2*(1-t)*t * control_point[1] + t**2 * node2[1]


              plt.plot(curve_x, curve_y, 'r-', linewidth=LINE_THICKNESS)


              # Add arrow head near the end of the curve
              # Find the position and direction at the end of the curve
              end_point_idx = -2 # Get a point near the end
              arrow_point = np.array([curve_x[end_point_idx], curve_y[end_point_idx]])
              direction = np.array([curve_x[-1] - curve_x[end_point_idx], curve_y[-1] - curve_y[end_point_idx]])
              direction = direction / np.linalg.norm(direction) # Normalize direction vector


              # Position the arrow head slightly before the end point
              arrow_base = np.array([curve_x[-1], curve_y[-1]]) - direction * NODE_RADIUS * 1.4 
              plt.arrow(arrow_base[0], arrow_base[1], direction[0] * 0.01, direction[1] * 0.01, # Draw a small arrow pointing in the direction
                        head_width=0.05, head_length=0.08, fc='r', ec='r', linewidth=0, length_includes_head=True)


    else: # Undirected graph
      title = 'Undirected Graph Representation'
      adj_matrix_undir = adj_matrix + adj_matrix.T
      adj_matrix_undir[adj_matrix_undir > 1] = 1


      for i in range(NUM_NODES):
        for j in range(i + 1, NUM_NODES): # Iterate through the upper triangle to avoid duplicate lines
          if adj_matrix_undir[i, j] == 1:
            node1 = all_nodes[i]
            node2 = all_nodes[j]


            if i == 0 or j == 0: # If either node is the center node (index 0)
              plt.plot([node1[0], node2[0]], [node1[1], node2[1]], 'k-', linewidth=LINE_THICKNESS)
            else:
              # Draw a quadratic Bezier curve
              midpoint = (node1 + node2) / 2
              control_point = midpoint * 0.3 + focus_point * 0.7 
              t = np.linspace(0, 1, 100)


              curve_x = (1-t)**2 * node1[0] + 2*(1-t)*t * control_point[0] + t**2 * node2[0]
              curve_y = (1-t)**2 * node1[1] + 2*(1-t)*t * control_point[1] + t**2 * node2[1]
              plt.plot(curve_x, curve_y, 'r-', linewidth=LINE_THICKNESS)




    # Draw nodes as circles with numbers
    for i, (x, y) in enumerate(all_nodes):
        circle = plt.Circle((x, y), NODE_RADIUS, color='skyblue', zorder=5) 
        plt.gca().add_patch(circle)
        plt.text(x, y, str(i), ha='center', va='center', color='black', fontsize=8, zorder=6) 
     # Remove axis
    plt.axis('off')
    # Set plot limits and aspect ratio
    plt.xlim(-0.2, 2.2)
    plt.ylim(-0.2, 2.2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)


    plt.show()
