A map is used to store the frequency that characters occur within an input message
because it provides an O(1) lookup. Space complexity for the map is O(n).

A min heap is used because the minimum frequency node needs to be easily accessible,
and new nodes are repeatedly being added on after merging nodes. This means that for 
each insertion the minimum node needs to be at the top and after each deletion, the
minimum node needs to be at the top. A min heap does both of these operations in 
O(log(n)). A min heap is the fastest when insertion, deleltion, and quick access to 
the minimum value are critical. Space complexity for the heap is O(n).


A tree is used for quick access to the leaf nodes of a huffman tree. Accessing an 
individual leaf node takes O(log(n)). Space complexity for the huffman tree is 
O(n*log(n)) because intermediate nodes are created connecting the leaf nodes.

A queue is used for printing and debugging the tree. This operates takes O(n). The 
apce complexity for the queue is O(n).

The run time of the entire encoding operation is O(n*log(n)) because each element
of the message must be gone through, O(n), and the corresponding huffman code must
be produced, O(log(n)). This equates to O(n*log(n)). There are no higher order 
elements than this during encoding. Decoding is the same, but in reverse. The space 
complexity is also O(n*log(n)) because this is the largest space complexity from 
the used data structures.

Time: O(n*log(n))
    encode: O(n*log(n))
    decoding: O(n*log(n))

Space: O(n*log(n))
    map: O(n)
    queue: O(n)
    min heap: O(n)
    huffman tree: O(n*log(n))
    encoding: O(n*log(n))
    decoding: O(n*log(n))