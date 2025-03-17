arr = [1, 'c', '1', 't']
isValid = False

for i in arr:
    if(arr.count(i) > 1):
        isValid = True
        break

if(isValid):
    print('The array contains more than one copy of the same element.')
else:
    print('The array does not contain more than one copy of the same element.')
