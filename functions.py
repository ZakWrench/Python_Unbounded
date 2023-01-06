def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        print(numbers, numbers[1:])
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
            return maxnum


maximum(1, 2, 40)

# Dealing with an indefinite number of arguments passed by keyword


def funct(x, y, **other):
    print("x: {0}, y: {1}, keys in 'other': {2}". format(
        x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]
    print("total of values in 'other' is {0}".format(other_total))


funct(2, y="1", foo=3, bar=5)
funct(y=2, x="1", foo=3, bar=5)

###


def funct(*params):
    for i in reversed(params):
        print(i)
    return i


funct(1, 2, 3, 4, '3', [2, 3, 4])


def f(n, list1, list2):
    list1.append(3)
    list2 = [4, 5, 6]
    n = n + 1


f(5, [1, 2], [4, 5])

# Nonlocal and Global Variables

g_var = 0
nl_var = 0
print("top level -> g_var: {0} nl_var: {1}".format(g_var, nl_var))


def test():
    nl_var = 2
    print("in test -> g_var: {0} nl_var: {1}".format(g_var, nl_var))

    def inner_test():
        global g_var
        nonlocal nl_var
        g_var = 1
        nl_var = 4
        print("in inner_test -> g_var: {0} nl_var: {1}".format(g_var, nl_var))

    inner_test()
    print("in test -> g_var: {0} nl_var: {1}".format(g_var, nl_var))


test()
print("top level -> g_var: {0} nl_var: {1}".format(g_var, nl_var))

# Assign Functions to Variables/list/Dictionary/Tuple


def fahr_to_kelvin(degree_f):
    return 273.15 + (degree_f - 32) * 5 / 9


def cel_to_kelvin(degree_c):
    return 273.15 + degree_c


abs_temperature = fahr_to_kelvin
abs_temperature(32)
dict_temp = {'FtoK': fahr_to_kelvin, 'CtoK': cel_to_kelvin}
dict_temp['FtoK'](50)

# Lambda Expressions

lambda_dict = {'fahr': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9,
               'cels': lambda deg_c: 273.15 + deg_c}
lambda_dict['fahr'](32)

# Generator Functions


def generator_fct(start, limit):
    x = start
    while x < limit:
        print("in generator, x =", x)
        yield x
        x += 1


for i in generator_fct(2, 10):
    print(i)

2 in generator_fct(2, 10)
5 in generator_fct(4, 20)
###


def subgen(x):
    for i in range(x):
        yield i


def gen(y):
    yield from subgen(y)


for q in gen(6):
    print(q)

# Decorators


def decorate(func):
    print("in decorate function, decorating", func.__name__)

    def wrapper_func(*args):
        print("Executing", func.__name__)
        return funct(*args)
    return wrapper_func


def myfunction(param):
    print(param)


myfunction = decorate(myfunction)
myfunction("Hello")


def decorate(func):
    print("in decorate function, decorating", func.__name__)

    def wrapper_func(*args):
        def inner_wrapper(*args):
            return_value = func(*args)
            return "<html>{}</html".format(return_value)
        print("Executing", func.__name__)
        return inner_wrapper(*args)
    return wrapper_func


@decorate
def myfunction(param):
    print(param)
    return param


print(myfunction("@Decorate'd"))


# word count

punctuation = str.maketrans("", "", "!.,:;-?")


def clean_line(line):
    cleaned_line = line.lower()
    cleaned_line = cleaned_line.translate(punctuation)
    return cleaned_line


def get_words(line):
    words = line.split()
    return "\n".join(words) + "\n"


with open("moby_01.txt") as infile, open("moby_01_words.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
        cleaned_word = get_words(cleaned_line)
        outfile.write(cleaned_word)


def count_words(words):
    word_count = {}
    for word in moby_words:
        count = word_count.setdefault(word, 0)
        word_count[word] += 1
    return word_count


def word_stats(word_count):
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    least_common = word_list[:5]
    most_common = word_list[-1:-6:-1]
    return most_common, least_common


moby_words = []
with open('moby_01_words.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())

word_count = count_words(moby_words)

most, least = word_stats(word_count)

print("Most Common Words: ")
for word in most:
    print(word)
print("\nLeast Common Words: ")
for word in least:
    print(word)
