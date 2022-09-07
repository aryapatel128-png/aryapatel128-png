# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# Assignment 03 (Translating Formulas/Math Operations.. Quadratic formula and discriminants)
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================
import math
def main(): 
    #..Input coefficients which you want to use:
    #Input A
    a = float(input("Enter the coefficient a: "))
    #Input B
    b = float(input("Enter the coefficient b: "))
    #Input C
    c = float(input("Enter the coefficient c: "))
    #..Print the Quadratic Equation: 
    print("\nQuadratic Equation is: ",a, "*X^2 +",b,"*X +",c,"= 0") 
    d = (b**2)-(4*a*c)
    #..Print the discriminant:
    print("\nThe discriminant is: ",f'{d:.2f}', "\n")
    #..Determines whether equation has two, one, or no real roots:
    if(d < 0):
        #No real roots (If "d" is less than 0)
        print("The equation has no real roots.\n")        
    elif(d == 0):
        #One real root (If "d" is equal to 0) 
        print("The equation has one real root: ", f'{-b/(2*a):.2f}',"\n" )
    else:
        #positive root
        p = (-b+(math.sqrt(d)))/(2*a)
        #negative root
        n = (-b-(math.sqrt(d)))/(2*a)
        #Two real roots (If "d" is greater than 0)
        print("The equation has two real roots: ",f'{p:.2f}', "and", f'{n:.2f}',"\n") 
        
    if(a < c and a < b):    
        #smallest coefficient is a
        print("The smallest coefficient is: ", f'{a:.2f}')
        #smallest coefficient is b
    elif(b < c and b < a): 
        print("The smallest coefficient is: ", f'{b:.2f}')
        #smallest coefficient is c
    else: 
        print("The smallest coefficient is: ", f'{c:.2f}')
        
        
        
        
        
        
    
    
main() 