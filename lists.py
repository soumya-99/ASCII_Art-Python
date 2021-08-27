# stack = [1, 4, 6, 2, 8]

# stack.append(20)
# print(stack)
# stack.pop()
# print(stack)

from collections import deque
queue = deque([])
queue.append(1)
queue.append(3)
queue.append(5)
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)