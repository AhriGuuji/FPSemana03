from collections import deque
stack = deque()
numbers = input()
for i in numbers.split(" "):
        stack.append(int(i))
print(stack)
while len(stack)>0:
    n=stack.pop() * 2
    print(n)