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
        print ("hello")
        
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