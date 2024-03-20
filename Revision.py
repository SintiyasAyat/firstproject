print("Hello World")
a = 10
b = 3
c = 'Sintiyas Ayat'
print(c.upper())
print(c.lower())
print(c.split())
print(c.replace("S","s"))
def new():
    c = "Mahmudul Hasan"
    print(c)
new()
print(f'My Name is {c} & My class roll is {a//b}')
d = (1,2,3,4,5)
d = bytes(d)
print(d)
e = (1,2,3,4,5)
e = bytearray(e)
print(e)
e[0]=6
print(e)
f = ["What","Sintiyas",a!=b,a+b]
print(f)
f[0]="Mahmudul"
f.insert(1,'Hasan')
f.append('Ayat')
f.remove(a+b)
f.pop(3)
print(f)
print(f.count("Sintiyas"))
print(f.index("Mahmudul"))
print(f[0])
print(f[-1])
print(f[0:12])
f.sort()
print(f)
f.sort(reverse=True)
print(f)
for ff in range(len(f)):
    print(ff)
x = 0
while x < len(f):
    print(f[x])
    x +=1
F = ["Lisan","Hamim","Hasib","Ayat"]
fF= F + f
print(fF)
f.extend(F)
print(f)
Ff = [["lisan","Hamim","Hasib","Ayat"],
      ['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
      "Bros"
]
print(Ff)
Ff[0][0]="Lisan"
Ff[0].insert(3,"Abrar")
print(Ff)
g = ('What', 'Sintiyas', True, 13)
print(g)
G = list(g)
G[0]="Mahmudul"
G.insert(1,'Hasan')
G.append('Ayat')
G.remove(a+b)
G.pop(3)
g = tuple(G)
print(g)
print(type(g))
x = 0
while x < len(g):
    print(g[x])
    x += 1
for Gg in g:
    if Gg == "Sintiyas":
        break
    print(Gg)
GG = ('Lisan', 'Hamim', 'Hasib', 'Abrar',)
Ggg = g + GG
print(Ggg)
print(Ggg*2)
A,B,*C = G
print(A)
print(B)
print(*C)
h = range(1,11)
print(h)
for hh in h:
    if hh == 6:
        continue
    print(hh)
print(a>b)
print(a==b)
print(type(a<b))
a,b=b,a
print(a)
print(b)
a+=17
print(a)
'''i = input('Enter Your Name : ')
print(i)'''
i = {"Sintiyas",'Ayat',a>b,a+b}
print(i)
i.remove('Ayat')
i.discard(10)
iii = {"Mahmudul","Hasan","AYAT"}
ii = i.union(iii)
print(ii)
i.pop()
i.update(GG)
i.add("Jotarbari")
print(i)
for iiii in i:
    print(iiii)
Friendshipinfo = {
    "Mamudul": {
        "Full Name": "Mahmudul Hasan Sintiyas Ayat",
        "Number": 1939283443
    },
    "Lisan": {
        "Full Name": "Lisanur Rahman",
        "Number": 599
    },
    "Abrar": {
        "Full Name": "Abrar Jawad",
        "Number": 87,
        "just": "hello"
    },
    "Hamim": {
        "Full Name": "Hamim Hosain"
    },
    "Year": {
        "Full Name": "hello"
    },
    "Any": "hi"
}
Friendshipinfo["Hamim"] = {
    "Full Name": "Hamim hosain",
    "Number": 55}
print(Friendshipinfo)
print(Friendshipinfo["Hamim"])
Friendshipinfo.pop("Year")
Friendshipinfo.popitem()
Friendshipinfo["Abrar"].pop("just")
print(Friendshipinfo)
for j in Friendshipinfo.keys():
    print(j)
for jj in Friendshipinfo.values():
    print(jj)
for jjj in Friendshipinfo.items():
    print(jjj)
k = (1,2,3,4,5)
for kk in k:
    print(kk * 2 )
print([kkk + 1 for kkk in k])
a = 10
b = 33
if a >= b or a == b :
    print("a is Geat")
elif a == b:
    print("a and b is Equal")
else:print("No b is Geater")
if not a < b :
    print("a is Geat")
elif a == b :
    print("wow is it Equal")
else:print("No b is Geater")