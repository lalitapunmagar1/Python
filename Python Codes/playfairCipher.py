import numpy as np

def findIndex(matrix, letter):
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == letter:
                return r, c
    return None  # Return None if the letter is not found (though it should always be found)

def encryptMessage(message, key):
    keyMatrix = generateMatrix(key)
    message = message.replace(" ", "").upper()

    # Prepare message for encryption
    message = list(message)
    cipherText = ""
    
    i = 0
    while i < len(message):
        if i == len(message) - 1 or message[i] == message[i + 1]:  
            digraph = [message[i], 'X' if message[i] != 'X' else 'Q']
            i += 1  # Move one step if padding is needed
        else:
            digraph = [message[i], message[i + 1]]
            i += 2  # Move two steps normally
        
        r1, c1 = findIndex(keyMatrix, digraph[0])
        r2, c2 = findIndex(keyMatrix, digraph[1])
        
        if r1 == r2:  # Same row
            cipherText += keyMatrix[r1][(c1 + 1) % 5] + keyMatrix[r1][(c2 + 1) % 5]
        elif c1 == c2:  # Same column
            cipherText += keyMatrix[(r1 + 1) % 5][c1] + keyMatrix[(r2 + 1) % 5][c1]
        else:  # Rectangle swap
            cipherText += keyMatrix[r1][c2] + keyMatrix[r2][c1]

    return cipherText

def generateMatrix(key):
    key = key.upper()
    matrix = []
    keyMatrix = [[None for _ in range(5)] for _ in range(5)]
    
    # Remove duplicates from the key
    for char in key:
        if char not in matrix:
            matrix.append('I' if char in ('I', 'J') else char)

    # Fill remaining letters
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # No 'J' (combined with 'I')
    for char in letters:
        if char not in matrix:
            matrix.append(char)

    # Fill the 5x5 matrix
    count = 0
    for row in range(5):
        for col in range(5):
            keyMatrix[row][col] = matrix[count]
            count += 1

    return keyMatrix

# Example usage
message = "Secret"
key = "Lalita"
encrypted_message = encryptMessage(message, key)
print("Encrypted Message:", encrypted_message)

