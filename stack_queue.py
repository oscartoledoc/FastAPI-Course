from collections import deque

######### deque is a double-ended queue (It's like a queue and a stack) #########
######### deque is more faster than list, because it is optimized to add and remove elements

# Creating a stack
# Stack is a LIFO (Last In First Out) data structure
# I can just move the last element added (It´s like a pile of books)
# Just I can use pop() to remove y push() to add the last added element
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3) 
print(stack.pop())  # Just I can use pop() to remove y push() to add → 3
print(stack)  # deque([1, 2])


# Creating a queue
# Queue is a FIFO (First In First Out) data structure
# I can just move the first element added (It´s like a line of people)
# I can use pop() to remove the last added element and popleft() to remove the first added element
# I can use append() to add the last added element and appendleft() to remove the first element added
queue = deque() 
queue.append(1)  # Encolar
queue.append(2)
queue.append(3)
print(queue.popleft())  # Desencolar → 1
print(queue.pop())
print(queue)  # deque([2, 3])

