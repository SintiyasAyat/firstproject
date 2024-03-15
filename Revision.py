print("Hello World")
a = 12
b = 3
c = "Sintiyas Ayat"
print(f'My name is {c} & My class roll is {a//b}')
def ano():
    c = "Mahmudul Hasan"
    print(c)
ano()
print(c)
print(c.upper())
print(c.lower())
print(c.split())
print(c.replace("Sintiyas",""))
d = (1,2,3,4,5)
d = bytes(d)
print(d)
print(type(d))
e = (1,2,3,4,5)
e = bytearray(e)
print(e)
e[0]=6
print(e)
f = ['what','Sintiyas',a!=b,a+b]
print(f)
f[0] = "Mahmudul"
f.insert(1,"Hasan")
f.append('Ayat')
f.pop(3)
f.remove(a+b)
print(f)
f.sort()
print(f)
f.sort(reverse=True)
print(f)
ff = ['Lisan','Hasib','Hamim',"Abrar"]
fff = ff  + f
print(fff)
f.extend(ff)
print(f)
Ff = f.copy()
print(Ff)
F = [['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
['Lisan','Hasib','Hamim',"Abrar"],
     'bro'
]
print(F)
for g in range(len(f)):
    print(g)
x = 0
while x < len(f):
    print(f[x])
    x += 1
h = ('what', 'Sintiyas', True, 15)
print(h)
H = list(h)
H[0] = 'Mahmudul'
H.insert(1,"Hasan")
H.append('Ayat')
H.pop(3)
H.remove(a+b)
h = tuple(H)
print(h)
hh = ('Lisan', 'Hasib', 'Hamim', 'Abrar')
H = hh + h
print(H)
print(H*2)
for HHH in range(len(H)):
    print(HHH)
x = 0
while x < len(H):
    print(H[x])
    x += 1
(A,B,*C) = h
print(A)
print(B)
print(*C)
print(H.count("h"))
print(H.index("Ayat"))
print(h[0])
print(h[-0])
print(h[:-0])
i = range(1,11)
print(i)
for ii in i:
    print(ii)
j = {"Sintiyas","Sintiyas",a!=b,a+b}
print(j)
j.remove(a+b)
j.discard(13)
j.pop()
j.add("Ayat")
J = {'Lisan', 'Hasib', 'Hamim', 'Abrar'}
j.update(J)
print(j)
Jj = (1,2,3,4,5)
j.update(Jj)
print(j)
k = {"GTR36": 2012,
     "Supra.gk2":2010}
print(k.get("GTR36"))
print(k.values())
print(k.keys())
k["GTR36"] = 2008
print(k)
K = {"Frindshipinfo": {
    "Mahmudul": {
        "Full Name": "Mahmudul Hasan Sintiyas Ayat",
        "Location": "BowBazar, Jatrabari",
        "Birth Date": (2000, 10, 25)
    },"lisan":{"full Name": "lisanur rahman",
               "Location":"Madaripur,Noyakhali",
               "Birth Date" : (2002,4,2)
               },"Abrar":{"Full Name": "Abrar Jawad",
                           "Location":"Dawadkhandi,Komillah"}
}}
print(K)
K["Frindshipinfo"]['Abrar'].pop("Location")
print(K)
K["Abrar"] ={"Full Name": "Abrar Jawad",
                           "Location":"Dawadkhandi,Komillah",
                             "Birth Date": (2002,1,2)}
for kk in K.values():
    print(kk)
for kkk in K.keys():
    print(kkk)
for kkkk in K.items():
    print(kkkk)
newdic = K.copy()
print(newdic)
newdic.clear()
print(newdic)
l = (1,2,3,4,5)
for ll in l:
    print(ll*2)
print([lll+5 for lll in l])
a,b=b,a
print(a)
print(b)
a+=10
print(a)