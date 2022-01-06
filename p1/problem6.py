class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def get_head(self):
        return self.head

# Map for storing entries in a linked list. A.
class Map:
    def __init__(self):
        self.map = dict()

    # For this implementation, there is no value stored per key other than an indication 
    # that the key exists in the map.
    def insert(self, key):
        entry = self.get(key)
        if entry:
            return
        else:
            self.map[key] = 1

    def get(self, key):
        return self.map.get(key)

    def get_map(self):
        return self.map
    
    def remove(self, key):
        if self.get(key):
            del self.map[key]
    
    # For debugging Map.
    def __repr__(self):
        string = "Hash Map: \n"
        for key, value in self.map.items():
            string += str(key) + ': ' + str(value) + '\n'
        return string

# Return the union of two linked lists. Assumes that in the union of two linked lists, 
# only unique values are desired.
def union(llist_1, llist_2):
    # Iterates through each node in the first linked list, adding it to the new linked 
    # list if it has not already been added. Uses map to quickly determine if a value has
    # already been added to the new linked list. This does not allow duplicate values.
    node = llist_1.get_head()
    map = Map()
    new_llist = LinkedList()
    while node:
        entry = map.get(node.get_value())
        if not entry:
            map.insert(node.get_value())
            new_llist.append(Node(node.get_value()))
        node = node.get_next()

    # Iterates through each node in the second linked list, adding it to the new linked 
    # list if it has not already been added. Uses map to quickly determine if a value has
    # already been added to the new linked list. This does not allow duplicate values.
    node = llist_2.get_head()
    while node:
        entry = map.get(node.get_value())
        if not entry:
            map.insert(node.get_value())
            new_llist.append(Node(node.get_value()))
        node = node.get_next()
    
    if new_llist.size():
        return new_llist
    else:
        return None

# Return the intersection of two linked lists. Assumes that in the union of two linked 
# lists, only unique values are desired.
def intersection(llist_1, llist_2):
    # Iterates through each node in the first linked list, adding it to a map.
    node = llist_1.get_head()
    map = Map()
    while node:
        map.insert(node.get_value())
        node = node.get_next()

    # Iterates through each node in the second linked list, adding it to the new linked 
    # list if it is present in the map. A key in the map is removed after being added to 
    # new linked list to prevent duplicate values.
    new_llist = LinkedList()
    node = llist_2.get_head()
    while node:
        entry = map.get(node.get_value())
        if entry:
            new_llist.append(Node(node.get_value()))
            map.remove(node.get_value())
        node = node.get_next()

    #  If there is no intersection betwee the linked lists return None.
    if new_llist.size():
        return new_llist
    else:
        return None

# Both intersection and union have an O(n) run time where n is the cumulative size of 
# both input lists. This is the case because looking through each linked list takes O(n);
# get, remove, and insert operations on the maps take O(1), and inserting into a linked 
# list takes O(1). The highest order operation takes O(n), hence the runtime of these
# processes are O(n).

# Test case 1
print("\nTest 1:")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) 
# solution = [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print (intersection(linked_list_1,linked_list_2)) 
# solution = [4, 6, 21]

# Test case 2
print("\nTest 2:")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) 
# solution = [3, 2 , 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
print (intersection(linked_list_3,linked_list_4)) 
# solution = None

# Test case 3
print("\nTest 3:")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) 
# solution = [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print (intersection(linked_list_1,linked_list_2)) 
# solution = [4, 6, 21]