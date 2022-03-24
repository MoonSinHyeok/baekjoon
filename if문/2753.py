#4배수이고 100배수 아니면 윤년, 400배수는 예외
year = int(input())

if(year%4==0 and year%100!=0):
    print(1)
elif(year%400==0):
    print(1)
else:
    print(0)
