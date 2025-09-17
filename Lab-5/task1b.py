#task 1b
task1b_input = open('input1B_3.txt','r')
task1b_output = open('output1B_3.txt','w')

def BFS(N, parent):
    graph = {}
    in_degree = [0] * (N + 1)

    for i in range(1, N + 1):
        graph[i] = []

    for U, V in parent:
        graph[U].append(V)
        in_degree[V] += 1

    queue = []
    for k in range(1, N + 1):
        if in_degree[k] == 0:
            queue.append(k)

    topo_bfs = []
    while queue:
        course = queue.pop(0)
        topo_bfs.append(course)
        for i in graph[course]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

    if len(topo_bfs) != N:
        s = "IMPOSSIBLE"
        task1b_output.write(s)
    else:
        s = ''
        for i in topo_bfs:
            s += str(i) + ' '
        #print(s)
        task1b_output.write(s)

N, M = map(int, task1b_input.readline().split())
Graph = [list(map(int, task1b_input.readline().split())) for i in range(M)]
print(Graph)
BFS(N, Graph)

task1b_input.close()
task1b_output.close()