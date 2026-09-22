num=int(input("Enter the numbers"))

is_prime=True

for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print("prime number")
else:
    print("Not a prime number")