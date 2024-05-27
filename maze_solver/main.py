from collections import deque

def read_mazes_from_file(file_path):
    mazes = {}
    current_maze = []
    current_label = None

    with open(file_path, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            if stripped_line.isupper() and len(stripped_line) == 1:
                if current_label:
                    mazes[current_label] = current_maze
                current_label = stripped_line
                current_maze = []
            else:
                current_maze.append(list(stripped_line.replace(' ', '')))
        
        if current_label:
            mazes[current_label] = current_maze

    return mazes

def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]

    start_x, start_y = None, None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start_x, start_y = i, j
                break
        if start_x is not None:
            break

    if start_x is None:
        return "No starting point found"

    queue = deque([(start_x, start_y, '')])
    visited = set((start_x, start_y))

    while queue:
        x, y, path = queue.popleft()

        if maze[x][y] == 'G':
            return path

        for dx, dy, direction in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != '#' and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, path + direction))

    return "No path found"

def find_paths_in_file(file_path):
    mazes = read_mazes_from_file(file_path)
    results = {}
    for label, maze in mazes.items():
        results[label] = find_path(maze)
    return results

file_path = "./input.txt"
results = find_paths_in_file(file_path)
space = " "
for label, path in results.items():
    print(f"{label}")
    if path != "No path found":
        
        print(f"S {' '.join(path)} G")
    else:
        print("No path found")
