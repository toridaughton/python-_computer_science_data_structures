class Node:

# Function to initialise the node object
    def __init__(self, data, next):
        self.data = data # Assign data
        self.next = next # Initialize next as null
        self.prev = None # Initialize prev as null


class Queue():
    """FIFO queue.

    Implemented as a linked list. This will be slower than
    using a Python list for small lists but when the list
    size is larger than ~5,000, it becomes faster to use,
    as it's expensive to pop items off the front of a Python
    list (this is a O(n) operation, whereas it's O(1) for
    a linked list.

    This is useful for studying how linked lists work but,
    should you want one in a real-world program, see the
    `collections.deque object` --- this is a
    doubly-linked lists, but it will perform excellently,
    given that it is implemented in C.
    """

    def __init__(self, inlist):
        self._tail = None
        self._length = len(inlist)

        prev = None
        for item in inlist[::-1]:
            node = Node(item, next=prev)
            if self._tail is None:
                self._tail = node
            prev = node
        self._head = prev

    def __repr__(self):
        if not self._head:
            return "<Queue (empty)>"
        else:
            return f"<Queue head={self._head.data} tail={self._tail.data} length={self._length}>"

    def enqueue(self, item):
        """Add item to end of queue."""

        self._length += 1
        node = Node(item)
        if self._tail:
            self._tail.next = node
            self._tail = node
        else:
            self._head = self._tail = node

    def dequeue(self):
        """Remove item from front of queue and return it."""

        if not self._head:
            raise QueueEmptyError()

        self._length -= 1
        node = self._head
        self._head = self._head.next

        if not self._head:
            self._tail = None

        return node.data

    def __iter__(self):
        """Allow iteration over list.

        __iter__ is a special method that, when defined,
        allows you to loop over a list, so you can say things
        like "for item in my_queue", and it will pop
        successive items off.
        """

        while True:
            try:
                yield self.dequeue()
            except QueueEmptyError:
                raise StopIteration

    def length(self):
        """Return length of queue."""

        return self._length

    def peek(self):
        """Return, but don't remove, item at front of queue."""

        if self.is_empty():
            return None

        return self._head.data

    def empty(self):
        """Empty queue."""

        self._tail = self._head = None
        self._length = 0

    def is_empty(self):
        """Is queue empty?"""

        return not bool(self._length)

    def head_swap(self, new_head):
        """This method swaps out the head item of the queue."""
        past_next = self._head.next
        self._head = Node(new_head, past_next)
        


def add_jobs(list_of_docs: str):
    job_queue = Queue(list_of_docs)
    
    return job_queue

orders = ["Tacos", "Nachos", "Enchilada", "Smothered Burrito", "Taco Salad", "Churros"]

waiting_orders = add_jobs(orders)

print(waiting_orders)

waiting_orders.head_swap("Taquito")

print(waiting_orders) # Not working correctly