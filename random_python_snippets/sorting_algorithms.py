import numpy as np
import random
import heapq
import itertools

x = [1, 2, 3, 4, 5, 6]
y = [14, 12, 13, 11, 16, 5]
z = [26, 25, 24, 23, 22, 21]
xyz = list(itertools.chain(x, y, z))


def np_random_array(lst):
    lst[:] = np.random.randint(0, 100, 10)
    return lst


xyz_3 = xyz
# append and remove 50 random elements from xyz_3
for i in range(50):
    xyz_3.append(random.randint(0, 100))
    del xyz_3[random.randint(0, len(xyz_3) - 1)]
# same as above
for i in range(len(xyz_3)):
    xyz_3[i] = random.randint(0, 100)

# O(n^2)

# Bubble Sort


def bubble_sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            return arr


# Insertion Sort


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def insertion_sort_tuple(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
            j -= 1
    return arr

# Selection sort


def selection_sort(arr):
    for i in range(len(arr)):
        # find minimum element
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def selection_sort_generator(arr):
    for i in range(len(arr)):
        min_index = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


xyz_2 = []
for i in selection_sort_generator(xyz):
    xyz_2.append(i)

# O(n log n)

# Quick Sort (Partition based/O(n) worst case)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide arr into 2 parts
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursive sorting
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # merging sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i, j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Heapsort


# transform xyz_3 into heap data structure
heapq.heapify(xyz_3)
# repeatedly extract the smallest element from the heap and place at the end of new list, effectively sorting the list
xyz_3 = [heapq.heappop(xyz_3) for i in range(len(xyz_3))]


# Radix Sort(Integers only, Work best with small number of digits, avoid large number of digits or floats)
# O(nk) where k is the number of digits in the largest number in the list
# and n is the number of elements in the list
arr = [4, 10, 6, 2]


def radix_sort(arr):
    max_digit = max(arr)  # 10
    exp = 1
    while max_digit // exp > 0:
        counting_sort(arr, exp)  # ([4, 10, 6, 2],1)
        exp *= 10  # 10
    return arr


def counting_sort(arr, exp):  # ([4, 10, 6, 2],1)
    n = len(arr)  # 4
    output = [0] * n  # [0,0,0,0]
    count = [0] * 10  # [0,0,0,0,0,0,0,0,0,0]
    for i in range(n):
        # 4//1%10=4, 10//1%10=0, 6//1%10=6, 2//1%10=2
        index = (arr[i] // exp) % 10
        count[index] += 1  # [0,0,0,0,1,0,1,0,0,0]
    for i in range(1, 10):
        count[i] += count[i - 1]  # [0,0,0,0,1,1,2,2,2,2]
    i = n - 1  # 3
    while i >= 0:  # 3>=0
        index = (arr[i] // exp) % 10  # 2//1%10=2
        output[count[index] - 1] = arr[i]  # [0,0,0,2]
        count[index] -= 1   # [0,0,0,0,1,1,2,1,2,2]
        i -= 1  # 2
    for i in range(n):  # 0,1,2,3
        arr[i] = output[i]  # [4,6,2,10]


# Bucket Sort
# O(n+k) where k is the number of buckets
# and n is the number of elements in the list


def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]  # [[],[],[],[]]
    for val in arr:
        bucket_index = int(val*len(arr))  # 0,1,2,3
        buckets[bucket_index].append(val)  # [[4],[10],[6],[2]]
    for bucket in buckets:
        bucket.sort()  # [[4],[6,10],[2]]
    return [val for bucket in buckets for val in bucket]  # [4,6,10,2]


# Counting Sort
# O(n+k) where k is the range of possible values
# and n is the number of elements in the list
# only works with positive integers, and only works with small range of numbers

def counting_sort(arr):
    max_val = max(arr)  # 10
    counting_arr = [0] * (max_val + 1)
    for val in arr:
        counting_arr[val] += 1
    sorted_arr = []
    for i, count in enumerate(counting_arr):
        for _ in range(count):
            sorted_arr.append(i)
    return sorted_arr


# Shell Sort
# O(n^2) worst case, O(nlogn) best case
# uses insertion sort, but with a gap between elements to be compared

def shell_sort(arr):
    gap = len(arr) // 2  # 2
    while gap > 0:  # 2>0
        for i in range(gap, len(arr)):  # 2,4
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# Tim Sort
# O(nlogn) worst case, O(n) best case
# uses insertion sort and merge sort
# sorted() take an iterable as arg an return new sorted list
# sort() take no arg and sort the list in place
# use sorted() on tuples
# numpy.sort() is better
new_list = sorted(xyz)  # safe because copy
new_list_2 = np.copy(xyz)
new_list_2 = np.sort(new_list_2, axis=-1, kind='heapsort', order=None)


def tim_sort(arr):
    np_random_array(arr)
    arr.sort()
    return arr


euh = []
tim_sort(euh)


# Intro Sort
# Combines quicksort and heapsort, uses quicksort primarly
# and switch to heapsort if recursion limit has reached depth of 2log(n)


def intro_sort(arr):
    # Switch to heapsort if recursion limit has reached depth of 2log(n)
    if len(arr) < 16:
        return sorted(arr)
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    return intro_sort(lows) + pivots + intro_sort(highs)
