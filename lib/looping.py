#!/usr/bin/env python3

def happy_new_year():
    for i in range (10,0, -1):
        print(i)

    print("Happy New Year!")
        

def square_integers(int_list):
   squared_ints = [num ** 2 for num in int_list]
   return squared_ints

def fizzbuzz():
    for i in range (1, 101, 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
