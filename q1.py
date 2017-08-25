s='abc'
l=[]
num=int(input("enter number of strings you want:"))
print("enter the strings-")
for i in range(0,num):
     s=raw_input()
     l.append(s)
print(l)
l.sort(key=len)
print(l)
