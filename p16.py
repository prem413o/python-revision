a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))

def average(a,b,c):
    sum=a+b+c
    aver= sum/3
    return aver

result=average(a,b,c)

print("the average of three number is ",result)