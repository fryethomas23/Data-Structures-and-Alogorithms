"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_lengths = {}
longest_caller = {
    "number": "",
    "call_length": 0
}
for entry in calls:
    if entry[0] not in call_lengths:
        call_lengths[entry[0]] = 0
    if entry[1] not in call_lengths:
        call_lengths[entry[1]] = 0
    call_lengths[entry[0]] += int(entry[3])
    call_lengths[entry[1]] += int(entry[3])
    
    if longest_caller["call_length"] < call_lengths[entry[0]]:
        longest_caller['number'] = entry[0]
        longest_caller['call_length'] = call_lengths[entry[0]]
    if longest_caller["call_length"] < call_lengths[entry[1]]:
        longest_caller['number'] = entry[1]
        longest_caller['call_length'] = call_lengths[entry[1]]    

print("%s spent the longest time, %s seconds, on the phone during September 2016."%(
    longest_caller['number'],
    longest_caller['call_length']
))

# O(n*log(n))
