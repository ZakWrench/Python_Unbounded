import random


def generate_random_content():
    lst = []
    dct = {}
    for i in range(20):
        lst.append(random.randint(0, 100))
        dct[i] = random.randint(0, 100)
    return lst, dct  # this should match the assignment of the function call

# Enumerate takes an iterable, and returns an iterator that produces tuples
# cainting the index and the value of each element in the iterable
# Use it to keep track of the current index of a loop.


def enum(lst, dct):
    for index, value in enumerate(lst):
        print(f'Index: {index}, Value: {value}', end=' \\\\ ')
        if value == 0:
            print('Found a zero!')
            break
    print("\n")
    x = 0
    for index, item in enumerate(dct.items()):
        if x == 0:
            print(f'Index: {index}, Value: {item[1]}', end=' \\\\ ')
            x = random.randint(1, lst[len(lst) - 1])
        else:
            print(f'Index: {index}, Value: {dct[index]}', end=' // ')
            x = 0

    return


lst2, dct2 = generate_random_content()  # unpacking the tuple
enum(lst2, dct2)
# takes two or more iterables as input and returns an iterator
# that generates tuples containing elements from each iterable.
lst3 = list(zip(lst2, dct2.values()))

# Map takes  a function and one or more iterables as input,
# and returns an iterator that paplies the function to each element of the iterables.
# The function is called with the elements from the iterables as args,
# in the same order as the appear in the input iterables.
lst3 = list(map(lambda x: x[0] + x[1], lst3))
lst4 = map(lambda x, y, z: x * y + z, lst2, dct2.values(), lst3)
strngs = list(map(str, lst4))
# list comprehension, works the same as above
strngs_2 = [str(x) for x in lst4]
strngs_to_ints = list(map(int, strngs))
# list(strngs) inside print() returns an empty list
print(f'\nlst3 = {lst3}\n{lst4, list(lst4)}\n{strngs}\n{strngs_to_ints}')
