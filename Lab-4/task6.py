#task6
task6_input = open('input6_2.txt', 'r')
task6_output = open('output6_2.txt', 'w')

R, H = [int(x) for x in task6_input.readline().strip().split()]

grid = []
for i in range(R):
    grid.append(list(task6_input.readline().strip()))

visited = []
for i in range(R):
    visited.append([0]*H)

# Directions: up, down, left, right
dr = [-1, 1, 0, 0] 
dc = [0, 0, -1, 1]  

def bfs(sr, sc):    # sr, sc = starting row, starting column
    queue = []
    queue.append((sr, sc))
    visited[sr][sc] = 1
    count = 1 if grid[sr][sc] == 'D' else 0

    front = 0
    while front < len(queue):
        r,c = queue[front]    # r = row, c = column
        front += 1
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]  # nr, nc = neighbour row, nrighbour column
            if nr >= 0 and nr < R and nc >= 0 and nc < H:
                if visited[nr][nc] == 0 and grid[nr][nc] != '#':
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                    if grid[nr][nc] == 'D':
                        count += 1
    return count

max_diamonds = 0

# starting from every unvisited non-obstacle cell
for i in range(R):
    for j in range(H):
        if grid[i][j]!='#' and visited[i][j] == 0:
            diamonds = bfs(i, j)
            if diamonds > max_diamonds:
                max_diamonds = diamonds

task6_output.write(f"{max_diamonds}\n")
task6_input.close()
task6_output.close()