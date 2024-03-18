print("Hello World")
a = 10
b = 3
c = 'Sintiyas Ayat'
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
        break
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
i = {
    "Frindshipinfo": {
        "Mamudul": {
            "Full Name": "Mahmudul Hasan Sintiyas Ayat",
            "Number": 1939283443
        },
    "Lisan": {
        "Full Name": "Lisanur Rahman",
        "Number": 599
    },
        "Abrar" : {"Full Name" : "Abrar Jawad",
                   "Numder" : 87 },
        "Hamim":{"Full Name " : "Hamim hosain"}
}}
i["Frindshipinfo"]["Hamim"] = {
    "Full Name": "Hamim hosain",
    "Number": 552
}
