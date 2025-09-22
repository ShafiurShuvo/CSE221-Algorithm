input = open('input.txt','r')
output = open('output.txt','w')

nodes, edges  = map(int, input.readline().split())
graph = {i:[] for i in range(nodes+1)}

for x in range(edges):
    n1, n2 = map(int, input.readline().split())
    graph[n1].append(n2)
print(graph)
source = int(input.readline())

queue = []
queue.append(source)
s = str(source) + ' '
level = [-1] * (nodes+1)
level[source] = 0

while queue != []:
    parent = queue.pop(0)
    for i in graph[parent]:
        queue.append(i)
        level[i] = int(level[parent]) + 1
        s += str(i) + ' '

print(s)
print(level)

destination = 13
x = f'in order to reach {destination} user has to move {level[destination]} floors from the source node {source}'
print(x)
output.write(s +'\n')
output.write(x)
input.close()
output.close()
