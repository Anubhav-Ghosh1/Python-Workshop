n = int(input("Enter Number: "))
count = 0
for i in range(2,n,1):
    if (n%i)==0:
            count = count + 1
if count == 0:
    print("Prime number")
else:
    print("Not a prime number")
