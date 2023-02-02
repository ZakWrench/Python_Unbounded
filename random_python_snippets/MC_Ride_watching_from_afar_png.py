######

# Avoid changing values of an iterable while iterating

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(lst):
    if index % 2 == 0:
        lst.pop(index)

print(lst)  # [20, 30, 50, 60, 80, 90]

# Correct way
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_lst = [v for i, v in enumerate(lst) if i % 2 == 0]
print(new_lst)

######

# Circular import -> change filename from built-in name to fix it
gooey.py
import gooey
>> AttributeError: partially initialized module 'gooey' has no attribute 'GooeyParser' (most likely due to a circular import)
    
    
######

