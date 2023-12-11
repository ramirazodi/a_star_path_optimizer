from visualization import draw_path, visualize_process

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic distance to end node
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

def astar(grid, start, end, canvas=None, visualize=False):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []
    open_list.append(start_node)

    iteration_count = 0
    update_frequency = 10  # Adjust this value as needed

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent

            if visualize and canvas:
                draw_path(canvas, path)
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # Ensure within grid bounds
            if node_position[0] > (len(grid[0]) - 1) \
                    or node_position[0] < 0 \
                    or node_position[1] > (len(grid) - 1)\
                    or node_position[1] < 0:
                continue

            # Check for barriers
            if grid[node_position[1]][node_position[0]] != 0:
                continue

            new_node = Node(current_node, node_position)
            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) \
                      + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if add_to_open(open_list, child):
                open_list.append(child)

            iteration_count += 1
            if visualize and canvas and iteration_count % update_frequency == 0:
                visualize_process(canvas, open_list, closed_list, current_node)
                canvas.update()

    return None

def add_to_open(open_list, child):
    for node in open_list:
        if child == node and child.g > node.g:
            return False
    return True
