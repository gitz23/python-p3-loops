#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
# happy_new_year()

def square_integers(int_list):
    sq_int_list = []
    for int in int_list:
        sq = int * int
        sq_int_list.append(sq)
    print (sq_int_list)
    return sq_int_list
#square_integers([2,4,6])

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) 
# fizzbuzz()        