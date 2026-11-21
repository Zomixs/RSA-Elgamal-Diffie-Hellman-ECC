"""Problem 1: RSA private key calculation and message encryption."""
from math import gcd

n, e = 221, 5
p, q = 13, 17
assert p * q == n
phi = (p - 1) * (q - 1)
assert gcd(e, phi) == 1
d = pow(e, -1, phi)
print('Problem 1(a): RSA')
print(f'n={n}, e={e}, p={p}, q={q}, phi(n)={phi}, d={d}')
print(f'Check: (e*d) mod phi(n) = {(e*d)%phi}')

message = 'HOW ARE YOU'
def encode(ch):
    return 26 if ch == ' ' else ord(ch) - ord('A')
def decode(value):
    return ' ' if value == 26 else chr(ord('A') + value)
blocks = [encode(ch) for ch in message]
assert all(0 <= block < n for block in blocks)
cipher = [pow(block, e, n) for block in blocks]
print('\nProblem 1(b): Encrypt HOW ARE YOU')
print('Letter | P | C = P^5 mod 221')
for ch, block, encrypted in zip(message, blocks, cipher):
    print(f'{"SPACE" if ch == " " else ch:5}  | {block:02d} | {encrypted:03d}')
print('Ciphertext:', ' '.join(f'{c:03d}' for c in cipher))
recovered = ''.join(decode(pow(c, d, n)) for c in cipher)
print('Decrypted check:', recovered)
assert recovered == message

