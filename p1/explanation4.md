Recursion was used to access groups within an input group because it allows for clean 
looking code that repeatedly looks through groups within groups. This process takes 
O(n) where n is the number of users and groups within the input group. The space 
complexity is O(1) because a single boolean value is returned.

Time: O(n)
    search: O(n)

Space: O(1)
    boolean:O(1)