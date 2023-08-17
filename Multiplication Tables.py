

from random import randint
from datetime import datetime
import time

count = 0

now1 = datetime.now()
print("Start time: ", now1)

print("How many multiplicaton tables do you want to practice?")
table = input("S for one table or M for multiple tables: ")

if table == "M":
    print("What is the minimum table number?: ")
    mini = int(input())
    print("What is the maximum table number?: ")
    maxi = int(input())
    times = int(input("How many questions do you want?: "))

    for x in range(0,times):
        user = 0
        multiplier1 = randint(mini, maxi)
        multiplier2 = randint(0,12)

        print((multiplier1, "x", multiplier2), "= ")
        answer = int(input())
        if answer == multiplier1 * multiplier2:
            print("Correct answer")
            count += 1
        else:
            print("Wrong answer")



if table == "S":
    m1 = int(input("What multiplication table do you want to practice?: "))
    times = int(input("How many questions do you want?: "))

    for x in range(0,times):
        user = 0
        multiplier = randint(0,12)

        print((m1, "x", multiplier), "= ")
        answer = int(input())
        if answer == m1 * multiplier:
            print("Correct answer")
            count += 1
        else:
            print("Wrong answer")

now2 = datetime.now()
print("End time: ",now2)
print("Time taken: ", now2-now1)
print("You got", float((count/times)* 100), "%")


#Multiplication table:
#    1. take input of what table and # of Qs
 #   2. for loop for # of Q's
  #  3. print for actual question
   # 4. if for checking the answer
# 5. single or multiple
#6. Time taken
#7. accuracy