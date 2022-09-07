# ========================================================================
# Arya Patel & Friday 1:30p
# pate1496@purdue.edu 
# InLab07 ()
# Academic Honesty: 
# I attest that this is my original work.
# I have not used unauthorized source code, either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
# ========================================================================
def main(): 
    n = int(input("How many students are there in your class?: ")) 
    students = []
    gpa = []    
    for i in range(0,n):
        name = (input("Input student #" + str(i+1) + " name: "))
        students.append(name)
        gpas = float(input("Input student #" + str(i+1) + " GPA: "))
        while True:
            if gpas < 0 or gpas > 4.0:
                print("A GPA must be between 0 and 4.0 (both inclusive!)!\n") 
                gpas = float(input("Input student #" + str(i+1) + " GPA: "))
                continue
            else:
                break
        gpa.append(gpas)
        
    print("================ List ================") 
    print("        Name            GPA")
    print("    ------------     ----------")
    for i in range (len(students)):
        print("\t",students[i],"\t\t",str(gpa[i]))   
    sum = 0
    for i in range(n):
        sum = gpa[i] + sum
    average = sum/n
    print("============================================")
    print("The average of entered GPAs is ",f'{average:.2f}')
    print("The maximum GPA is ",f'{max(gpa):.2f}')
    print("The minimum GPA is ",f'{min(gpa):.2f}')
    print("============================================")
    
    
    
        
            
    
main() 