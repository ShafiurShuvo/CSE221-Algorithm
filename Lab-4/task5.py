#task5
task4_input = open('input5_5.txt',"r")
task4_output = open('output5_5.txt',"w")

cities,roads,dest= task4_input.readline().strip().split(" ")
uv = [0]* (int(cities) +1)

visited= []
queue = []
graph = {}
dest = int(dest)

for a in range (int(roads)) :
  k = [int(x) for x in task4_input.readline().strip().split(' ')]

  if uv[k[0]] != 0 :
    uv[k[0]].append(k[1])

  else:
    uv[k[0]]=[k[1]]

  if uv[k[1]] != 0:
    uv[k[1]].append(k[0])

  else:
    uv[k[1]]= [k[0]]

# print(k)
for b in range(int(cities)+1) :
  graph[b]= uv[b]

def bfs(visited, graph, dest, node) :

  nod= [0]* (int(cities) +1)
  time_step = [0]* (int(cities) +1)

  visited.append(node)
  queue.append(node)
  while len(queue)!= 0 :
    s = queue.pop(0)
    for i in uv[s] :

      if i not in visited:
        time_step[i]= time_step[s]+1
        nod[i]= s

        visited.append(i)
        queue.append(i)

  task4_output.write(f"Time:{time_step[dest]}\n")
  var= str(dest)
  for task4_input in range (time_step[dest]) :
    var= str(nod[dest])+" "+var
    dest= nod[dest]

  task4_output.write(f"shortest path:{var}")


bfs(visited,graph,dest,1)
task4_input.close()
task4_output.close()