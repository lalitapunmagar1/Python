def encryptRailFence(message, key):
    rail = [['\n' for _ in range(len(message))] for _ in range(key)]
    down = False
    row, col = 0, 0

    for char in message:
        if row == 0 or row == key - 1:
            down = not down
        rail[row][col] = char
        col += 1
        row += 1 if down else -1

    cipherText = ''.join(char for row in rail for char in row if char != '\n')
    return cipherText

def decryptRailFence(cipherText, key):
    rail = [['\n' for _ in range(len(cipherText))] for _ in range(key)]
    down = False
    row, col = 0, 0

    for _ in cipherText:
        if row == 0 or row == key - 1:
            down = not down
        rail[row][col] = '*'
        col += 1
        row += 1 if down else -1

    index = 0
    for r in range(key):
        for c in range(len(cipherText)):
            if rail[r][c] == '*' and index < len(cipherText):
                rail[r][c] = cipherText[index]
                index += 1

    message = []
    row, col = 0, 0
    down = False
    for _ in cipherText:
        if row == 0 or row == key - 1:
            down = not down
        message.append(rail[row][col])
        col += 1
        row += 1 if down else -1

    return ''.join(message)

# Example Usage with "CHOCOLATE" 🍫
message = "EXAMPLE"
key = 3

encrypted_text = encryptRailFence(message, key)
decrypted_text = decryptRailFence(encrypted_text, key)

print("Original Message:", message)
print("Encrypted Message:", encrypted_text)
print("Decrypted Message:", decrypted_text)

