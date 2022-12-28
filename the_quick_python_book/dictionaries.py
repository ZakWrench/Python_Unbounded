from collections import Counter
from collections import defaultdict

# O(n^2)
matrix = [[3, 0, -2, 11],
          [0, 9, 0, 0],
          [0, 7, 0, 0],
          [0, 0, 0, -5]]

same_matrix = [3, 0, -2, 11, 0, 9, 0, 0, 0, 7, 0, 0, 0, 0, 0, -5]
# formula:
#index = row * num_columns + column

index = 1 * 4 + 2
element = same_matrix[index]
print(element)

matrix_dict = {(0, 0): 3, (0, 2): -2, (0, 3): 11,
               (1, 1): 9, (2, 1): 7, (3, 3): -5}

if (1, 1) in matrix_dict:
    element = matrix_dict[(1, 1)]
else:
    element = 0
print(element)

element = matrix_dict.get((0, 1), "can't find item or is = 0")
print(element)


matrix_dict = {
    "matrix_one_array": same_matrix
}
index = 1 * 4 + 1
element = matrix_dict["matrix_one_array"][index]
print(element)


###########

# Dictionaries as cache
cache = {}  # global var to store previous results
result = 1  # some result


def fct(m, n, t):
    if (m, n, t) in cache:
        return cache[(m, n, t)]  # value repeated
    else:
        cache[(m, n, t)] = result  # new added value
        return result


# Spreadsheet
spread = {}
spread[('A', 1)] = 100
spread[('A', 2)] = 103
print(spread)
print(len(spread))

# Count occurence with dict
moby_words = ['zak', 'zak', 'zak', 'zak', 'zak', 'zak', 'zak', 'zak']
word_count = {}
for word in moby_words:
    count = word_count.setdefault(word, 0)
    count += 1
    word_count[word] += 1

word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])
print("Most common words: ")
for word in reversed(word_list[-5:]):
    print(word)
print("\nLeast common words:")
for word in word_list[:5]:
    print(word)

# Count using Counter
#moby_words = [n]
word_count = Counter(moby_words)
# Get n most common and least common words
most_common_words = word_count.most_common(10)
for word, count in most_common_words:
    print(f'{word}: {count}')
least_common_words = word_count.most_common()[:-6:-1]
for word, count in least_common_words:
    print(f'{word}: {count}')

# using defaultdict
word_count = defaultdict(int)
for word in moby_words:
    word_count[word] += 1

word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])
print("Most common words:")
for word in reversed(word_list[-5:]):
    print(word)
print("\nLeast common words: ")
for word in word_list[:5]:
    print(word)
