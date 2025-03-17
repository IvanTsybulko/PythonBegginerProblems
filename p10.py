#Cesar cript
str =  "abzABZ"

criptedStr = ""

for c in str:
    c = ord(c) + 3

    if c > ord('z') or c > ord('Z') and c < ord('a'):
        c -= 26

    criptedStr += chr(c)

print(criptedStr)