Num_list = set(range(1, 10001))
D_Num_list = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    D_Num_list.add(i)

Self_Num = sorted(Num_list - D_Num_list)
for i in Self_Num:
    print(i)
