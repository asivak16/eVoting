import random
import math
import json


def generate_large_prime():
    while True:
        p = random.randint(2**45, 2**46)  
        if is_prime(p):
            return p


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def L(x, n):
    return (x - 1) // n


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


p = generate_large_prime()
q = generate_large_prime()


n = p * q


lambda_val = lcm(p - 1, q - 1)


g = random.randint(1, n**2)


g_lambda_mod = mod_exp(g, lambda_val, n**2)
mu = mod_inverse(L(g_lambda_mod, n), n)


election_name = input("Enter the Election Name: ")
num_candidates = int(input("Enter the Number of Candidates: "))
total_voters = int(input("Enter the Total Number of Voters: "))


public_key_data = {
    "PublicKey": {
        "n": n,
        "g": g
    },
    "ElectionDetails": {
        "ElectionName": election_name,
        "NumberOfCandidates": num_candidates,
        "TotalNumberOfVoters": total_voters
    }
}

with open('public_key.json', 'w') as file:
    json.dump(public_key_data, file, indent=4)


private_key_data = {
    "PrivateKey": {
        "λ": lambda_val
    }
}

with open('private_key.json', 'w') as file:
    json.dump(private_key_data, file, indent=4)

print("Public Key:")
print(json.dumps(public_key_data, indent=4))

print("Private Key:")
print(json.dumps(private_key_data, indent=4))
