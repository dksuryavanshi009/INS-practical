def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Get user input for two integers
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
gcd, x, y = extended_gcd(a, b)

print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients (x, y) for the equation ax + by = gcd(a, b) are ({x}, {y})")
