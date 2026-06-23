def fibo(length):
    mylist =[1,1]
    if length<=2:
        return mylist
    else:
        for i in range(length):
            val=mylist[-1]+mylist[-2]
            print(val)
            mylist.append(val)
            return mylist
#a=fibo(int(input("enter any number")))
print (fibo(7)) 