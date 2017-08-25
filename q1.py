s='abc'
l=[]
num=int(input("enter number of strings you want:"))
for i in range(0,num):
     s=raw_input()
     l.append(s)
print(l)
l.sort(key=len)
print(l)