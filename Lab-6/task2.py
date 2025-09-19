#task2
import math
from queue import PriorityQueue
task2_input = open('input2_3.txt','r')
task2_output = open('output2_3.txt','w')

nodes, edges = list(map(int,task2_input.readline().split()))

graph = {i: [] for i in range(1,nodes+1)}

for i in range(edges):
    u,v,w = list(map(int,task2_input.readline().split()))

    if graph[u] == 0:
        graph[u] = [(v,w)]
    else:
        graph[u].append((v,w))
print(graph)

Alice, Bob = list(map(int,task2_input.readline().split()))

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

path1 = shortest_path(Alice, graph, 0)
path2 = shortest_path(Bob, graph, 0)

node= None
total_time= math.inf

for t in range(len(path1)):

    if path2[t] != math.inf and path1[t] != math.inf:
        temp = max(path2[t], path1[t])

        if total_time > temp:
            node = t

            total_time = temp

if node != None:
    task2_output.write(f'Time {total_time}\n')
    task2_output.write(f'Node {node}\n')
else:
    task2_output.write('Impossible\n')

task2_input.close()
task2_output.close()