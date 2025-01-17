print("part one")
def encrypted(text,n,m):
    encrypted_text = ""
    for char in text:
        # For lowercase letters (a-m)
        if 'a' <=char <='m':
        encrypted_text+= chr(((ord(char)-ord('a')+ n*m)%26)+ord('a'))
        # For lowercase letters (n-z)elif 'n'<=char<='z':
        encrypted_text 



