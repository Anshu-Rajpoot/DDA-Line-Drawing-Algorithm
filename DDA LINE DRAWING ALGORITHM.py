#Take inputs from user
x1=int(input("Enter the first coordinate of X : "))
x2=int(input("Enter the Second coordinate of X : "))
y1=int(input("Enter the first coordinate of Y : "))
y2=int(input("Enter the seconf coordinate of Y : "))

dx=x2-x1;       #Difference in the value of x
dy=y2-y1;       #Difference in the value of y

#Finding Maximum among dx and dy using if-else
if(dx>dy):
    max=dx;
else:
    max=dy;
print("Number of Steps are ", max)

#Calculating the Increment in x and y
x_inc= dx/max;
y_inc=dy/max;
print("increment of x is : ",x_inc)
print("increment of y is : ",y_inc)
x=x1;
y=y1;
#increment the values
while(x<x2):
    x=x+x_inc;
    y=y+y_inc;
    round_off=round(y)   # Round off
    #Print Solution
    print("x is : ", x,"   Y is : ",y ,"   Round off is : " ,round_off)
