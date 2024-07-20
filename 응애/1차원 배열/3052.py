List = []
for i in range(10):
  List.append(int(input())%42)

List = list(set(List))
print(len(List))
