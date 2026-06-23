def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True
print(isprime(7))

        
