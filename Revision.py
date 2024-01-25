print("Hello World")
a = 10
b = 3
c = "Sintiyas"
print(f"My Name is {c} & My class roll is {a//b} ")
d = [1,2,3,4,5]
dd = bytes(d)
print(type(dd))
e = [9,2,3,4,5]
ee = bytearray(e)
print(type(ee))
print(ee)
ee[0]=1
print(ee)
print(a!=b)
print(a==b)
f = ["Sintiyas","Sintiyas",a!=b,a+b]
f[0]="Mahmudul"
f.insert(1,"Hasan")
f.append("Ayat")
f.pop(3)
f.remove(a+b)
print(type(f))
print(f)
g = ('Mahmudul', 'Hasan', 'Sintiyas', 'Ayat')
print(type(g))
print(g)
h = range(1,11)
print(type(h))
print(h)
for i in h:
    print(i)
j = 0
while j < len(f):
    print(f[j])
    j = j + 1
j = 0
while j < 2:
    print(f[j])
    j = j + 1
a,b=b,a
print(a)
print(b)
a+=b
print(a)
print(b)
print(a-3)
k = ["Hasib","Abrar","Lisan","Hamim"]
f.extend(k)
print(f)
kk = k + f
print(kk)
kk.sort()
print(kk)
kk.sort(reverse=True)
print(kk)
n = None
print(type(n))
print(n)
new = [1,2,3,4,5]
gg = [ii//2 for ii in new]
print(gg)
for iii in new:
    print(iii*2)
