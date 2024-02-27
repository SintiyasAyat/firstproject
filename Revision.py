print("Hello World")
a = 10
b = 3
c = "Sintyas Ayat"
print(f"My Name is {c} & My class roll is {a//b}")
d = [1,2,3,4,5]
dd = bytes(d)
print(type(d))
print(dd)
e = [1,2,3,4,5]
ee = bytearray(e)
print(type(ee))
print(ee)
ee[0]=6
print(ee)
print(a>=b)
print(a<=b)
print(type(a!=b))
f = ("Sintiyas",a!=b,a+10)
print(type(f))
print(f)
g = range(0,11)
print(type(g))
for h in g:
    print(h)
i = ["Sintiyas","Sintiyas","Sintiyas",a//3]
print(type(i))
print(i)
i[0]="Mahmudul"
i.insert(1,"Hasan")
i.append("Ayat")
i.remove(a//3)
i.pop(2)
print(i)
ii = 0
while ii < len(i):
    print(i[ii])
    ii = ii + 1
i.sort()
print(i)
i.sort(reverse=True)
print(i)
for h in range(len(i)):
    print(h)
j = ["Lisan","Hasib","Abrar","Hamim"]
J = i + j
print(J)
j.extend(i)
print(j)
j.clear()
print(j)
print(a)
print(b)
a,b=b,a
print(a)
print(b)
a+=b
print(a)
print(b)
A = (1,2,3,4,5)
for AA in A:
    print(AA * 2)
BB =[B + 2 for B in A]
print(BB)
N = None
print(type(N))
print(N)
x = input("Enter your Name : ")
print(x)
s = "30"
print(type(s))
print(s)
print(int(s))
print(type(int(s)))