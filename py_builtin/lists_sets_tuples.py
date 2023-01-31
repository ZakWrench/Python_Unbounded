#########################
# Lists: Ordered and mutable.
# sorting, searching, or looping.
# Storing a list of high scores in a game.
# Keeping track of a list of to-do tasks for a project.
# Storing a list of stock prices for a financial application.

#########################

import copy
from collections import Counter
l1 = [1, 2, 3, 4, 5, 6]
l2 = [7, 8, 9, 10, 8, 10]
l3 = [23, 221, 120]

l1.append(7) #[..,6,7]
l2.reverse() #[10,9..]
l2.remove(10) #[7, 8, 9, 8, 10]
# now if only this was possible:
#l2_remove = l2.remove(10)
#l2_remove _ = l2_remove * 2
l2.insert(0, 100) #[100, 7, ...]
del l1[:-4] #[4, 5, 6, 7]
l1.append(l2) #[4, 5, 6, 7, [100, 10, 8, 9, 8, 7]]
l1.extend([8, 9, 10]) #[4, 5, 6, 7, [100, 10, 8, 9, 8, 7],8, 9, 10]
l1.append(l3) 
l1.pop(0) #[5, 6, 7, [100, 10, 8, 9, 8, 7],8, 9, 10]
l1.index(8) # 4
l1.count(7) # 1
l4 = l1.copy()
l4.clear()
l4 += l3
l4 *= 2
l4 = (l3 * 1) + (l4 + [])
l4.sort()
l_deepcopy = copy.deepcopy(l1)
l_deepcopy[0] = 1000
print(l1)
l_deepcopy = l1
l_deepcopy[0] = 1000
print(l1)


def sort_lists(lst):
    for i, x in enumerate(lst):
        if isinstance(x, list):
            lst[i] = sorted(x, key=lambda x: (isinstance(x, str), x))
    return lst


l1 = sort_lists(l1)

print(f"l4={l4} \nl1={l1}")


#########################
# Sets: Unordered collections of unique elements
# list duplication removal
# membership testing with in
# mathematical set operations like union, intersection, difference, and symmetric difference.
# data validation
# frequency counter
#########################

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 5, 7, 8, 9, 10}

s1.add(7)
s1.remove(5)
s1.discard(6)
s3 = s2 | s1
s3 = s2.union(s1)
s4 = s3 & s1
s4 = s3.intersection(s1)
s4.add(8)
s1.add(9)
s5 = s4.difference(s1)
s6 = s1.difference(s4)
s7 = s5.symmetric_difference(s3)

print(f's1={s1} \ns2={s2} \ns3={s3} \ns4 ={s4} \ns5={s5}\ns6={s6} \ns7={s7}')
print(f'{s1.add(1)}\n{Counter(s1)}')

#########################
# Tuples: Ordered and immutable.
# A point's x and y coordinates
# date's month, day, and year.
# return multiple values from a function.
# Unpacking a tuple.
#
#########################

t1 = (1, 2, 3, 4, 5, 6)
t2 = (7, 8, 9, 10)
t3 = (23, 221, 120)

t1 += (7,)
t2 = t2[::-1]  # reverse order
t2 = t2[:1] + (100,) + t2[1:]  # insert 100 at index 1
t1 = t1[:-4]  # delete/slice last 4 elements
t1 += (t2,)  # add tuple t2 to tuple t1
t1 += (8, 9, 10)
t1 += (t3,)
t1 = t1[1:]
t1.index(8)  # return index of 8
t1.count(7)
t4 = t1[:]
t4 = ()
t4 += t3
t4 *= 2
t4 = (t3 * 1) + (t4 + ())
t4 = sorted(t4)
print("len: ", len(t2), "max: ", max(t2), "min: ",
      min(t2), "sum: ", sum(t2))
print("tuple: ", tuple(t2), "t2[1]", t2[1],
      "t2[1:3]", t2[1:3], "t2[1:3:2]", t2[1:3:2])
print("t1 == t2: ", t1 == t2, "100 in t2: ", 100 in t2)

print(f"t1={t1} \nt2={t2} \nt3={t3}\nt4={t4}\n{Counter(t1)} ")

#########################
