print("Hello World")
a = 10
b = 3
c = "Sintiyas Ayat"
print(f"my name is {c} & my class roll is {a//b}")
d = (1,2,3,4,5)
dd = bytes(d)
print(type(dd))
print(dd)
e = (1,2,3,4,5)
ee = bytearray(e)
print(type(ee))
print(ee)
ee[0]=6
print(ee)
f = ("Sintiyas","Ayat",a!=b,12j)
print(type(f))
print(f)
g = range(1,11)
print(type(g))
print(g)
h = ["Sintiyas","Sintiyas",a!=b,12j]
h[0]="Mahmudul"
h.insert(1,"Hasan")
h.append("Ayat")
h.remove(12j)
h.pop(3)
print(type(h))
print(h)
for i in (range(len(h))):
    print(i)
x = 0
while x < len(h):
    print(h[x])
    x = x + 1
j = ["Lisan","Hamim","Hasib","Abrar"]
j.sort()
print(j)
j.sort(reverse=True)
print(j)
jj = h + j
print(jj)
j.extend(h)
print(j)
j.clear()
print(j)
a,b=b,a
print(a)
print(b)
a+=b
print(a)
print(type(a!=b))
print(a>=b)
print(a<b)
n = None
print(type(n))
print(n)
k = [['Lisan', 'Hamim', 'Hasib', 'Abrar'],
     ['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
    'Bro'
]
print(k)
print(type(k))
print(k[0][1])
l = (1,2,3,4,5)
for o in l:
    print(o*2)
p = [oo + 10 for oo in l]
print(p)
w = input("Enter Your Name : ")