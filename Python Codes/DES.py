import random

# Initial 56-bit key permutation (PC-1)
PC1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

# Permutation Choice 2 (PC-2)
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Example S-Box (S1)
S_BOX = [
    [3, 15, 0, 6, 12, 9, 5, 10, 2, 7, 8, 14, 1, 4, 13, 11],
    [8, 2, 11, 13, 5, 14, 7, 0, 12, 6, 10, 3, 4, 9, 15, 1],
    [6, 1, 14, 4, 9, 8, 3, 13, 10, 15, 5, 11, 0, 7, 2, 12],
    [7, 13, 4, 8, 11, 1, 0, 5, 10, 2, 9, 6, 15, 3, 14, 12]
]

# Function to permute data based on a given table
def permute(data, table):
    return [data[i - 1] for i in table]

# Function to perform left circular shift
def left_shift(key_half, shifts):
    return key_half[shifts:] + key_half[:shifts]

# Function to generate 16 round keys
def generate_keys(initial_key):
    key = permute(initial_key, PC1)  # Apply PC-1
    C, D = key[:28], key[28:]  # Split key into two halves
    keys = []

    # Shift and generate round keys
    for shift in [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        keys.append(permute(C + D, PC2))  # Apply PC-2
    return keys

# Function to apply S-Box substitution
def sbox_substitution(block):
    row = int(f"{block[0]}{block[5]}", 2)  # First and last bits form row
    col = int(f"{''.join(map(str, block[1:5]))}", 2)  # Middle bits form column
    return format(S_BOX[row][col], '04b')  # Convert S-Box output to 4-bit binary

# Generate a random 64-bit key
def generate_random_key():
    return [random.randint(0, 1) for _ in range(64)]

# Example Usage
message = "ALGORITHM"
key = generate_random_key()

print("Original Message:", message)
print("Generated Key:", ''.join(map(str, key)))

round_keys = generate_keys(key)
print("First Round Key:", ''.join(map(str, round_keys[0])))

sample_block = [random.randint(0, 1) for _ in range(6)]
print("Sample Block:", ''.join(map(str, sample_block)))
print("S-Box Output:", sbox_substitution(sample_block))

