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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
from operator import itemgetter

sorted_texts = sorted(texts, key=itemgetter(2))
sorted_calls = sorted(calls, key=itemgetter(2), reverse=True)

print("First record of texts, %s texts %s at time %s"%(
    sorted_texts[0][0], 
    sorted_texts[0][1], 
    sorted_texts[0][2]
))
print("Last record of calls, %s calls %s at time %s, lasting %s seconds"%(
    sorted_calls[0][0], 
    sorted_calls[0][1], 
    sorted_calls[0][2], 
    sorted_calls[0][3]
))

# O(n*log(n))