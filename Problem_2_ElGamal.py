"""Problem 2: ElGamal key generation, encryption, and decryption."""
p, e1, d = 31, 3, 7
# 3 is a primitive root modulo 31.
e2 = pow(e1, d, p)
print('Problem 2(a): ElGamal keys')
print(f'p={p}, e1={e1}, d={d}, e2={e1}^{d} mod {p}={e2}')
print(f'Public key: ({p}, {e1}, {e2}); private key: {d}')

message = 'HELLO'
blocks = [ord(ch) - ord('A') for ch in message]
assert all(0 <= block < p for block in blocks)
r = 5  # Fixed only for a reproducible classroom example; never reuse r in practice.
c1 = pow(e1, r, p)
shared = pow(e2, r, p)
cipher = [(c1, (block * shared) % p) for block in blocks]
print('\nProblem 2(b): Encrypt HELLO')
print(f'r={r}, C1={c1}, shared secret={shared}')
for ch, block, pair in zip(message, blocks, cipher):
    print(f'{ch}: P={block:02d}, ciphertext={pair}')
print('Ciphertext:', cipher)

print('\nProblem 2(c): Decrypt')
recovered = []
for first, second in cipher:
    secret = pow(first, d, p)
    inverse = pow(secret, -1, p)
    block = second * inverse % p
    recovered.append(block)
    print(f'{(first, second)}: secret={secret}, inverse={inverse}, P={block:02d}')
plaintext = ''.join(chr(ord('A') + block) for block in recovered)
print('Decrypted message:', plaintext)
assert plaintext == message