changeIndex = "abcc"
index = 0

str = "abcABCabc"
criptedStr =""

def letter_position(letter):
    return ord(letter.lower()) - ord('a') + 1  # 'a' = 1, 'b' = 2, ..., 'z' = 26

for c in str:
    c = ord(c)+letter_position(changeIndex[index])

    if c > ord('z') or c > ord('Z') and c < ord('a'):
        c -= 26

    criptedStr += chr(c)
    index+=1
    if index == len(changeIndex):
        index = 0

print(criptedStr)
