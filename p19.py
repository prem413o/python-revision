a=int(input("Enter your number: "))

def sum(a):
    if(a==1):
        return 1
    else:
        return sum(a-1)+a
    
result=sum(a)
print("the sum of first ",a,"natural number is ",result)
