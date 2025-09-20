#task1
task1_input = open('input1_3.txt',"r")
task1_output = open('output1_3.txt',"w")

num_of_tasks = int(task1_input.readline())
list1 = []
final_list = []

for i in range(num_of_tasks) :
    start, end = map(int, task1_input.readline().split())

    list1.append((start, end))
print(list1)

for i in range(0, len(list1)):
    for j in range(0, len(list1)-i-1):
        if (list1[j][1] > list1[j + 1][1]):
            temp = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = temp

# list1.sort(key = sec_element)
print(list1)
end_time = -1
for t in list1 :

    if t[0] >= end_time :

      final_list.append(t)
      end_time = t[1]

print(final_list)

task1_output.write(str(len(final_list)) + "\n")
for t in final_list:
  task1_output.write(f'{t[0]} {t[1]}\n')
task1_input.close()
task1_output.close()