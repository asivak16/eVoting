# eVoting System

This project implements a simple voting system using the Paillier cryptosystem for secure vote encryption and tallying. It consists of three main scripts:

1. `keygen.py` - Generates public and private keys for the election.
2. `cast_vote.py` - Allows voters to cast their votes.
3. `tally_vote.py` - Tallies the votes and provides the election results.

## Prerequisites

- Python 3.x
- `gmpy2` library (for precise arithmetic)

To install the required library, use:
```
pip install gmpy2
```


## Usage

### 1. Key Generation

Run `keygen.py` to generate the public and private keys required for the election.

```
python keygen.py
```

You will be prompted to enter the election name, number of candidates, and the total number of voters. The generated keys will be saved in `public_key.json` and `private_key.json`.


### 2. Casting Votes

Run `cast_vote.py` to cast a vote.

```
python cast_vote.py
```

You will be prompted to enter your vote as a number corresponding to your candidate of choice. The vote will be encrypted and saved in `votes.json`.

### 3. Tallying Votes

Run `tally_vote.py` to tally the votes and see the election results.

```
python tally_vote.py
```

The script will read the votes from `votes.json`, decrypt the tally using the private key from `private_key.json`, and display the election results.


### Files
- `keygen.py`: Generates public and private keys and election details.
- `cast_vote.py`: Encrypts and stores votes.
- `tally_vote.py`: Tallies votes and decrypts the results.
- `public_key.json`: Stores the public key and election details.
- `private_key.json`: Stores the private key.
- `votes.json`: Stores the encrypted votes.


### Example Workflow
1. Run `keygen.py` to create the keys and election details.
2. Distribute `public_key.json` to all voters.
3. Voters use `cast_vote.py` to cast their votes.
4. Collect the `votes.json` from all voters.
5. Run `tally_vote.py` to tally the votes and get the results.

###Security Considerations
- Ensure `private_key.json` is kept secure and not distributed to voters.
- `public_key.json` can be safely distributed to all voters.
