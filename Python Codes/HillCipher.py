import numpy as np

# Function to calculate the modular inverse of a matrix
def mod_inverse(matrix, mod):
    det = int(round(np.linalg.det(matrix))) % mod  # Compute determinant
    try:
        det_inv = pow(det, -1, mod)  # Compute modular inverse of determinant
    except ValueError:
        raise ValueError("Matrix determinant has no modular inverse under mod 26. Choose a different key matrix.")

    # Compute adjugate matrix (cofactor matrix transposed)
    matrix_cofactor = np.linalg.inv(matrix) * np.linalg.det(matrix)  # Compute cofactor matrix
    matrix_adj = np.round(matrix_cofactor).astype(int) % mod  # Adjugate matrix

    return (det_inv * matrix_adj) % mod  # Compute inverse in mod 26

# Function for Hill cipher encryption
def hill_encrypt(plaintext, key):
    mod = 26
    n = len(key)

    # Pad plaintext to be a multiple of key matrix size
    while len(plaintext) % n != 0:
        plaintext += 'X'  # Padding with 'X'

    # Convert plaintext to numerical values (A=0, B=1, ..., Z=25)
    plaintext_numbers = [ord(char) - ord('A') for char in plaintext.upper()]

    # Encrypt the message
    ciphertext_numbers = []
    for i in range(0, len(plaintext_numbers), n):
        block = np.array(plaintext_numbers[i:i+n])
        encrypted_block = np.dot(key, block) % mod
        ciphertext_numbers.extend(encrypted_block)

    # Convert numerical ciphertext back to letters
    ciphertext = ''.join(chr(num % mod + ord('A')) for num in ciphertext_numbers)
    return ciphertext

# Function for Hill cipher decryption
def hill_decrypt(ciphertext, key):
    mod = 26
    n = len(key)

    # Compute modular inverse of key matrix
    key_inv = mod_inverse(key, mod)

    # Convert ciphertext to numerical values
    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext.upper()]

    # Decrypt the message
    decrypted_numbers = []
    for i in range(0, len(ciphertext_numbers), n):
        block = np.array(ciphertext_numbers[i:i+n])
        decrypted_block = np.dot(key_inv, block) % mod
        decrypted_numbers.extend(decrypted_block)

    # Convert numerical decrypted message back to letters
    decrypted_text = ''.join(chr((num + mod) % mod + ord('A')) for num in decrypted_numbers)
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key_matrix = np.array([[3, 10, 20], [20, 9, 17], [23, 5, 6]])  # Example 3x3 key matrix
    plaintext = "SECRET"

    encrypted = hill_encrypt(plaintext, key_matrix)
    print(f"Encrypted: {encrypted}")

    decrypted = hill_decrypt(encrypted, key_matrix)
    print(f"Decrypted: {decrypted}")

