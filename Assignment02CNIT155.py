# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# Assignment 02 (Conversion table).
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================

def main():
    print("\t********************************************")
    print("\t*           CNIT155 Assignment 02          *")
    print("\t*                                          *")
    print("\t*           Conversion Calculator          *")
    print("\t********************************************\n\n")
    
    
    #Pounds --> Kilograms
    print("** 1st. Pounds to Kilograms conversion")
    p = float(input("What is the weight in pounds to convert it to kilograms?: "))
    #Conversion factor for pounds --> kilograms
    kg = p/2.2046 
    #Output for kilograms 
    print("The weight entered in pounds is "f'{p:.2f}',"lb and it is "f'{kg:.2f}' " Kilograms")
    
    #Celsius --> Fahrenheit
    print("\n\n** 2nd. Celsius to Fahrenheit conversion")
    c = float(input("Enter the Celsius temperature to convert it to Fahrenheit: "))
    #Conversion factor for celsius --> fahrenheit
    f = c*(9/5)+32
    #Output for fahrenheit
    print("The entered temperature in Celsius is "f'{c:.2f}',"and it is "f'{f:.2f}' "°F")
    
    #Miles --> Kilometers 
    print("\n\n** 3rd. Miles to Kilometers conversion")
    m = float(input("Enter miles to convert it to kilometers: "))
    #Conversion factor for miles --> kilometers
    km = m*1.609344
    #Output for kilometers 
    print("The entered distance in miles is "f'{m:.2f}',"and it is "f'{km:.2f}' " kilometers")
    
    #Feet and Inches --> Centimeters
    print("\n\n** 4th. Feet and Inches to Centimeters?\nWhat is your height in feet and inches?")
    feet = int(input("Feet?: "))
    i = int(input("Inches?: "))
    centi = (feet*12*2.54)+(i*2.54)
    print("The entered height is",feet,"feet",i,"inch and it is", centi, "cm")
    
main() 
    
    