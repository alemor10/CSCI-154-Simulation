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


def displayFactorial (number):
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
        print ("hello")

    elif (userinput == "c" or input == "C"):
        print ("hello") 
    
    elif (userinput == "d" or input == "D"):
        print ("hello")

    elif (userinput == "m" or input == "M"):
        print ("hello")

    elif (userinput == "q" or input == "Q"):
        print ("hello")
