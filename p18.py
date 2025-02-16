n=int(input("Enter your number: "))

def fact(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return fact(n-1)*n
    

result=fact(n)
print("the factorial of a number is ",result)
