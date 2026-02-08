'''
]

🔹 DICTIONARY – Coding Questions
1️⃣ Sort dictionary by values
d = {'a': 3, 'b': 1, 'c': 2}


➡ Output: {'b':1, 'c':2, 'a':3}
'''

dict1 = {'a': 3, 'b': 1, 'c': 2}
#dict.items() returns a view object that displays a list of a dictionary's key-value tuple pairs.like[('a', 3), ('b', 1), ('c', 2)]
#sorted() function sorts the items of the dictionary based on the values (x[1]) using a lambda function as the key.
#x[1] means ('a', 3) -> 3, ('b', 1) -> 1, ('c', 2) -> 2
sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1]))

print(sorted_dict)
print("1-------------------------------------------------------")