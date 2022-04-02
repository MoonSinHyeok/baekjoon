def sum(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum

N = int(input())
print(sum(input()))
