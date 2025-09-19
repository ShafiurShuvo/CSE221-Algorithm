#task 3
import math
from queue import PriorityQueue

task3_input = open('input3_1.txt', 'r')
task3_output = open('output3_1.txt', 'w')

nodes, edges = list(map(int, task3_input.readline().split()))
source = 1
graph = {i: [] for i in range(0, nodes + 1)}

for i in range(edges):
    u,v,w = list(map(int, task3_input.readline().split()))

    if not graph[u]:
        graph[u] = [(v,w)]
    else:
        graph[u].append((v,w))
print(graph)

def safest_path(graph, source):
    list_1 = []
    temp = [math.inf] * (nodes + 1)

    temp[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))

    while not queue.empty():
        store = queue.get()
        list_1.append(store[1])
        print(store[1])

        if store[0] < temp[store[1]]:
            temp[store[1]] = store[0]

        for d in graph[store[1]]:
            edges = max(store[0], d[1])

            if d[0] not in list_1:
                queue.put((edges, d[0]))

    return temp[-1]


result = safest_path(graph, source)
task3_output.write(str(result))

task3_input.close()
task3_output.close()