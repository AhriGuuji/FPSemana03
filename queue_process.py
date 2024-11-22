from collections import deque
names=input()
queue=deque()
for i in names.split(" "):
    queue.appendleft(i)
print(queue)
while len(queue)>0:
    l=queue.pop()
    if 'a' in l:
        print(l)