
"""Problem 3: Elliptic curve ElGamal point arithmetic, encryption, decryption."""
MOD, A, B = 67, 2, 3
# None represents the point at infinity (identity element).
def on_curve(P):
    if P is None:
        return True
    x, y = P
    return (y*y - (x*x*x + A*x + B)) % MOD == 0

def negate(P):
    return None if P is None else (P[0], -P[1] % MOD)

def add(P, Q):
    """Add curve points, using the doubling formula when P == Q."""
    assert on_curve(P) and on_curve(Q)
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and (y1 + y2) % MOD == 0:
        return None
    if P == Q:
        numerator, denominator = 3*x1*x1 + A, 2*y1
    else:
        numerator, denominator = y2-y1, x2-x1
    slope = numerator * pow(denominator % MOD, -1, MOD) % MOD
    x3 = (slope*slope - x1 - x2) % MOD
    y3 = (slope*(x1-x3) - y1) % MOD
    result = (x3, y3)
    assert on_curve(result)
    return result

def multiply(k, P):
    """Double-and-add scalar multiplication."""
    if k < 0:
        return multiply(-k, negate(P))
    result = None
    while k:
        if k & 1:
            result = add(result, P)
        P = add(P, P)
        k >>= 1
    return result

G, d, plaintext, r = (2, 22), 4, (24, 26), 2
assert on_curve(G) and on_curve(plaintext)
print('Problem 3: ECC on y^2 = x^3 + 2x + 3 (mod 67)')
print(f'G={G}, Bob private key d={d}, plaintext={plaintext}, Alice r={r}')
print('2G =', add(G, G))
public_key = multiply(d, G)
print('Bob public key e2 = dG =', public_key)

# Alice's encryption algorithm:
#   C1 = rG
#   S = r*e2
#   C2 = P + S
C1 = multiply(r, G)
S = multiply(r, public_key)
C2 = add(plaintext, S)
print('\nAlice encryption:')
print('C1 = rG =', C1)
print('S = r*e2 =', S)
print('C2 = P + S =', C2)
print('Ciphertext =', (C1, C2))

# Bob's decryption algorithm:
#   S_bob = d*C1
#   P = C2 + (-S_bob)
S_bob = multiply(d, C1)
recovered = add(C2, negate(S_bob))
print('\nBob decryption:')
print('d*C1 =', S_bob)
print('-(d*C1) =', negate(S_bob))
print('Recovered P =', recovered)
assert recovered == plaintext
print('ECC decryption verified.')