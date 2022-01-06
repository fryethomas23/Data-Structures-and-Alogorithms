import sys
from collections import deque

# Stores data and points to children nodes when used in a heap.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    def get_data(self):
        return self.data

    def set_data(self):
        return self.data
    
    def get_frequency(self):
        return self.data[0]
    
    def get_letter(self):
        try:
            return self.data[1]
        except IndexError:
            return -1

    # For debugging Node. 
    def __repr__(self):
        return f"Node({self.get_data()})"

# For printing nodes in a heap
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    # For debugging Queue.
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

# Array implementation of a minimum heap used as a priority queue
class MinHeap:
    def __init__(self):
        self.heap = list()
        self.size = 0

    # Inserts node at the end of the head and then ensures that each parent node 
    # is greater than its children nodes.
    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        
        if len(self.heap) <= 1:
            return

        # Getting most recently inserted node and it's parent
        child_index = len(self.heap) - 1
        child_node = self.heap[child_index]
        parent_index = (child_index-1)//2
        parent_node = self.heap[parent_index]

        # Loop for checking if the child node is smaller than the parent. If so,
        # the nodes are switched, and the process is repeated for the new parent
        # and its parent. If not, the function returns.
        while True:
            if child_node.get_frequency() < parent_node.get_frequency():
                self.heap[parent_index] = child_node
                self.heap[child_index] = parent_node

                if parent_index == 0:
                    return

                child_index = parent_index
                child_node = self.heap[child_index]
                parent_index = child_index//2
                parent_node = self.heap[parent_index]
            else:
                return

    # Removes the minimum item in the heap (the first item in the list).
    def pop_min(self):
        # The last node becomes the first node, and the last node is removed.
        min_node = self.get_min()
        if not min_node:
            return
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        if self.size == 0:
            return min_node

        # Loop for checking if the new first node is smaller than than it's children. 
        # If not, the first node is switched with the smaller child node. The process 
        # is repeated for the new child node and its children until all child nodes are 
        # again smaller than their parent.
        parent, parent_index, left, left_index, right, right_index = (
            self.get_node_family(0)
        )
        
        while True:
            # If there is a left and a right node, and one is smaller than the parent,
            # the parent and the child are swapped and the process begins again with
            # the child as the parent. If the child nodes are not smaller than the 
            # parent, the heap sorted correctly and returns.
            if left and right:
                if (left.get_frequency() < parent.get_frequency() and 
                    left.get_frequency() <= right.get_frequency()):

                    self.heap[parent_index] = left
                    self.heap[left_index] = parent

                    parent, parent_index, left, left_index, right, right_index = (
                        self.get_node_family(left_index)
                    )

                elif right.get_frequency() < parent.get_frequency():
                    self.heap[parent_index] = right
                    self.heap[right_index] = parent

                    parent, parent_index, left, left_index, right, right_index = (
                        self.get_node_family(right_index)
                    )
                else:
                    return min_node

            # If there is only a left node, and it is smaller than the parent,
            # the parent and the child are swapped and the process begins again with
            # the child as the parent. If it is not smaller than the parent, the heap
            # sorted correctly and returns.
            elif left and not right:
                if left.get_frequency() < parent.get_frequency():

                    self.heap[parent_index] = left
                    self.heap[left_index] = parent

                    parent, parent_index, left, left_index, right, right_index = (
                        self.get_node_family(left_index)
                    )
                else:
                    return min_node

            # If there is only a right node, and it is smaller than the parent,
            # the parent and the child are swapped and the process begins again with
            # the child as the parent. If it is not smaller than the parent, the heap
            # sorted correctly and returns.
            elif right and not left:
                if right.get_frequency() < parent.get_frequency():

                    self.heap[parent_index] = right
                    self.heap[right_index] = parent

                    parent, parent_index, left, left_index, right, right_index = (
                        self.get_node_family(right_index)
                    )
                else:
                    return min_node
            # If there no children nodes, the heap is ordered correctly.
            else:
                return min_node
    
    # Gets the node and the input index and the associated children and child indexes.
    def get_node_family(self, node_index):
        node = self.heap[node_index]
        left_child_index = 2*node_index + 1
        if len(self.heap) > left_child_index:
            left_child_node = self.heap[left_child_index]
        else: 
            left_child_node = None
        
        right_child_index = 2*node_index + 2
        if len(self.heap) > right_child_index:
            right_child_node = self.heap[right_child_index]
        else:
            right_child_node = None
        
        return (node, 
            node_index, 
            left_child_node, 
            left_child_index, 
            right_child_node, 
            right_child_index
        )

    # Recursively removes the smalles two nodes and makes them the children of 
    # a new node that is the sum of their two values. Then it inserts the new 
    # parent node back into the heap. The process ends when there is one node 
    # left in the heap.
    def merge_nodes(self):
        if self.size <= 1:
            return self.get_min()

        node1 = self.pop_min()
        node2 = self.pop_min()
        new_node = Node([node1.get_frequency() + node2.get_frequency()])

        new_node.set_left_child(node1)
        new_node.set_right_child(node2)
        self.insert(new_node)

        self.merge_nodes()
        
        return self.get_min()

    def get_min(self):
        if self.heap:
            return self.heap[0]
        else:
            return None
    # For debugging min heap.
    def __repr__(self):
        s = "Min Heap\n"
        previous_level = 0
        level = 0
        for index, node in enumerate(self.heap):
            if index == 2**level - 1:
                level += 1
                
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level
            
        return s

class HuffmanTree:
    def __init__(self, root):
        self.root = root
        self.map = dict()

    def get_root(self):
        return self.root

    # Generates huffman code map.
    def generate_map(self):
        if not self.get_root():
            return None
        self._generate_map(self.root)
        return self.map

    # Recursively calls itself adding characters to the end of a string 
    # for each call until a leaf node is reached to generate a code for 
    # the letter at each leaf node.
    def _generate_map(self, node, string=""):
        # If their are no children nodes, a leave node has been reached, so add
        # it's letter and the generated code to the dictionary.
        if not node.has_left_child() and not node.has_right_child():
            self.map[node.get_letter()] = string
            return

        # Leaf node has not been reached, so continue adding letters to the end of
        # the string until a leaf node is reached.
        else:
            if node.has_left_child():
                self._generate_map(node.get_left_child(), string + "0")
            if node.has_right_child():
                self._generate_map(node.get_right_child(), string + "1")
            return
    
    # Turns message into an encoded message by replacing characters with with
    # Huffman code replacements.
    def encode(self, data):
        code_map = self.generate_map()
    
        encoded_data = ""
        for char in data:
            code = code_map[char]
            encoded_data += code 
        return encoded_data

    # Decodes a message that has been encoded with Huffman encoding. Uses the Huffman
    # Tree used to encode to message to recursively move through the tree following that 
    # path direction specified by each integer of the encoded message until a leaf node
    # is hit. The character at this leaf node is added to the decoded message, and the 
    # process starts again at the next index of the encoded message.
    def decode(self, code):
        if not self.get_root():
            return ""
        return self._decode(code, self.root, 0, "")

    # Recursive portion of the above function.
    def _decode(self, code, node, index, data):
        # Checks if the end of the encoded message has been reached, and adds
        # the last character to the message if so.
        if index == len(code):
            data += node.get_letter()
            return data
        
        # Checks if at a leaf node, and if so, adds the character at the leaf node
        # to the decoded message. Then, the next cycle is started with the next index.
        if not node.has_left_child() and not node.has_right_child():
            data += node.get_letter()
            data = self._decode(code, self.root, index, data)

        # Moves left or right on the Huffman Tree depending on the encoded character at 
        # the specified position if not at a leaf node.
        elif node.has_left_child() and code[index] == "0":
            data = self._decode(code, node.get_left_child(), index + 1, data)

        elif node.has_right_child() and code[index] == "1":
            data = self._decode(code, node.get_right_child(), index + 1, data)

        return data
    
    # For debugging Tree.
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s

# Map for storing frequency that each character appears in a message.
class Map:
    def __init__(self):
        self.map = dict()

    def insert(self, key):
        frequency = self.get(key)
        if not frequency:
            self.map[key] = 1
        else:
            self.map[key] += 1

    def get(self, key):
        return self.map.get(key)
    
    def get_map(self):
        return self.map
    
    # For debugging Map.
    def __repr__(self):
        string = "Hash Map: \n"
        for key, value in self.map.items():
            string += str(key) + ': ' + str(value) + '\n'
        return string

# Encodes a message.
def huffman_encoding(data):
    # Builds a character to frequency of the character map.
    frequency_map = Map()
    for char in data:
        frequency_map.insert(char)
    
    # Puts the key, value pairs from the frequency map into a priority queue (min heap).
    min_heap = MinHeap()
    for char, freq in frequency_map.get_map().items():
        min_heap.insert(Node([freq, char]))

    # Merges min heap nodes into a Huffman Tree
    merged_node = min_heap.merge_nodes()
    huffman_tree = HuffmanTree(merged_node)

    # Encodes message using the corresponding Huffman Tree.
    encoded_data = huffman_tree.encode(data)

    return encoded_data, merged_node
    

def huffman_decoding(data, tree):
    huffman_tree = HuffmanTree(tree)

    # Decodes message using the corresponding Huffman Tree.
    return huffman_tree.decode(data)

if __name__ == "__main__":
    print("Test 1: ")
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # 69, The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # 36, 1110001010111011101111110000011011110110110001001010111001110011100000

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # 69, The bird is the word

    print("Test 2: ")
    codes2 = {}

    letter = "A"

    print ("The size of the data is: {}".format(sys.getsizeof(letter)))
    print ("The content of the data is: {}\n".format(letter))
    # 50, A

    encoded_data2, tree = huffman_encoding(letter)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data2)))
    print ("The content of the encoded data is: '{}'\n".format(encoded_data2))
    # 49,''

    decoded_data2 = huffman_decoding(encoded_data2, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data2)))
    print ("The content of the encoded data is: {}\n".format(decoded_data2))
    # 50, A

    print("Test 3: ")
    codes = {}

    empty = ""

    print ("The size of the data is: {}".format(sys.getsizeof(empty)))
    print ("The content of the data is: '{}'\n".format(empty))
    # 49, ''

    encoded_data, tree = huffman_encoding(empty)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: '{}'\n".format(encoded_data))
    # 49, ''

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: '{}'\n".format(decoded_data))
    # 49, ''