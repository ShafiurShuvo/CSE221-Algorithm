#task7
task7_input = open('input7_1.txt', "r")
task7_output = open('output7_1.txt', "w")

N = int(task7_input.readline().strip())
edges = []
for i in range(N-1):
    u, v = [int(x) for x in task7_input.readline().strip().split()]
    edges.append((u, v))
print(edges)
print(N)
adj = [[] for i in range(N+1)]  # 1-based indexing
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    visited = [0] * (N+1)
    dist = [0] * (N+1)
    queue = [start]
    visited[start] = 1
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    max_dist = 0
    farthest = start
    for i in range(1, N+1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest = i
    return farthest, max_dist

u, dist = bfs(1)
v, length = bfs(u)

task7_output.write(f"{u} {v}\n")

task7_input.close()
task7_output.close()