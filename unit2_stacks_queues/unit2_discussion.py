"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = []
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.stack.append(value) #adds value to the end of the stack, as last in you can remove it first when you need to
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty(): # if stack is empty, raises exception indicating the error.
            raise IndexError("Unable to remove. Stack is empty")
        return self.stack.pop() # removes the most recently added value

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty(): raise IndexError("Unable to peek. Stack is empty")
        return self.stack[-1] # returns the most recent value, without getting rid of it

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return not self.stack


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.queue.append(value) #adds value to the end of the queue, than we can pop() the first element
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty(): raise IndexError("Can't remove. Queue is empty") #without queue handling, programs crash when modifying an empty queue or stack
        return self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty(): raise IndexError("Can't return front value. Queue is empty")
        return self.queue[0] #Returns the first value of the queue, not the end

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return not self.queue


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal. \n")

    print("---Creating stack--- \n")

    demo_list = Stack()
    demo_list.push(10)
    print("Adding 10 to the stack")
    demo_list.push(20)
    print("Adding 20 at the end of the stack")
    print(f"stack: {demo_list.stack}")
    demo_list.push(30)
    print("Adding the rest of the stack, 30 and 40 to the stack...")
    demo_list.push(40)
    print(f"stack: {demo_list.stack}")
    print("Now that all items are added, I can start removing the last value first")
    demo_list.pop()
    print("Removing the last item from the stack")
    print(f"stack: {demo_list.stack}")
    print("40 is now gone from the stack")
    demo_list.pop()
    print("Removed 30 from the stack")
    demo_list.pop()
    print("Removed 20 from the stack")
    print(f"stack: {demo_list.stack}")
    demo_list.pop()
    print(f"stack: {demo_list.stack}")
    print("Removed 10 from the stack. Now if I pop an empty stack, I'll trigger my raise exception and get an IndexError")

    try:
        demo_list.pop()
    except IndexError as e:
        print(f"Exception raised: {e}")

    print("Now when peaking at an empty stack. Same error")
    try:
        demo_list.peek()
    except IndexError as e:
        print(f"Exception raised: {e}")

    print(f"\n ==Creating New stack == \n")

    edge_list = Stack()
    print("stack created")
    edge_list.push("Apple")
    print("Adding Apple to the stack, than popping it from the stack")
    edge_list.pop()
    print("running is_empty()")
    edge_list.is_empty()
    print("Is stack empty? ", edge_list.is_empty())
    print("Stack: ", edge_list.stack)



    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.\n")

    print("---Creating queue--- \n")

    demo_queue = Queue()
    print("Queue created")
    demo_queue.enqueue(10)
    print("Adding 10, 20, 30, 40 to the queue")
    demo_queue.enqueue(20)
    demo_queue.enqueue(30)
    demo_queue.enqueue(40)
    print(f'queue: {demo_queue.queue}')
    print("Now I can can remove items at the start of the queue, the first occurring item. For this, it's 10")
    demo_queue.dequeue()
    print(f"queue: {demo_queue.queue} \n Same thing as a stack when I try to remove from an empty queue \n removing items...")
    demo_queue.dequeue()
    demo_queue.dequeue()
    demo_queue.dequeue()
    print(f"queue: {demo_queue.queue}")

    try:
        demo_queue.dequeue()
    except IndexError as e:
        print(f"Exception raised: {e}")

    print("When trying to see the front value of an empty queue. Same error like stack")
    try:
        demo_queue.front()
    except IndexError as e:
        print(f"Exception raised: {e}")

    print(f"\n ==Creating New Queue == \n")

    car_queue = Queue()
    print("Car Queue created")
    car_queue.enqueue("Bugatti Chiron Super Sport 300+")
    print(f"Cars: {car_queue.queue}")
    print("Oh no! Your Bugatti Chiron Super Sport 300+ got picked up by the Hulk as a throwable in the battle for New York!")
    car_queue.dequeue()
    car_queue.is_empty()
    print(f"Is the car port, and your heart broken? {car_queue.is_empty()}")

if __name__ == "__main__":
    main()
