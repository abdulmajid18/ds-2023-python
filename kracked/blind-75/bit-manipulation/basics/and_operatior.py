a = 6   # 110 in binary
b = 3   # 011 in binary

print(a & b)        # 2
print(bin(a & b))   # '0b10'



def is_even(n):
    return (n & 1) == 0
