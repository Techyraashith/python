a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
if a > b and b > c:
    biggest = a 
elif b > a and c > b:
    biggest = b    
else :                                           
     biggest = c 

print("The biggest of the three no:",biggest)
    
 