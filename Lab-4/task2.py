#task2
task2_input = open('input2_4.txt', 'r')
task2_output = open('output2_4.txt', 'w')
vertices, edge =  map(int,task2_input.readline().split())
graph = {}

for i in range(edge):
    u, v = map(int, task2_input.readline().split())

    if u not in graph:
        graph[u] = []
    graph[u].append(v)

    if v not in graph:
        graph[v] = []
    graph[v].append(u)
def bfs_traversal(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    bfs = []

    while queue:
        vertices = queue.pop(0)
        bfs.append(vertices)

        for i in graph[vertices]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    return bfs

bfs_output = bfs_traversal(graph, 1)
task2_output.write(" ".join(map(str,bfs_output)))

task2_input.close()
task2_output.close()