def find_all_paths(origin, current, path, visited, solutions):
    if len(path) == len(graph):  # If all nodes have been visited
        if path[-1] == origin:  # Check if the last node is the origin
            solutions.append(path[:])  # Store the path
        return

    min_weight = float('inf')
    min_neighbor = None

    for neighbor, weight in sorted(graph[current].items(), key=lambda x: x[1]):
        if visited[neighbor] == 0:
            min_weight = weight
            min_neighbor = neighbor
            break

    if min_neighbor is None:
        print("\033[91mNon-viable solution:\033[0m", path)
        return

    for neighbor, weight in sorted(graph[current].items(), key=lambda x: x[1]):
        if weight < min_weight and visited[neighbor] == 1:
            min_weight = weight
            min_neighbor = neighbor

    if min_neighbor is None:
        print("\033[91mNon-viable solution:\033[0m", path)
        return

    visited[min_neighbor] += 1
    path.append(min_neighbor)
    find_all_paths(origin, min_neighbor, path, visited, solutions)
    visited[min_neighbor] -= 1
    path.pop()


def calculate_total_value(path):
    total_value = 0
    path_with_weights = []
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        path_with_weights.extend([current_node, graph[current_node][next_node]])  # Add connection weight between nodes
        total_value += graph[current_node][next_node]  # Accumulate the weight of the connection
    # Add connection weight from last node to origin
    path_with_weights.extend([path[-1], graph[path[-1]][path[0]]])  # Add connection weight from last node to origin
    total_value += graph[path[-1]][path[0]]  # Accumulate the weight of the connection to origin
    return total_value, path_with_weights


def find_all_solutions():
    solutions = []
    for node in graph:
        path = [node]
        visited = {n: 0 for n in graph}  # Initialize visited count for each node
        visited[node] = 1  # Mark the starting node as visited
        find_all_paths(node, node, path, visited, solutions)
    return solutions


# Call the function to find all solutions
all_solutions = find_all_solutions()

# Print all solutions with total connection values
print("All solutions:")
for solution in all_solutions:
    total_value, path_with_weights = calculate_total_value(solution)
    if solution[-1] == solution[0]:
        print("\033[92mViable solution:\033[0m", path_with_weights, "Total Connection Value:", total_value)
    else:
        print("\033[91mNon-viable solution:\033[0m", path_with_weights, "Total Connection Value:", total_value)
