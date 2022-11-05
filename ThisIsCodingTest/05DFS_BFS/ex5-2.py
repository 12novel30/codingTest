from collections import deque
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 나중에 온 애들부터
queue.reverse()
print(queue) # 먼저 온 애들부터