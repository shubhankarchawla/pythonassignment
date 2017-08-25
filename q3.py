flag=0
def factor(x):
     global flag
     for i in range(2,x/2+1):
             if x%i==0:
                     print(i)
                     flag=1
     if flag==1:
             print("number is not prime")
     else:
             print("number is prime")

num=int(input("enter number:"))
while(num>=100000):
     num=int(input("enter value less than 100000:"))
else:
     factor(num)