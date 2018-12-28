s = str(raw_input())

s = s.split(" ")

a = int(s[0])
b = int(s[1])
c = int(s[2])
x = int((a+b+abs(a-b))/2)
x = int((b+c+abs(b-c))/2)
x = int((a+c+abs(a-c))/2)

print(str(x)+" eh o maior")