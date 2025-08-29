def encryptMessage(plainText, key):
    cipherText = ''
    key = (key * ((len(plainText) // len(key)) + 1))[:len(plainText)]  # Repeat and trim key to match text length
    count = 0
    
    for letter in plainText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shifter = lowerCase.index(key[count].lower())  # Ensure key character is in lowercase
            shiftedIndex = (index + shifter) % 26
            cipherText += lowerCase[shiftedIndex]
            count += 1
        elif letter in upperCase:
            index = upperCase.index(letter)
            shifter = lowerCase.index(key[count].lower())  # Ensure key character is in lowercase
            shiftedIndex = (index + shifter) % 26
            cipherText += upperCase[shiftedIndex]
            count += 1
        else:
            cipherText += letter  # Keep non-alphabet characters unchanged
            count += 1

    return cipherText


def decryptMessage(cipherText, key):
    plainText = ''
    key = (key * ((len(cipherText) // len(key)) + 1))[:len(cipherText)]  # Repeat and trim key to match text length
    count = 0

    for letter in cipherText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shifter = lowerCase.index(key[count].lower())  # Ensure key character is in lowercase
            shiftedIndex = (index - shifter) % 26
            plainText += lowerCase[shiftedIndex]
            count += 1
        elif letter in upperCase:
            index = upperCase.index(letter)
            shifter = lowerCase.index(key[count].lower())  # Ensure key character is in lowercase
            shiftedIndex = (index - shifter) % 26
            plainText += upperCase[shiftedIndex]
            count += 1
        else:
            plainText += letter  # Keep non-alphabet characters unchanged
            count += 1

    return plainText


# Create uppercase and lowercase letter mappings
upperCase = [chr(i) for i in range(65, 91)]
lowerCase = [chr(i) for i in range(97, 123)]

# User input and encryption
message = input('Enter your Message: ')
key = 'Lalitkey'

cipherText = encryptMessage(message, key)
print(f'Your encrypted Message: {cipherText}')

# Decryption
key2 = input('Please enter the secret key to decrypt the message: ')
plainText = decryptMessage(cipherText, key2)

print(f'Your hidden message is: {plainText}')

