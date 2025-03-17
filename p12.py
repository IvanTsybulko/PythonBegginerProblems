dict = {'Bobi': 3, 'Ivan': 8, 'Ceci' : 3, 'Didi' : 3}

#1
print([k for k, v in dict.items() if v == 3])

#2
for k,v in dict.items():
    if v == 3:
        print(k)