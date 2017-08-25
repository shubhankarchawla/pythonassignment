MAX=50
def cypher(n):
     string=["\0"]*MAX
     i=0
     while n>0:
             rem=n%26
             if rem==0:
                     string[i]='Z'
                     i+=1
                     n=(n/26)-1
             else:
                     string[i]=chr((rem-1)+ord('A'))
                     i+=1
                     n=n/26
     string[i]='\0'
     string=string[::-1]
     print "".join(string)
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
while(1>=a or a>=b or b>=676):
     a=int(input("enter correct value(1<a<b<676):"))
     b=int(input("enter correct value(1<a<b<676):"))
else:
     for i in range(a,b+1):
             cypher(i)