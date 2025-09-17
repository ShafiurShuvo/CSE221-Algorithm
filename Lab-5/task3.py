#task 3
task3_input = open('input3_1.txt','r')
task3_output = open('output3_1.txt','w')

def dfs_1(node, graph, visited, stack):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs_1(i, graph, visited, stack)
    stack.append(node)

def dfs_2(node, graph, visited, scc):
    visited[node] = True
    scc.append(node)
    for j in graph[node]:
        if not visited[j]:
            dfs_2(j, graph, visited, scc)

def kosaraju(N, graph):
    visited = [False] * (N + 1)
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:
            dfs_1(i, graph, visited, stack)

    transpose_graph = {i:[] for i in range(1, N + 1)}
    for j in range(1, N + 1):
        for k in graph[j]:
            transpose_graph[k].append(j)

    visited = [False] * (N + 1)
    list_of_scc = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_2(node, transpose_graph, visited, scc)
            list_of_scc.append(scc)

    return list_of_scc


N, M = map(int, task3_input.readline().split())
graph = {i: [] for i in range(1, N + 1)}
for i in range(M):
    u, v = map(int, task3_input.readline().split())
    graph[u].append(v)

SCC = kosaraju(N, graph)

for i in SCC:
    s = " ".join(map(str, i))
    task3_output.write(s + "\n")

task3_input.close()
task3_output.close()