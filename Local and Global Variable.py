a=10 #global -> Whenever we will ask the value of A it will use this value as the value of a .
def add():
    b=20
    c=a+b
    print(c)
    a=50 #local-> Cause it is stored in add function and will not execute untill add functiom is called out.
    d=a+b
    print(d)
print (a)
add()
def sub():
    b=15
    c=a-b
    print(c)
