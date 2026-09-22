num=int(input("enter your number"))

first=0
second=1

for i in range(num):
    print(first)
    next_num=first+second
    first=second
    second=next_num
