import sys
import itertools
import math


#main function that handles choices
def process_choice(my_func, my_str):
    '''Handles input for Pascals triangle and Factorial '''
    user_input = ''
    num = ''
    while user_input != 'q':
        try:
            user_input = input("Enter number (q to quit): ")
            if user_input == 'q':
                break
            try:
                num = float(user_input)
            except ValueError:
                print("Enter a number!")
                continue
            if num < 0 or None:
                raise ValueError("Invalid number!")
            print (my_str.format(num, my_func(num)))
        except ValueError as excpt:
            print (excpt)

''' function for pascal triangle'''
def pascal_triangle(size):
    size = int(size)
    row = [1] #first row
    k = [0] 
    # loop through, _ because we dont need the value
    for _ in range(max(size,0)):
        print(' '.join(str(x) for x in row)) # print items in list
        row=[l+r for l,r in zip(row+k,k+row)] #get next row
    return size>=1

''' Factorial function '''
def factorial (number):
   ''' if number is one then just return 1 '''
   number = int(number)
   #base case
   if number == 0: 
       return 1    
   else:
        #recursive solution
        return number * factorial (number - 1)


def euler_number (terms):
    terms = int(terms)
    #initalize with 1
    totalsum = 1 
    for i in range (1 , terms + 1):
        #calculating euler's number with given terms
        totalsum = totalsum + (1 / factorial(i))
    return totalsum


def sin_value(rad):
    total = 0
    prev = 0
    for i in itertools.count(): # "infinite" loop
        total += pow(-1, i) * (rad**(2*i+1))/factorial(2*i+1)
        
        # break out of infinite loop
        # if within margin
        if (abs(prev-total) < 10e-8):
            break 
        else:
            prev = total
    return total

'''
Write a python script that repeatedly prompts the user to select one of the
following menu options:
A. Display a Pascal’s triangle of height H.
B. Display the value of the factorial of N.
C. Approximate and display the Euler’s number.
D. Approximate and display the value of the sine of X.
M. Display these menu options.
Q. Exit from the program.

'''

userinput = True 

while userinput:
    print("""
    Main menu:
    ------------

   A. Display a Pascal’s triangle of height H.
   B. Display the value of the factorial of N.
   C. Approximate and display the Euler’s number.
   D. Approximate and display the value of the sine of X.
   M. Display these menu options. 
   Q. Exit from the program.
    """)

    userinput=input("What would you like to do? ")
    # process choices 
    if (userinput == "a" or input == "A"):
        process_choice(pascal_triangle, "Pascal triangle of height {}")
        
    elif (userinput == "b" or input == "B"):
        process_choice(factorial, "Factorial of {} is {}")

    elif (userinput == "c" or input == "C"):
        process_choice(euler_number, "The sum of {} term series is {}")
    
    elif (userinput == "d" or input == "D"):
        process_choice(sin_value, "The sin of {} is {:.3f}")

    elif (userinput == "m" or input == "M"):
        continue

    elif (userinput == "q" or input == "Q"):
        sys.exit()

 



''' #3  Understand and comment the following code snippet and write a single line of
code that enables the class Hamburger to store as instance arguments the meat choice
and as many extras as given at the instantiation call.'''

class Hamburger:
    def __init__(self,**kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
      #   the previous  loop goes through the **kwarg arguments and uses the built in function with the value in **kwargs 
  # print the object 
    def __str__(self, sep = ''):
        return (', '.join(list(self.__dict__.values())))

burger1 = Hamburger(meat="chicken", extra1="cheese", extra2="ketchup")
print(burger1)
