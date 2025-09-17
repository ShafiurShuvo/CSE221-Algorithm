#task 2
from queue import PriorityQueue

task2_input = open('input2_1.txt','r')
task2_output = open('output2_1.txt','w')

def BFS(N, parent):
    graph = {}
    in_degree = [0] * (N + 1)

    for i in range(1, N + 1):
        graph[i] = []

    for A, B in parent:
        graph[A].append(B)
        in_degree[B] += 1

    queue = PriorityQueue()
    for k in range(1, N + 1):
        if in_degree[k] == 0:
            queue.put(k)

    lexicographical_order = []
    while not queue.empty():
        course = queue.get()
        lexicographical_order.append(course)
        for i in graph[course]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.put(i)
    if len(lexicographical_order) == N:
        return lexicographical_order
    else:
         return []

N, M = map(int, task2_input.readline().split())
Graph_ = [list(map(int, task2_input.readline().split())) for i in range(M)]

lexicographical_order = BFS(N, Graph_)
if lexicographical_order == []:
    s = "IMPOSSIBLE"
    #print(s)
    task2_output.write(s)
else:
    s = ''
    for i in lexicographical_order:
        s += str(i) + ' '

    #print(s)
    task2_output.write(s)

task2_input .close()
task2_output.close()