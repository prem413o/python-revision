p=int(input("Enter your number: "))

sum=0
while p>0:
    sum= sum +(p%10)
    p//=10

print("the sum of digit of a number is ",sum)
