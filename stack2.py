# Creating a stack data structures
# Stack follows Last in First out criteria

class Stack:
    def __init__(self):
        self.stack = []

    def display(self):
        print(self.stack)

    def add_item(self, item):
        self.stack.append(item)

    def remove_item(self):
        self.stack.pop()

    def insert_item(self, index, item):
        self.stack.insert(index, item)

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    # creating an instance of Stack class
    stack = Stack()
    stack.add_item(10)
    stack.add_item(20)
    stack.add_item(30)
    stack.add_item(40)
    stack.remove_item()

    print(stack)
    print(stack.size())
