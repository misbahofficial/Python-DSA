# Demonstration of Stack data structure with Python
# Stack uses LIFO (Last in First Out) order.

# Adding element to a list at the end

stack = []
stack.append(2)
stack.append(3)
stack.append(5)

# print(stack) --> [2, 3, 5]

# Removing element from the end of a stack

stack.pop()
stack.pop()

# print(stack) --> [2]

# Implementing stack using Collection module
import collections

# using deque

stack = collections.deque()
# print(stack)

# Appending items to the end of the stack

stack.append(7)
stack.append(11)
stack.append(13)
# print(stack)

# Removing elements from the end of the stack

stack.pop()
# print(stack)

# Appending to the left
stack.appendleft(5)
# print(stack)

# Removing all elements from a stack
# stack.clear()
# print(stack)

# Removing a specific element from a stack
stack.remove(5)
# print(stack)

# Reversing the stack in-place
stack.reverse()
# print(stack)

# Inserting an item to a stack in a specific index
# first argument is the index at which you wanna insert and the 2nd argument is the actual value
stack.insert(0, 34)
# print(stack)

# For more reference, visit the official docs --> https://docs.python.org/3/library/collections.html#collections.deque.copy











