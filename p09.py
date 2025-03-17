arr = [1,1,1,2,3,99,7]

arrSet = []

for i in arr:
    if(i not in arrSet):
        arrSet.append(i)

print(arrSet);