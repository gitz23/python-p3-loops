#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!") 
# #test
# happy_new_year()
    

def square_integers(int_list):
    sq_int_list = []
    for int in int_list:
       sq_num = int ** 2
       sq_int_list.append(sq_num)
    return(print(sq_int_list))
# #test
# square_integers([3,4,5,6])

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Fizz")
        else:
            print(num)
# #test
# fizzbuzz()

def reversed_string(string):
    reverse_string = ""
    for letter in string:
        reverse_string = letter + reverse_string
    return reverse_string
#test
print(reversed_string("input string"))
print(reversed_string("Eve Wambui"))
#looping through the string 
#for [each item] in [param]: