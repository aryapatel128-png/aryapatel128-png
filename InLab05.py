# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# In Lab 05  (For loops and Nested Loops with pyramids and triangles)
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================

def main(): 
    option = 0
    while option != 5: #Large while loop for entire project    
        print("\t\t\tFor Loops Lab")
        print("======================================================================")
        print("1. Display and Add natural numbers from N to 1\n2. The Multiplication table of N\n3. The Pyramid of Stars")
        print("4. The Pyramid of Numbers\n5. Exit")
        print("======================================================================")
    
        option = int(input("Choose one of options to perform: ")) #Prompts user to choose an option they desire
        #=====================================================================================
        if option == 1: #Option 1 (Display and Add natural numbers from N to 1)
            n = int(input("Enter a natural number for N: "))
            sum = 0 
            print("Displaying natural numbers from",n,"to 1")
            for i in range(n,0,-1): #For loop for displaying and adding natural numbers
                print(i)
                sum = sum + i
            print("The sum of natural numbers from",n,"to 1: ",sum)
        #=====================================================================================
        elif option == 2: #Option 2 (The Multiplication table of N)
            n = int(input("Enter a natural number for N: "))
            print("The Multiplication table of",n)
            for i in range(1,11): #For loop for multiplication table 
                p = n*i
                print(n," * ",i," = ",p)            
        #=====================================================================================
        elif option == 3: #Option 3 (The Pyramid of Stars)
            n = int(input("Enter a number to define the number of the rows of *: "))
            for i in range(0,n): #Nested for loop for the pyramid of stars
                for j in range(0,i+1):
                    print("* ",end='')
                print();
        #=====================================================================================        
        elif option == 4: #Option 4 (The Pyramid of Numbers) 
            n = int(input("Enter a number to define the number of the rows of numbers: "))
            for i in range(n,0,-1): #Nest for loop for pyramid of numbers
                for j in range(1,i+1):
                    print(j,end=' ')
                print();            
        #===================================================================================== 
        elif option == 5: #Good Bye!
            print("Good Bye!")
        #=====================================================================================
        else: #Please choose a valid option between 1 and 5
            print("Invalid option!\nPlease choose an option between 1 and 5") 
    

main()
            
                
                    
            
            
            
        
        
                