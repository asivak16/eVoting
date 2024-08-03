import random
import json


with open('public_key.json', 'r') as file:
    data = json.load(file)
    n = data["PublicKey"]["n"]
    g = data["PublicKey"]["g"]
    number_of_candidates = data["ElectionDetails"]["NumberOfCandidates"]
    number_of_voters = data["ElectionDetails"]["TotalNumberOfVoters"]


b = number_of_voters + 1


m_mapping = {i: b**(i-1) for i in range(1, number_of_candidates + 1)}
print(m_mapping )


while True:
    try:
        m = int(input(f"Enter a message (1-{number_of_candidates}): "))
        if 1 <= m <= number_of_candidates:
            break
        else:
            print(f"Please enter a number between 1 and {number_of_candidates}.")
    except ValueError:
        print(f"Invalid input. Please enter an integer between 1 and {number_of_candidates}.")

m_transformed = m_mapping[m]


r = random.randint(1, n-1)


n_squared = n * n
c = (pow(g, m_transformed, n_squared) * pow(r, n, n_squared)) % n_squared

print(f"Public key (n, g): ({n}, {g})")
print(f"Message m: {m_transformed}")
print(f"Random number r: {r}")
print(f"Ciphertext c: {c}")


vote_data = {"ciphertext": c}

try:
    with open('votes.json', 'r') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = []

votes.append(vote_data)

with open('votes.json', 'w') as file:
    json.dump(votes, file, indent=4)
