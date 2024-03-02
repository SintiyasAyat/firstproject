print("Hello World")
a = 10
b = 3
c = "Sintiyas Ayat"
print(f"My Name is {c} & My class roll is {a//b}")
d = (1,2,3,4,5)
dd = bytes(d)
print(dd)
e = (1,2,3,4,5)
ee = bytearray(e)
print(ee)
ee[0]=6
print(ee)
print(a!=b)
print(b**a)
f = (1,"Sintiyas",a>b,a+b)
print(f)
g = list(f)
g[0]="Mahmudul"
g.insert(1,"Hasan")
g.append("Ayat")
g.remove(a>b)
g.pop(3)
f = tuple(g)
print(type(f))
print(f)
(A,B,*c) = f
print(A)
print(B)
print(*c)
h = ("Lisan","Hasib","Hamim","Abrar")
ff = f + h
print(ff)
print(f*2)
for i in range(len(ff)):
    print(i)
x = 0
while x < len(ff):
    print(ff[x])
    x += 1
print(ff.index("Abrar"))
print(ff.count("Sintiyas"))
j = ["Sintiyas","Sintiyas",a+b,a!=b]
print(j)
j[0]="Mahmudul"
j.insert(1,"Hasan")
j.append("Ayat")
j.remove(a+b)
j.pop(3)
print(j)
k = ["Lisan","Hasib","Hamim","Abrar"]
jj = k + j
print(jj)
j.extend(k)
print(j)
j.sort()
print(j)
j.sort(reverse=True)
print(j)
print(j[0])
print(j[-2])
print(j[0:9])
l = range(1,11)
print(l)
a,b=b,a
print(a)
a+=7
print(a)
o = (1,2,3,4,5)
for oo in o:
    print(oo*2)
n = [ooo * 3 for ooo in o]
print(n)
p = None
print(p)
m = input("Enter Your Name : ")
q = [ ['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
      ['Lisan', 'Hasib', 'hamim', 'Abrar'],
      "bro"]
print(type(q))
print(q)
print(q[0][1])
q[2]='bros'
q[1][2]="Hamim"
print(q)