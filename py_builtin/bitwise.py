# Bitwise AND
a = 10  # 1010 in binary
b = 3   # 0011 in binary
c = a & b
print(c, bin(c))  # Output: 2 (0010 in binary)

# Bitwise OR
c = a | b
print(c, bin(c))  # Output: 11 (1011 in binary)

# Bitwise XOR
c = a ^ b
print(c, bin(c))  # Output: 9 (1001 in binary)

# Bitwise NOT
c = ~a
print(c, bin(c))  # Output: -11 (11111111111111111111111111110101 in binary)

# Left shift
c = a << 2
print(c, bin(c))  # Output: 40 (101000 in binary)

# Right shift
c = a >> 2
print(c, bin(c))  # Output: 2 (0010 in binary)