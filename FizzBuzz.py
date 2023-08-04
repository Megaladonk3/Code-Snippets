#For "Fizz" print numbers 1-100 for multiples of 3
#For "Buzz" print numbers 1-100 for multiples of 5
#For "FizzBuzz" print numbers 1-100 for multiples of 15

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue

    print(i)
