import json
import gmpy2


def read_vote_data(file_path):
    with open(file_path, 'r') as file:
        votes = json.load(file)
    return [vote["ciphertext"] for vote in votes]


def read_private_key(file_path):
    with open(file_path, 'r') as file:
        private_key_data = json.load(file)
    return private_key_data["PrivateKey"]["λ"]


def read_public_key(file_path):
    with open(file_path, 'r') as file:
        public_key_data = json.load(file)
    return public_key_data["PublicKey"]["n"], public_key_data["PublicKey"]["g"]


def calculate_mu(g, lambda_val, n):
    def L(x, n):
        return (x - 1) // n

    n_squared = n * n
    g_lambda_mod_n_squared = pow(g, lambda_val, n_squared)
    L_g_lambda_mod_n_squared = L(g_lambda_mod_n_squared, n)
    mu = gmpy2.invert(L_g_lambda_mod_n_squared, n)
    return mu


def tally_votes(votes, n):
    n_squared = n * n
    T = 1
    for vote in votes:
        T = (T * vote) % n_squared
    return T


def decrypt_tally(T, lambda_val, mu, n):
    def L(x, n):
        return (x - 1) // n

    n_squared = n * n
    T_lambda_mod_n_squared = pow(T, lambda_val, n_squared)
    L_T_lambda_mod_n_squared = L(T_lambda_mod_n_squared, n)
    m = (L_T_lambda_mod_n_squared * mu) % n
    return m


vote_file = 'votes.json'
private_key_file = 'private_key.json'
public_key_file = 'public_key.json'


votes = read_vote_data(vote_file)
lambda_val = read_private_key(private_key_file)
n, g = read_public_key(public_key_file)


mu = calculate_mu(g, lambda_val, n)


T = tally_votes(votes, n)


decrypted_tally = decrypt_tally(T, lambda_val, mu, n)


with open(public_key_file, 'r') as file:
    data = json.load(file)
number_of_voters = data["ElectionDetails"]["TotalNumberOfVoters"]
number_of_candidates = data["ElectionDetails"]["NumberOfCandidates"]

b = number_of_voters + 1


vote_counts = {i: 0 for i in range(1, number_of_candidates + 1)}


for i in range(number_of_candidates, 0, -1):
    power = b**(i-1)
    if decrypted_tally >= power:
        count = decrypted_tally // power
        decrypted_tally -= count * power
        vote_counts[i] += count

print("Election Results:")
for candidate, count in vote_counts.items():
    print(f"Candidate {candidate}: {count} votes")
