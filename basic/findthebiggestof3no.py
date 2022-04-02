n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
n3=int(input("enter the third no:"))
if n1 > n2  and n1 > n3:
    biggest =n1 
elif n2 > n1 and n2 > n3:
    biggest = n2    
else :                                       
     biggest = n3 

print("The biggest of the three no:",biggest)
    
 