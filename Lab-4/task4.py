#task4
task4_input = open('input4_5.txt',"r")
task4_output = open('output4_5.txt',"w")
graph = {}
num = 0
cities,roads = map(int,task4_input. readline().split())


for a in range(1,cities+1) :
    graph.update({a:[]})

for b in range(roads) :
    d = task4_input.readline().split()
    arr = [int(x) for x in d]

    temp= graph.get (int(arr[0]))
    temp.append (int(arr[1]))

print(arr)


for k,v in graph.items():
    visit = [k]
    store = [k]

    while store:
        t = store.pop(0)

        for x in graph[t]:

            if x == k:
                num = num+1
            if x not in visit:
                visit.append(x)

                store.append(x)

if num ==0:
    task4_output.write("NO")

else:
    task4_output.write("Yes")

task4_input.close()
task4_output.close()