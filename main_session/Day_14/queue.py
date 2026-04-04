#Queue - Implement list as queue

#Enqueue - insert
queue = []
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)

print(queue)

#Dequeue

a = queue.pop(0)
print(queue)
b = queue.pop(0)
print(queue)

#Front
print(queue[0])

#isEmpty
print(len(queue)==0)