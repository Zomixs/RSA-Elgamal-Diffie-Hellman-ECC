
# Problem 3: ECC

# Elliptic curve: y^2 = x^3 + 2x + 3 (mod 67)

p = 67
a = 2
b = 3

# Function to add two points
def add_points(P, Q):

    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # Check if the points cancel each other
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # If the points are the same, use point doubling
    if P == Q:
        top = 3 * x1**2 + a
        bottom = 2 * y1

    # If the points are different, use point addition
    else:
        top = y2 - y1
        bottom = x2 - x1

    # Calculate the slope
    inverse = pow(bottom % p, -1, p)
    slope = (top * inverse) % p

    # Find the new point
    x3 = (slope**2 - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)


# Function to multiply a point by a number
def multiply_point(num, point):

    result = None

    for i in range(num):
        result = add_points(result, point)

    return result


# Given values
G = (2, 22)
d = 4
P = (24, 26)
r = 2

print("Problem 3: ECC")
print("Curve: y^2 = x^3 + 2x + 3 (mod 67)")
print("Base point =", G)
print("Bob's private key =", d)
print("Plaintext =", P)
print("Alice's r =", r)


# Step 1: Bob calculates his public key

print("\nStep 1: Bob's Public Key")

public_key = multiply_point(d, G)

print("Bob's public key =", public_key)


# Step 2: Alice encrypts the message

print("\nStep 2: Alice Encryption")

# Calculate C1 = r * G
C1 = multiply_point(r, G)

# Calculate the shared point
shared = multiply_point(r, public_key)

# Calculate C2 = P + shared
C2 = add_points(P, shared)

print("C1 =", C1)
print("Shared point =", shared)
print("C2 =", C2)

print("Encrypted ciphertext =", (C1, C2))


# Step 3: Bob decrypts the message

print("\nStep 3: Bob Decryption")

# Calculate d * C1
shared_bob = multiply_point(d, C1)

# Find the negative of the shared point
x, y = shared_bob
negative = (x, (-y) % p)

# Recover the original point
decrypted = add_points(C2, negative)

print("Bob's shared point =", shared_bob)
print("Negative point =", negative)
print("Decrypted plaintext =", decrypted)
