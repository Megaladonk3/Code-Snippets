#Find if a number is a prime number
num = int(input("Enter a number: "))
rem = 0
for x in range(2,num):
    if num % x == 0:
        rem = 1
        break

if rem == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#___________________________________________________________________________

#Find all the prime numbers from 1 to 100
num = 101
for x in range(2, num):
    rem = 0

    for y in range(2, x):
        if x % y == 0:
            rem = 1
            break

    if rem == 0:
        print(x, " is a prime number\n")

