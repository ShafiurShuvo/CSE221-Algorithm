#task1a
task1_input = open('input1A_2.txt','r')
task1_output = open('output1A_2.txt','w')

def dfs(node, graph, visited, stack, in_cycle):
    visited[node] = True
    in_cycle[node] = True
    for i in graph[node]:
        if in_cycle[i]:
            return True
        if not visited[i]:
            if dfs(i, graph, visited, stack, in_cycle):
                return True
    in_cycle[node] = False
    stack.append(node)
    return False

def find_order_dfs(N, parent):
    graph = {i: [] for i in range(1, N + 1)}
    for U, V in parent:
        graph[U].append(V)

    visited = [False] * (N + 1)
    in_cycle = [False] * (N + 1)
    stack = []

    for i in range(1, N + 1):
        if not visited[i]:
            if dfs(i, graph, visited, stack, in_cycle):
                return []

    return stack[::-1]


N, M = map(int, task1_input.readline().split())
parent = [list(map(int, task1_input.readline().split())) for i in range(M)]


result = find_order_dfs(N, parent)

if result == []:
    s = "IMPOSSIBLE"
    #print(s)
    task1_output.write(s)
else:
    s = ''
    for i in result:
        s += str(i) + ' '

    #print(s)
    task1_output.write(s)

task1_input.close()
task1_output.close()