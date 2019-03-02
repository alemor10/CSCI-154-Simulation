import sys


''' function for pascal triangle'''
def displayPascalTriangle(size):
    ''' this first loop sets up the number of rows'''
    for i in range (1, size + 1 ):
        ''' this loop prints out the spaces not in the triangle '''
        for j in range( 1 , num - i + 1 ):
            print (end=" ")
        ''' this loop prints out the left side of the triangle ''' 
        for j in range (i , 0 , - 1):
            print (j , end = "")
        ''' this loop prints out the right side of the triangle '''
        for j in range (2, i + 1):
            print (j , end ="")
        ''' after printing each row we want to go to a new line'''
        print()

''' Factorial function '''
def displayFactorial (number):
   ''' if number is one then just return 1 '''
   if number == 1: 
       return 1    
   else:
        return number * displayFactorial (number - 1)


def displayEulerNumber (terms):
    totalsum = 1 
    for i in range (1 , terms + 1):
        totalsum = totalsum + (1 / displayFactorial(i))

    print ("The sum of series is", totalsum)


def displaySinValue (numberInRadians):
    pass

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

    if (userinput == "a" or input == "A"):
        num = int ( input ("Enter the height of the Pascal triangle:"))
        displayPascalTriangle(num)
        
    elif (userinput == "b" or input == "B"):
        num = int ( input ("Enter the number you want to find the factorial for:"))
        displayFactorial(num)

    elif (userinput == "c" or input == "C"):
        num =int(input("Enter the number of terms: "))
        displayEulerNumber(num)
    
    elif (userinput == "d" or input == "D"):
         num =int(input("Enter the number of in terms of radians : "))

    elif (userinput == "m" or input == "M"):
        continue

    elif (userinput == "q" or input == "Q"):
        sys.exit()


class Scrambler(object):

    def __init__(self):
        self.sentences = []
    
    ''''scramble_it():''' 



