def factorial(num):
    if num==2:
        return (num)
    else:
        fact= int(num)*(factorial(int(num)-1))
        return fact 
a=factorial(input("enter any number: "))
print (a) 
