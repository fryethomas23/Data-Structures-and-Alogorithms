import os

# Looks through input directory and sub directories returning files that have the 
# matching extension. Recursively calls itself when input directory contains another 
# directory.
def find_files(path, suffix):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system

    Returns:
    a list of paths
    """
    file_list = []
    suf_len = len(suffix)
    # Get list of items in current directory and iterate through them
    directory_contents = os.listdir(path)
    for item in directory_contents:
        # If item is a directory, call find_files with the directory to get matching 
        # files in the directory and add them to the file list
        if os.path.isdir(path + '/' + item):
            file_list += find_files(path + '/' + item, suffix)
        #if item is a file with the provided extension, add it to the list
        elif os.path.isfile(path + '/' + item) and item[(suf_len*-1):] == suffix:
            file_list.append(item)
    
    return file_list

print('Test 1: ', find_files('p1/testdir','.c'))
# Test 1:  ['a.c', 'b.c', 'a.c', 't1.c']

print('Test 2: ', find_files('p1/testdir','.h'))
# Test 2:  ['a.h', 'b.h', 'a.h', 't1.h']

print('Test 3: ', find_files('p1/testdir','.q'))
# Test 3:  ['t1.q']

