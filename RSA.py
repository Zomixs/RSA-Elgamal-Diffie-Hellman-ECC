
# Problem 1: RSA

# Part A: Find d
n = 221
e = 5

# Prime factors of 221
p = 13
q = 17

# Calculate phi(n)
phi = (p - 1) * (q - 1)

# Find d
d = pow(e, -1, phi)

print("Problem 1(a)")
print("n =", n)
print("e =", e)
print("p =", p)
print("q =", q)
print("phi(n) =", phi)
print("d =", d)

# Part B: Encrypt HOW ARE YOU

print("\nProblem 1(b)")

message = "HOW ARE YOU"

# A = 00, B = 01, ..., Z = 25, space = 26
numbers = []

for letter in message:
    if letter == " ":
        numbers.append(26)
    else:
        numbers.append(ord(letter) - 65)

print("Original message:", message)
print("Numbers:", numbers)

# Encrypt each number using C = P^e mod n
encrypted = []

for num in numbers:
    c = pow(num, e, n)
    encrypted.append(c)

print("Encrypted numbers:", encrypted)

# Decrypt to check the answer
decrypted = []

for c in encrypted:
    num = pow(c, d, n)

    if num == 26:
        decrypted.append(" ")
    else:
        decrypted.append(chr(num + 65))

print("Decrypted message:", "".join(decrypted))