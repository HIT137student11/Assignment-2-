def encrypt(text, n, m):
    encrypted_text = ""
    
    for char in text:
        # For lowercase letters (a-m)
        if 'a' <= char <= 'm':
            encrypted_text += chr(((ord(char) - ord('a') + n * m) % 26) + ord('a'))
        # For lowercase letters (n-z)
        elif 'n' <= char <= 'z':
            encrypted_text += chr(((ord(char) - ord('a') - (n + m)) % 26) + ord('a'))
        # For uppercase letters (A-M)
        elif 'A' <= char <= 'M':
            encrypted_text += chr(((ord(char) - ord('A') - n) % 26) + ord('A'))
        # For uppercase letters (N-Z)
        elif 'N' <= char <= 'Z':
            encrypted_text += chr(((ord(char) - ord('A') + m**2) % 26) + ord('A'))
        else:
            # Special characters and numbers remain unchanged
            encrypted_text += char
            
    return encrypted_text


def decrypt(text, n, m):
    decrypted_text = ""
    
    for char in text:
        # For lowercase letters (a-m)
        if 'a' <= char <= 'm':
            decrypted_text += chr(((ord(char) - ord('a') - n * m) % 26) + ord('a'))
        # For lowercase letters (n-z)
        elif 'n' <= char <= 'z':
            decrypted_text += chr(((ord(char) - ord('a') + (n + m)) % 26) + ord('a'))
        # For uppercase letters (A-M)
        elif 'A' <= char <= 'M':
            decrypted_text += chr(((ord(char) - ord('A') + n) % 26) + ord('A'))
        # For uppercase letters (N-Z)
        elif 'N' <= char <= 'Z':
            decrypted_text += chr(((ord(char) - ord('A') - m**2) % 26) + ord('A'))
        else:
            # Special characters and numbers remain unchanged
            decrypted_text += char
            
    return decrypted_text


def check_decryption(original_text, decrypted_text):
    return original_text == decrypted_text


# Read the file
with open('raw_text.txt', 'r') as file:
    raw_text = file.read()

# Get user inputs
n = int(input("Enter value for n: "))
m = int(input("Enter value for m: "))

# Encrypt the text
encrypted_text = encrypt(raw_text, n, m)
# Write encrypted text to a new file
with open('encrypted_text.txt', 'w') as file:
    file.write(encrypted_text)

# Decrypt the text to verify
decrypted_text = decrypt(encrypted_text, n, m)

# Check if the decryption is correct
if check_decryption(raw_text, decrypted_text):
    print("Decryption is successful!")
else:
    print("Decryption failed!")


