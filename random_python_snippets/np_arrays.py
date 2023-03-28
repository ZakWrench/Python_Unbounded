import cmath
import numpy as np

my_array = [1, 2, 3]
my_np_array = np.array([1, 2, 3])

my_array[0]
my_np_array[1]

my_array[0:2]
my_np_array[:-1]

my_array.append(4)
my_np_array = np.append(my_np_array, 4)

my_array.remove(2)
my_np_array = np.delete(my_np_array, 2)

len(my_array)
my_np_array.size

max(my_array), min(my_array)
my_np_array.max(), my_np_array.min()

my_array.sort()
my_np_array.sort()

my_np_array = np.array([1, 2, 3, 4])

reshaped_array = my_np_array.reshape((4, 1))
print(reshaped_array)

transposed_array = my_np_array.T
print(transposed_array * 2)

heh_array = transposed_array * reshaped_array * 2
print(heh_array)

############################
array = np.array([1, 2, 3, 4])
add_array = np.add(array, 5)  # [6,7,8,9]
subtract_array = np.subtract(add_array, 1)  # [5,6,7,8]
divide = np.divide(subtract_array, cmath.pi)
multiply = np.multiply(divide, cmath.e)
print(multiply)
power = np.power(array, 3)
remainder = np.remainder(array, 3)
floor_divide = np.floor_divide(array, 3)

reciprocal = np.reciprocal(array.astype(float))
sqrt = np.sqrt(array)
exp = np.exp(array)
log = np.log(array)
log10 = np.log10(array)
absolute = np.absolute(array)
round = np.round(array / 3)
trunc = np.trunc(array / 3)
print(
    f"\ntrunc: {trunc},\nround: {round},\nlog10: {log10},\nreciprocal: {reciprocal}")

sin = np.sin(array)
cos = np.cos(array)
tan = np.tan(array)
arcsin = np.arcsin(array / 5)
arccos = np.arccos(array / 5)
arctan = np.arctan(array)
print(f"arccos: {arccos}")

############Comparison And Logical##############

arr1 = np.array([1, 3, 5])
arr2 = np.array([2, 4, 6])
print(f"arr1: {arr1}, arr2: {arr2}")

a, b = arr1, arr2
print(f"np.greater(a, b): {np.greater_equal(a, b)}")
print(f"np.greater_equal(a, b): {np.greater_equal(a, b)}")
print(f"np.less(a, b): {np.less(a, b)}")
print(f"np.less_equal(a, b): {np.less_equal(a, b)}")
print(f"np.equal(a, b): {np.equal(a, b)}")
print(f"np.not_equal(a, b): {np.not_equal(a, b)}")

x = np.array([True, False, True])
y = np.array([True, True, False])

print(f"np.logical_and(x, y): {np.logical_and(x, y)}")
print(f"np.logical_or(x, y): {np.logical_or(x, y)}")
print(f"np.logical_not(x): {np.logical_not(x)}")
print(f"np.logical_xor(x, y): {np.logical_xor(x, y//2)}")

###########Statistics###############
data = np.array([1, 2, 3, 4, 5])

print(f"np.sum(data): {np.sum(data)}")
print(f"np.mean(data): {np.mean(data)}")
print(f"np.median(data):{np.median(data)}")
print(f"np.std(data): {np.std(data)}")
print(f"np.var(data): {np.var(data)}")
print(f"np.percentile(data, 50): {np.percentile(data, 50)}")
print(f"np.histogram(data, bins = 2): {np.histogram(data, bins = 2)}")
data_2 = data * 2
print(
    f"np.correlate(data, data): {np.correlate(data, data),}\n{np.correlate(data, data_2)}")
print(f"np.convolve(data, data_2): {np.convolve(data, data_2)}")
print(f"np.cov(data, data_2): {np.cov(data, data_2)}")
print(f"polyfit(data, data_2, 1): {np.polyfit(data, data_2, 1)}")
print(f"np.polyval([1, -5], data)): {np.polyval([1, -5], data)}")

###########Linear Algebra################

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"np.dot(A,B): {np.dot(A,B)}")
print(f" np.matmul(A,B): {np.matmul(A,B)}")
print(f"np.linalg.det(A): {np.linalg.det(A)}")
print(f"np.linalg.inv(A): {np.linalg.inv(A)}")
print(f"np.linalg.eig(A): {np.linalg.eig(A)}")
