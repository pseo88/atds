#!/usr/bin/env python3

"""
atds.py
The module containing all of the data structures used in the Advanced Topics in CS course at Poly.
"""

__author__ = "Patrick Seo"
__version__ = "2024-02-15"

class Stack():
    """Describes a Stack that can be used with push and pop commands
    """
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)
    
    def pop(self):
        return self.st.pop()
    
    def peek(self):
        """Returns the item on the "top" of the list, as long as there's an item there.
        """
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return None
    
    def size(self):
        return len(self.st)

    def is_empty(self):
        return len(self.st) == 0
    
class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)
    
    def dequeue(self):
        return self.queue.pop()   

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[-1]
        else:
            return None
    
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue)
    
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
        
    def __repr__(self):
        return str(self.queue)
        
class Deque(object):
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.append(item)

    def add_rear(self, item):
        self.deque.insert(0, item)

    def remove_front(self):
        return self.deque.pop()

    def remove_rear(self):
        return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0
    
class Node(object):
    """Defines a node class to be used in an UnorderedList, coming soon.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
    
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def __repr__(self):
        return "Node[data=" + str(self.data) + ",next=" + str(self.next) + "]"
    
class UnorderedList(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        """Inserts a new node at the beginning of the list
        """
        temp_node = Node(data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def length(self):
        """Identifies the length of the list by going through the entire list.
        """
        node_count = 0
        current = self.head
        while current != None: 
            current = current.get_next()
            node_count += 1
        return node_count
    
    def search(self, data):
        """Returns True if the data is on the list.
        """
        current = self.head
        while current != None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False
    
    def remove(self, data):
        """Removes the first occurence of data on the list. Assumes that data *is* on the list.
        """
        current = self.head
        prev = None
        while (current != None and self.head != None):
            if current.get_data() == data:
                if (prev == None):
                    self.head = current.get_next()
                else:
                    prev.set_next(current.get_next())
            else:
                prev = current
            current = current.get_next()
        
    def append(self, data):
        current = self.head
        temp = Node(data)
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def insert(self, pos, data):
        current = self.head
        previous = None
        index = 0
        temp = Node(data)
        while index < pos:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp      
        else:
            previous.set_next(temp)
            temp.set_next(current)
    
    def index(self, item):
        index = 0
        if (self.head == None):
            return None
        current = self.head
        while (current != None):
            if (current.get_data() == item):
                break
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index
    def pop(self, i = -1):
        if self.head == None:
            return None
        if i == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif i == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:
            current = self.head
            previous = None
            position = 0
            while position < i:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result
    def __repr__(self):
        """Creates a representation of the list suitable for printing,debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        if result[-1] == ",":
            result = result[:-1] # remove trailing comma
        result = result + ",]"
        return result
    def is_empty(self):
        return self.head == None

class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack"""
        self.ul.add(item)
    
    def pop(self):
        return self.ul.pop()
    
    def peek(self):
        """Returns the item on the "top" of the list, as long as there's an item there.
        """
        num = self.stack.pop(0)
        self.stack.add(num)
        return num

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()
    
    def __repr__(self):
        return str(self.ul)


class HashTable(object):
    def __init__(self, size):
        self.keys = size * [None]
        self.data = size * [None]
        self.size = size

    def put(self, key, value):
        
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        if self.keys[hash_value] == key:
            self.data[hash_value] = value
        else:
            self.keys[hash_value] = key
            self.data[hash_value] = value
        
    def get(self, key):
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        if self.keys[hash_value] == key:
            return self.data[hash_value]
        else:
            return None
        
    def __str__(self):
        return "Keys:   " + str(self.keys) + "\n" + \
               "Values: " + str(self.data)
 
class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        
    def get_root_val(self):
        return self.val
    
    def set_root_val(self, val):
        self.val = val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def insert_left(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.left_child = self.left_child
        self.left_child = new_subtree
    
    def insert_right(self, val):
        new_subtree = BinaryTree(val)
        new_subtree.right_child = self.right_child
        self.right_child = new_subtree

    def __str__(self):
        return "BinaryTree[key=" + str(self.val) + \
               ",left_child=" + str(self.left_child) + \
               ",right_child=" + str(self.right_child) + "]"
    
def main():
    tests_passed = 0
    print("\nTEST: Creating HashTable(11)...")
    try:
        h = HashTable(11)
        tests_passed += 1
        print("SUCCESS. Table created.")
    except:
        print("FAIL. Table not created.")

    print("\nTEST: Using put function to store key-value pairs in table...")
    try:
        h.put(1, "a")
        h.put(6, "e")
        h.put(9, "f")
        h.put(12, "b")
        h.put(23, "c")
        tests_passed += 1
        print("SUCCESS. .put() method called with 5 values.")
    except:
        print("FAIL. Problem with .put() method.")

    print("\nTEST: Trying to print the current state of table:")
    try:
        print(h)
        print("Should look something like:")
        print("Keys:   [None, 1, 12, 23, None, None, 6, None, None, 9, None]")
        print("Values: [None, 'a', 'b', 'c', None, None, 'e', None, None, 'f', None]")
        tests_passed += 1
    except:
        print("FAIL. Couldn't print using __str__ or __repr__")

    print("\nTEST: Looking for original hash in table..")
    try:
        result = h.get(9)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "f":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision in table..")
    try:
        result = h.get(23)
        tests_passed += 1
        print("SUCCESS. .get() method called.")
        if result == "c":
            tests_passed += 1
            print("SUCCESS. Correct value returned.")
        else:
            print("FAIL. Incorrect value returned.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for original hash not in table..")
    try:
        result = h.get(14)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent value not found.")
        else:
            print("FAIL. Non-existent value found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nTEST: Looking for collision not in table..")
    try:
        result = h.get(45)
        if result == None:
            tests_passed += 1
            print("SUCCESS. Non-existent collision not found.")
        else:
            print("FAIL. Non-existent collision found.")
    except:
        print("FAIL. Problem with .get() method.")

    print("\nResults:")
    print(tests_passed,"/ 9 tests passed")

if __name__ == "__main__":
    main()