print("Hello World")
a = 10
b = 3
c = "Sintiyas Ayat"
print(f"My name is {c} & My class roll is {a//b}")
d = (1,2,3,4,5)
dd = bytes(d)
print(dd)
e = (1,2,3,4,5)
ee = bytearray(e)
print(ee)
ee[0]=6
print(ee)
f = ("Sintiyas",a!=b,a+b)
print(f)
g = range(1,11)
print(g)
h = ["Sintiyas","Sintyas",a!=b,112j]
h[0]="Mahmudul"
h.insert(1,"Hasan")
h.append("Ayat")
h.remove(a!=b)
h.pop(3)
print(h)
i = ["Lisan","Hamim","Hasib","Abrar"]
ii = h + i
print(ii)
i.extend(h)
print(i)
i.sort()
print(i)
i.sort(reverse=True)
print(i)
i.clear()
print(i)
print(h[0])
print(h[-1])
print(h[0:5])
j = [ ['Mahmudul', 'Hasan', 'Sintyas', 'Ayat'],
    ['Lisan', 'Hamim', 'Hasib', 'Abrar'],'Bro'
]
print(j)
for k in range(len(h)):
    print(k)
x = 0
while x < len(h):
    print(h[x])
    x = x + 1
a,b=b,a
print(a)
print(b)
a+=b
print(a)
k = (1,2,3,4,5)
for ii in k:
    print(ii*5)
l = [oo * 2 for oo in k]
print(l)
n = None
print(n)
inp = input("Enter Your Name : ")