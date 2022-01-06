Recursion was used to access sub directories within an input directory because it 
allows for clean looking code that repeatedly looks through directories within a 
directory. This process takes O(n) when n is the number of files and sub directories within the
input directory. Storage costs is O(n) because files names are stored in an array.

Times: O(n)
    search: O(n)

Space: O(n)
    list: O(n)