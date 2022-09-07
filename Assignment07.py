# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# Assignment 07 (User defined functions while using while and for loops as well as if statements to find Factorials, SumOdds, SumInverse and FindChar) 
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================
def Factorial(): #User Defined function 1 
    n = int(input("Please enter a natural number for n: ")) #Natural number for n
    factorial = 1    
    for i in range(1,n+1): 
        factorial = factorial * i
    print(n,"!=",factorial)
#======================================================================================================================================                
def SumOdds(): #User Defined function 2
    n1 = int(input("Please enter a natural number for n1: ")) #Num1
    n2 = int(input("Please enter a natural number for n2: ")) #Num2    
    sum = 0
    if n1%2==0:
        n1 = n1 + 1   
    for i in range(n1,n2+1,2):
        print (n1)
        sum = sum + n1
        n1 = n1 + 2
    print("The sum of the odd numbers is:",sum)     
#======================================================================================================================================                
def SumInverse(): #User Defined function 3
    n1 = int(input("Please enter a natural number for n1: ")) #Num1
    n2 = int(input("Please enter a natural number for n2: ")) #Num2
    print("Displaying the inverse of the numbers from n1 to n2 (n1<=n2)") 
    sum = 0 
    for i in range(n1,n2+1): 
        print("1 /",i)
        num = 1/i 
        sum = sum + num
    print("The sum of the inverse of the numbers between n1 and n2 is",f'{sum:.2f}')
#======================================================================================================================================            
def FindChar(): #User Defined function 4
    count = 0
    sentence = str(input("Please enter the string to work on: ")) #Sentence 
    char = str(input("Please enter a character that you want to count in the string entered above: ")) #Character
    sentence = sentence.lower() 
    char = char.lower()     
    for i in (sentence): 
        if i == char:
            count = count + 1 
    print("The character",char,"appeared",count,"times\n") 
    
def main(): #Main function 
    option = 0
    while option != 5: #Important while loop in order for the code to continuously run 
        print("==============   User Defined Functions Menu   ==============") #title 
        print("1. Compute n Factorial\n2. Sum of all odd numbers from n1 to n2 (n1<=n2)") #Menu option 1 and 2 
        print("3. Sum of the inverse of the numbers between n1 and n2 (n1<=n2)\n4. Find the Number of Characters") #Menu option 3 and 4
        print("5. Exit") #Menu option Exit = 5
        print("=============================================================\n")
    
        option = int(input("Choose one of the options to perform: ")) 
        if option == 1: #Prints Option 1
            print("1. Compute n Factorial") 
            Factorial() #User Defined function 1
        elif option == 2: #Prints Option 2
            print("2. Sum of all odd numbers from n1 to n2 (n1<=n2)")
            SumOdds() #User Defined function 2
        elif option == 3: #Prints Option 3
            print("3. Sum of the inverse of the numbers between n1 and n2 (n1<=n2)")
            SumInverse() #User Defined function 3           
        elif option == 4: #Prints Option 4
            print("4. Find the Number of Characters")
            FindChar() #User Defined function 4
        elif option == 5: #Prints Option 5
            print("Bye!") #User Defined function 5
        else:
            print("Invalid option! Enter a number from 1 and 5.")

main()
        