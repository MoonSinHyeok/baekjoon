def include(s):
    result = []
    for i in range(97, 123):
        check = True
        for j, letter in enumerate(s):
            if ord(letter) == i:
                result.append(j)
                check = True
                break
            else:
                check = False
            
        if(check == False):
            result.append(-1)

    return result

for i in include(input()):
    print(i, end=" ")
