def draw_path(canvas, path, color="blue"):
    for point in path:
        canvas.create_rectangle(point[0]*10, point[1]*10, point[0]*10 + 10,
                                point[1]*10 + 10, fill=color, outline=color)

def visualize_process(canvas, open_list, closed_list, current_node):
    for node in open_list:
        canvas.create_rectangle(node.position[0]*10, node.position[1]*10,
                                node.position[0]*10 + 10, node.position[1]*10 + 10,
                                fill="green", outline="green")

    for node in closed_list:
        canvas.create_rectangle(node.position[0]*10, node.position[1]*10,
                                node.position[0]*10 + 10, node.position[1]*10 + 10,
                                fill="red", outline="red")

    if current_node:
        canvas.create_rectangle(current_node.position[0]*10, node.position[1]*10,
                                node.position[0]*10 + 10, node.position[1]*10 + 10,
                                fill="yellow", outline="yellow")
