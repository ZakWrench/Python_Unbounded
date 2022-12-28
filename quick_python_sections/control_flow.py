
# other examples of pass
def fct():
    pass


for i in range(10):
    pass
x = 2
if x > 0:
    pass
try:
    pass
except Exception:
    pass

# switch/case alt


def fct1():
    print("fct1()")


def fct2():
    pass


func_dict = {'a': fct1,
             'b': fct2}
func_dict['a']()

# for loop
for i in range(10):
    pass

a_list = [1, 2, 3, '4', [5, 6]]
for item in a_list:
    print(item)
for item in a_list:
    if isinstance(item, (type(a_list))):
        for subitem in item:
            print(int(subitem))
    else:
        print(int(item))


numbers = [10, 20, 30, 40]
double_numbers = map(lambda x: x * 2, numbers)
print(list(double_numbers))

# range
x = [13, 24, 34, 45, 56, 67, 78, 89, 90, 10, 11, 12, 13, 14, 15]
y = x[:len(x)+1]
print(list(range(x[1], x[8], x[-1])))

# tuple unpacking
x = [(1, 2), (3, 7), (9, 5)]

somelist = [(1, 2), (3, 7), (9, 5), (2, 2)]
result = 0
for t in somelist:
    result = result + (t[0] * t[1])
    print(result)


def fct3():
    result = 0
    for a, b in x:
        result = result + (a*b)
    print(result)


fct3()

# enumerate
prices = {'apples': 0.5, 'banana': 0.25, 'orange': 0.75, 'mango': 1.0}
for index, (fruit, price) in enumerate(prices.items()):
    print(f'{index}: {fruit} costs {price} dollars')

fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

words = ['cat', 'window', 'defenestrate']
lengths = [3, 6, 12]
for i, word in enumerate(words):
    print(f"{word}: {lengths[i]} characters. ")

# dictionary comprehension
fruits = ['apple', 'banana', 'orange', 'mango']
prices = [0.5, 0.25, 0.75, 1.0]

fruit_prices = {fruit: price for index,
                (fruit, price) in enumerate(zip(fruits, prices))}
print(fruit_prices)

fruit_prices = {}
for index, (fruit, price) in enumerate(zip(fruits, prices)):
    fruit_prices[fruit] = price

# remove all negative numbers - count -
x = [1, 3, 5, 0, -1, 3, -2]
for i in x:
    if i < 0:
        x.remove(i)
print(x)

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0
for row in y:
    for col in row:
        if col < 0:
            count += 1
print(count)

x.append(-12)


def count_neg_elements(lst):
    count = 0
    for element in lst:
        if element < 0:
            count += 1
    return count


print(count_neg_elements(x))

'''using sum() generator'''
count = sum(1 for element in x if element < 0)
print(count)

# list comprehension
x = [1, 2, 3, 4]
x_squared = []
for item in x:
    x_squared.append(item*item)

print(f'x_squared={x_squared}')
y = [item*item for item in x if item % 2 == 0]
print(f'y = {y}')

new_dict = {item: item * item for item in x}
print(f'dictionary = {new_dict}')

x_squared = (item*item for item in x)
print(list(x_squared))


def generator_count(max):
    count = 1
    while count <= max:
        yield count
        count += 1
    print(end=";;;;;;;;; ")


count = 40


def looping_generator():
    for number in generator_count(count):
        print(number, end=", ")


x = [1, -2, 0, 10, 9, -3, -10]
x_compr = [i for i in x if i < 0]
print(x_compr)

odd_100 = (i for i in range(100) if i % 2)
for i in odd_100:
    print(i, end=", ")
    # generator_count(i)
    # looping_generator()


cube_dict = {x: x**3 for x in range(11, 17)}


def start_line():
    print('\n')


start_line()
print(cube_dict)

#####word_count.py#####
infile = open('word_count.tst')
lines = infile.read().split("\n")
line_count = len(lines)

word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)
    print(len(line))

print("File has {0} lines, {1} words, {2} characters".format(
    line_count, word_count, char_count))
###
line_count = 0
word_count = 0
char_count = 0
with open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count += len(words)

print("File has {0} lines, {1} words, {2} characters".format(
    line_count, word_count, char_count))


'''
def isPalindrome(theString):
    if len(theString) == 0 or len(theString) == 1:
        # BASE CASE
        return True
    else:
        head = theString[0]
        middle = theString[1:-1]
        last = theString[-1]
        return head == last and isPalindrome(middle)


# init counts


text = 'racecar'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'amanaplanacanalpanama'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'tacocat'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
text = 'zophie'
print(text + ' is a palindrome: ' + str(isPalindrome(text)))
print(type(len([1, '2'])))


looping_generator()
'''
