# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# In Lab 06 (User defined functions using while loops and if statements.. area of triangle and minimum/maximum variable) 
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================
import math
def printInfo(): #This is all the information you will need to know about me 
    print("\t***************************************")
    print("\t* Arya Patel                          *")
    print("\t* pate1496@purdue.edu                 *")
    print("\t***************************************")    
def Validate(a,b,c): #This will help validate the program to make sure the variables are correctly organized
    if a + b <= c or a + c <= b or b + c <= a: 
        return False #Returns False 
  
    else:
        return True #Returns True 
    
def ComputeArea(a,b,c): #This will compute the area of the triangle using Herons Formula 
    s = (a+b+c)/2.0 
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))     
    return area 
           
def FindMin(a,b,c): #Finds the minimum valued variable 
    if a <= b and a <= c:
        min = a 
    elif b <= a and b <= c:
        min = b 
    else:
        min = c
    return min 
        
def FindMax(a,b,c): #Finds the maximum valued variable 
    if a >= b and a >= c: 
        max = a 
    elif b >= a and b >= c:
        max = b
    else: 
        max = c 
    return max

        
def main(): #MAIN FUNCTION 
    printInfo()
    while True:
        a = int(input("Enter the length of side A of a Triangle: ")) #input A
        b = int(input("Enter the length of side B of a Triangle: ")) #input B
        c = int(input("Enter the length of side C of a Triangle: ")) #input C
        print("\nValidating a triangle...\n") #Prints if its valid below 
        if Validate(a,b,c) == True: 
            area = ComputeArea(a,b,c) #Variable for area 
            print("This is a valid triangle")
            print("The area of the triangle is",f'{area:.2f}') #Prints the area and below this will print the minimum and maximum 
            print("The smallest side is", FindMin(f'{a:.1f}',f'{b:.1f}',f'{c:.1f}'),"and the largest side is",FindMax(f'{a:.1f}',f'{b:.1f}',f'{c:.1f}'))
        else:
            print("Inputs cannot form a triangle. Please enter differnt numbers!") #Cannot form a triangle please enter valid values
            continue
        while True: 
            yn = str(input("Do you want to compute again? (Y/N): ")) #Would you like to continue and try again?
            if yn == "Y" or yn == "y":
                break  
            elif yn == "N" or yn == "n": 
                print("End of the program") #Program will stop 
                return
            else: 
                print("Invalid input\nPress Y or N, case-insensitive") #Not a valid input, please try again
            
main()
             
    
    
    

    