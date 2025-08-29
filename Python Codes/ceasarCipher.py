def encryptMessage(plainText, key):
    cipherText = ''
    for letter in plainText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shiftedIndex = (index + key) % 26
            cipherText += lowerCase[shiftedIndex]
        elif letter in upperCase:
            index = upperCase.index(letter)
            shiftedIndex = (index + key) % 26
            cipherText += upperCase[shiftedIndex]
        else:
            cipherText += letter  # Non-alphabetic characters remain unchanged
    return cipherText

def decryptMessage(cipherText, key):
    plainText = ''
    for letter in cipherText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shiftedIndex = (index - key) % 26
            plainText += lowerCase[shiftedIndex]
        elif letter in upperCase:
            index = upperCase.index(letter)
            shiftedIndex = (index - key) % 26
            plainText += upperCase[shiftedIndex]
        else:
            plainText += letter
    return plainText

# Creating uppercase and lowercase letter lists
upperCase = [chr(i) for i in range(65, 91)]  # A-Z
lowerCase = [chr(j) for j in range(97, 123)]  # a-z

# Input from user
message = input("Enter your message here: ")
key = int(input("Enter your key here: "))  # Convert key to integer

# Encrypt message
ciphertext = encryptMessage(message, key)
print(f'Others will see: {ciphertext}')

# Decrypt message
key2 = int(input("Please enter the key to decrypt your message: "))  # Convert key to integer
plainText = decryptMessage(ciphertext, key2)
print(f'Hidden Message seen by receiver: {plainText}')
