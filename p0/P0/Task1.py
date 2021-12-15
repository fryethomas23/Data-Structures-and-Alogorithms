"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_numbers = set()
for entry in texts:
    unique_numbers.add(entry[0])
    unique_numbers.add(entry[1])

for entry in calls:
    unique_numbers.add(entry[0])
    unique_numbers.add(entry[1])

print("There are %s different telephone numbers in the records."%(len(unique_numbers)))

# O(n)