print("Hello World")
a = 10
b = 3
c = "Sintiyas Ayat"
print(f'My Name is {c} & My class roll is {a//b}')
d = (1,2,3,4,5)
e = (1,2,3,4,5)
dd = bytes(d)
print(dd)
ee = bytearray(e)
print(ee)
ee[0]=6
print(ee)
f = ['Sintyas','Sintiyas',a!=b,a+b]
print(f)
f[0] = "Mahmudul"
f.insert(1,"Hasan")
f.append("Ayat")
f.remove(a+b)
f.pop(3)
print(f)
for g in range(len(f)):
    print(g)
x = 0
while x < len(f):
    print(f[x])
    x +=1
h = ["Lisan","Hamim","Hasib","Abrar"]
h.sort()
print(h)
h.sort(reverse=True)
print(h)
hh = f + h
print(hh)
h.extend(f)
print(h)
print(h[0])
print(h[-1])
print(h[0:5])
H = [['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
     ['Lisan', 'Hasib', 'Hamim', 'Abrar',],
     "Bros"]
print(H)
i = ('Sintyas','Sintiyas',a!=b,a+b)
print(i)
I = list(i)
I[0] = "Mahmudul"
I.insert(1,"Hasan")
I.append("Ayat")
I.remove(a+b)
I.pop(3)
i = tuple(I)
print(i)
print(i.count(3))
print(i.index("Ayat"))
j = ('Lisan', 'Hasib', 'Hamim', 'Abrar')
J = i + j
print(J)
print(j*2)
(A,B,*C) = i
print(A)
print(B)
print(*C)
for ii in range(len(J)):
    print(ii)
while x < len(J):
    print(J[x])
    x += 1
k = range(1,11)
print(k)
l = {'Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'}
print(l)
for ll in l:
    print(ll)
print("Mahmudul" in l)
lll = {'Sintyas', 'Sintiyas', True, 13}
sss = [1,2,3,4,5,6,7,8,9,10]
lll.add(False)
print(lll)
lll.pop()
print(lll)
lll.remove("Sintiyas")
print(lll)
lll.discard(10)
lll.update(sss)
print(lll)
s = {False, True, 'Sintyas', 'Sintiyas', 13}
lll.union(s)
print(lll)
lll.add(False)
print(lll)
sss = [1,2,3,4,5,6,7,8,9,10]
for iii in sss:
    print(iii+2)
print([ssss * 2 for ssss in sss ])
a,b=b,a
print(a)
print(b)
a+=7
print(a)
b-=7
print(b)