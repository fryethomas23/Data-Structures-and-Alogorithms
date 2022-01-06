
# Double linked list node points to previous and next node
class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
    
    def get_prev(self):
        return self.prev
    
    def get_next(self):
        return self.next

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    # __repr__ method for debugging purposes
    def __repr__(self):
        string = "node: " + str(self.get_data())
        return string
            
# Double linked list allows nodes to point to previous and next node. This allows a
# node to be to the end of the linked list because the node before and after a node 
# are known and can be linked together in O(1).
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size
    
    # Adds a new node to the end of the linked list
    def push(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.size += 1
            return node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node
            self.size += 1
            return node
    
    # Moves a node to the end of the list and connects the created void.
    def move_to_end(self, node):
        # If node is at the head, moves head to next node unless the head is the only node
        # in this case, it does nothing.
        if node == self.head and node.get_next():
            self.head = node.get_next()
        elif node == self.head:
            return
        
        # Removes node from linked list and connects the nodes on each side of the gap.
        if not node.prev and not node.next:
            return
        elif node.prev and not node.next:
            node.prev.set_next(node.get_next())
        elif not node.prev and node.next:
            node.next.set_prev(node.get_prev())
        else:
            node.prev.set_next(node.get_next())
            node.next.set_prev(node.get_prev())

        # Clears node connections and pushes onto the tail.
        node.set_prev(None)
        node.set_next(None)
        self.push(node)
    
    # Removes the head node and sets the next node as the head.
    def pop_head(self):
        node = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return node

    # __repr__ method for debugging purposes
    def __repr__(self):
        string = "Linked List: \n"
        node = self.head
        while node:
            string += repr(node) + '\n'
            node = node.get_next()
        return string

# Hash map stores a value based on a key. Inputs are expected to be small real numbers
class HashMap:
    def __init__(self):
        self.map = dict()
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, key, value):
        self.map[key] = value
        self.size +=1

    def get(self, key):
        return self.map.get(key)

    def remove(self, key):
        del self.map[key]
        self.size -= 1 
    
    # __repr__ method for debugging purposes
    def __repr__(self):
        string = "Hash Map: \n"
        for key, value in self.map.items():
            string += str(key) + ': ' + str(value) + '\n'
        return string

# Cache utilizes a double linked list to keep track of the order in which values have
# been used and a hash map to allow for quick access to nodes in the linked list. 
# A capacity limit as set, meaning when the cache reaches its limit, the least 
# recently used item is removed
class LRU_Cache(object):
    def __init__(self, capacity=5):
        # Initialize class variables
        self.linked_list = DoubleLinkedList()
        self.hash_map = HashMap()
        self.size = self.hash_map.size
        self.max_size = capacity
    
    # Checks to see if item is in the cache using provided key. If it is, move it to 
    # the most recently used position of the linked list (the tail) and return value.
    # If it isn't in the cache return -1.
    def get(self, key):
        node = self.hash_map.get(key)
        if not node:
            return -1
        else:
            self.linked_list.move_to_end(node)
            return node.get_data()[1]

    # Add an item to the cache. 
    def set(self, key, value):
        # If cache is at capacity, remove the least recently used item.
        if self.size == self.max_size:
            self._remove_oldest()

        node = self.hash_map.get(key)
        # If value is already in the cache, update the value and move the node to 
        # the most recently used position of the linkend list (the tail).
        if node:
            node.set_value([key, value])
            self.linked_list.move_to_end(node)
        # If the value isn't in the cache, add it to the cache and put it at the 
        # most recently used position of the linkend list (the tail).
        else:
            new_node = Node([key, value])
            self.hash_map.insert(key, new_node)
            self.linked_list.push(new_node)
            self.size = self.hash_map.get_size()
    
    # Gets the least recently used entry from the linked list (the head) and removes 
    # it from the cache
    def _remove_oldest(self):    
        node = self.linked_list.pop_head()
        key = node.get_data()[0]
        self.hash_map.remove(key)
        
    # __repr__ method for debugging purposes
    def __repr__(self):
        string = ('\n*Oldest on top*\n' + repr(self.linked_list) +'\n' + 
            repr(self.hash_map) + '\nSize: ' + str(self.size) + 
            '\n_______________________________________________')
        return string


# Test 1
print("Test 1")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print('Output of get(1): ', our_cache.get(1))   # returns 1
print('Output of get(2): ', our_cache.get(2))   # returns 2
print('Output of get(9): ', our_cache.get(9))   # returns -1 because 9 is not present 
                                                # in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('Output of get(3): ', our_cache.get(3))   # returns -1 because the cache reached 
                                                # it's capacity and 3 was the least 
                                                # recently used entry.

# print(our_cache)

# Test 2
print("Test 2")
our_cache2 = LRU_Cache(5)

our_cache2.set(1, 1)
our_cache2.set(2, 2)
our_cache2.set(3, 3)
our_cache2.set(4, 4)
our_cache2.set(5, 5) 

print('Output of get(1): ', our_cache2.get(1))  # returns 1
our_cache2.set(6, 6)
print('Output of get(3): ', our_cache2.get(3))  # returns -1 because the cache reached   
                                                # it's capacity and 3 was the least  
                                                # recently used entry.
print('Output of get(1): ', our_cache2.get(1))  # returns 1 because when 1 was gotten
                                                # earlier, this moved it to the most 
                                                # recently used position meaning it
                                                # is no longer the next up for 
                                                # deletion
# print(our_cache2)

# Test 3
print("Test 3")
our_cache3 = LRU_Cache(5)

our_cache3.set(1, 1)
our_cache3.set(2, 2)
our_cache3.set(3, 3)
our_cache3.set(4, 4)
our_cache3.set(5, 5) 
our_cache3.set(6, 6)

print('Output of get(6): ', our_cache3.get(6))  # returns 6 because it was successful 
                                                # added to the linked list after 
                                                # reaching capacity
print('Output of get(1): ', our_cache3.get(1))  # returns -1 because 1 is not present 
                                                # in the cache
# print(our_cache3)