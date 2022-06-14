from hashlib import new


class Node(object):
  """Node in a linked list."""

  def __init__(self, data):
      self.data = data
      self.next = None

  def __repr__(self):
      return f"<Node object. Data: {self.data}; Next: {self.next.data if self.next else None}>"


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return f"<Linked List. Head: {self.head.data if self.head else None}; Tail: {self.tail.data if self.head else None}>"

    def append(self, data):
        """Append node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # Did list start as empty?
            self.tail.next = new_node

        self.tail = new_node

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            length += 1
        return length

    def print_list(self):
        """Print all items in the list."""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, data):
        """Does this data exist in our list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def remove(self, value):
        """Remove node with given value"""

        # If removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return

        # Removing something other than head
        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    # If removing last item, update .tail
                    self.tail = current
                return

            else:     # haven't found yet, keep traversing
                current = current.next



def word_shorten(list_of_words):
    shorter_list = list_of_words[1:]

    new_linked_list = LinkedList()

    for item in shorter_list:
        new_linked_list.append(item)
    
    return new_linked_list
        

kh_characters = ["Sora", "Riku", "Kairi", "Donald", "Goofy", "Sid"]


print(len(word_shorten(kh_characters)))
# print(len(LinkedList()))