#task3
task3_input = open(file='input3_4.txt', mode='r')
task3_output = open(file='output3_4.txt', mode='w')

LIST1 = task3_input.readline().strip().split(" ")
vertices = int(LIST1[0])
edge  = int(LIST1[1])

graph= {}

for i in range(edge):
   u, v = map(int,task3_input.readline().split())

   if u not in graph :
      graph[u] = []
   graph[u].append(v)


   if v not in graph :
      graph[v] = []
   graph[v].append(u)

def dfs_traversal(graph, vertices, visited=None):
   if visited is None:
      visited = set()

   visited.add(vertices)
   dfs.append(vertices)
   for i in graph[vertices]:
      if i not in visited:
        dfs_traversal(graph , i , visited)

dfs = []
dfs_traversal(graph,1)
task3_output.write(' '.join(map(str, dfs)))

task3_input.close()
task3_output.close()