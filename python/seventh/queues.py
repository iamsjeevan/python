class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed '{item}' to the stack.")

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek into an empty stack.")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Current stack:")
        print(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued '{item}' to the queue.")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek into an empty queue.")
        return self.items[0]

    def size(self):
        return len(self.items)

    def display(self):
        print("Current queue:")
        print(self.items)


# Testing the Stack and Queue classes
def test_stack():
    print("Testing Stack operations:")
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()

    print(f"Peeked: {stack.peek()}")
    print(f"Popped: {stack.pop()}")
    stack.display()

    print(f"Size of stack: {stack.size()}")

    try:
        print(f"Popped: {stack.pop()}")
        print(f"Popped: {stack.pop()}")
    except IndexError as e:
        print(f"Error: {e}")

    stack.display()


def test_queue():
    print("\nTesting Queue operations:")
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()

    print(f"Peeked: {queue.peek()}")
    print(f"Dequeued: {queue.dequeue()}")
    queue.display()

    print(f"Size of queue: {queue.size()}")

    try:
        print(f"Dequeued: {queue.dequeue()}")
        print(f"Dequeued: {queue.dequeue()}")
    except IndexError as e:
        print(f"Error: {e}")

    queue.display()


def main():
    test_stack()
    test_queue()


if __name__ == "__main__":
    main()
