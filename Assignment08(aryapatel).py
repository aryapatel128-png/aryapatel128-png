# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# Assignment 08 (lists with name,ID,Price, average of price, and discounted price list + discounted average and price list <=100)
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================
def Discount(lst): # discount function 
    updated = [] # updated empty list 
    lst1 = ['Book','Tea','Soda','Shoes','Mug','TV'] # lst1 which contains all names 
    lst2 = [100,101,102,103,104,105] # lst2 which contains all ID's 
    print("\tName\t\tID\t\tPrice") 
    print("==================================================")    
    for i in range(len(lst)):
        discountPrice = lst[i] * .7 # discount formula  
        updated.append(discountPrice) 
    for j in range(len(lst)):
        print("\t",lst1[j],"\t\t",lst2[j],"\t\t",f'{updated[j]:.2f}') # prints discount list 
    
    return updated 
    
def PrintInfo(lst1,lst2,lst3): # print-info function 
    print("\tName\t\tID\t\tPrice")
    print("==================================================")
    for i in range(0, len(lst1) ):
        print("\t",lst1[i],"\t\t",lst2[i],"\t\t",f'{lst3[i]:.2f}') # prints lists (all generic information)         
        

def Search(lst1,lst2,lst3):  # search function 
    for i in range(len(lst3)):                
        if lst3[i] <= 100.0: # less than or equal to 100 
            print("\t",lst1[i],"\t\t",lst2[i],"\t\t", f'{lst3[i]:.2f}')  # prints values which fit the criteria 

def Average(lst3): # average function 
    sum = 0 
    for i in (lst3): 
        sum = i + sum
    average = sum/6 # basic average formula 

    return average
def main(): 
    lst1 = ['Book','Tea','Soda','Shoes','Mug','TV'] # lst1 which contains all names
    lst2 = [100,101,102,103,104,105] # lst2 which contains all ID's
    lst3 = [130.00,153.00,221.00,117.00,55.00,200.00] # lst3 which contains all of the prices 
    
    print("**************************************************")
    print("**********                              **********")
    print("**********         Assignment 08        **********")
    print("**********                              **********")
    print("**************************************************")
    
    PrintInfo(lst1,lst2,lst3) # calls print-info function into main 
    
 
    print("\n**************************************************")
    print("==================== Averages ====================")
    print("\nThe average of prices before the discount is $",f'{Average(lst3):.2f}') # prints the average of prices before discount
    print("\n\n**************************************************")
    print("Prices have been adjusted!\n")
    
    discountedPrices = Discount(lst3) # calls discount function into main 
    
    print("\n**************************************************")
    print("==================== Averages ====================")
    print("\nThe average of prices after the discount is $",f'{Average(discountedPrices):.2f}') # prints the average of prices after discount    
    
        
    print("\n============  Price(s) under <= $100 =============") 
    print("\tName\t\tID\t\tPrice") 
    print("==================================================") 
    Search(lst1,lst2,discountedPrices) # calls search function into main 


main()