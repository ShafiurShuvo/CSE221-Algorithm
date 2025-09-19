#task1
import math
from queue import PriorityQueue
task1_input = open('input1_1.txt','r')
task1_output = open('output1_1.txt','w')

nodes, edges = list(map(int,task1_input.readline().split()))

graph = {i: [] for i in range(1,nodes+1)}

for i in range(edges):
    u,v,w = list(map(int,task1_input.readline().split()))

    if graph[u] == 0:
        graph[u] = [(v,w)]
    else:
        graph[u].append((v,w))

source = int(task1_input.readline())
# print(source)
# print(graph)
def shortest_path(source, graphs, c):
    distance = [math.inf] * (nodes+1)

    queue = PriorityQueue()
    queue.put((c,source))
    while not queue.empty():
        weight, source = queue.get()

        if distance[int(source)] > weight:
            distance[int(source)] = weight

            if graphs[int(source)] != 0:

                for i in graphs[int(source)]:
                    source, new_value =  i
                    queue.put((new_value + weight, source))


    return distance



x = shortest_path(source, graph, 0)
print(x)
for i in range(1 ,len(x)) :
    s = ''
    if x[i] != math.inf :
        s += str(x[i]) + ' '
        task1_output.write(s)
    else:
        task1_output.write("-1")
task1_input.close()
task1_output.close()