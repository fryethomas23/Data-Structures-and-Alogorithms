For the cache, a double linked list is used for the efficiency of deleting the head 
node, O(1); insertion at the tail, O(1); and moving of an intermediate node, O(1). Searching 
the linked list would normally take O(n), but using a map allows for the access to an
intermediate node in the linked list using a key at O(1). This means that all operations
implemented for this problem using a least recently used cache have O(1). Storage costs 
of both the linked list and the map are O(n).

Time: O(1)
    insertion: O(1)
    deletion: O(1)
    search: O(1)

Space: O(n)
    map: O(n)
    linked list: O(n)