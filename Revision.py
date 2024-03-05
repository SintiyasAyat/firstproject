print("Hello World")
a = 10
b = 3
c = "Sintiyas"
print(f"My name is {c} & My class roll is {a//b}")
d = (1,2,3,4,5)
dd = bytes(d)
print(dd)
e = (1,2,3,4,5)
ee = bytearray(e)
print(ee)
ee[0] = 6
print(ee)
f = ('Sintiyas',"Sintiyas",a!=b,a+b)
print(f)
F = list(f)
F[0] = "Mahmudul"
F.insert(1,"Hasan")
F.append("Ayat")
F.remove(a!=b)
F.pop(3)
f = tuple(F)
print(type(f))
print(f)
g = ['Sintiyas',"Sintiyas",a!=b,a+b]
g[0]='Mahmudul'
g.insert(1,'Hasan')
g.append('Ayat')
g.remove(a!=b)
g.pop(3)
print(g)
g.sort()
print(g)
g.sort(reverse=True)
print(g)
h = [1,2,3,4,5]
H = h + g
print(H)
g.extend(h)
print(g)
for i in range(len(g)):
    print(i)
x = 0
while x < len(g):
    print(g[x])
    x += 1
j = {1,2,3,3,4,5,False,"Mahmudul"}
print(type(j))
print(j)
for ii in j:
    print(ii)
print("Mahmudul" in j)
a,b=b,a
print(a)
print(b)
a+=10
print(a)
k = (1,2,3,4,5)
l = [ll + 2 for ll in k]
print(l)
for kk in k:
    print(kk*2)
o = [['Sintiyas', 'Mahmudul', 'Hasan', 'Ayat'],
     [1, 2, 3, 4, 5,],
    'Bros'
]
print(o)
n = None
print(n)
inp = input("Enter your Name : ")