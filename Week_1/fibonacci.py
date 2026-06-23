def fibo(num):
    if num==0 or num==1:
        return 1
    else:
        return fibo(int(num)-1)+fibo(int(num)-2)
a=fibo(int(input("enter any number: ")))
print (a)
