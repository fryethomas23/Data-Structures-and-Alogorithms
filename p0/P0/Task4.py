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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
telemarketers = set()
making_calls = set()

for call in calls:
    making_calls.add(call[0])

for number in making_calls:
    telemarker = True
    for text in texts:
        if number == text[0] or number == text[1]:
            telemarketer = False
    for call in calls:
        if number == call[1]:
            telemarker = False
    if telemarker:
        telemarketers.add(number)

print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
    print(number)

# O(n^2)