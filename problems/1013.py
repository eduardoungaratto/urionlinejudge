s = str(input())

s = s.split(" ")
a = int(s [0])
b = int(s [1])
c = int(s [2])
x = (a+b+abs(a-b))/2 
x = (b+c+abs(b-c))/2
x = (a+c+abs(a-c))/2
x = (c+a+abs(c-a))/2

print(str(x)+" eh o maior")