print("Hello World")
a = 10
b = 3
c = "Sintiyas Ayat"
print(f"My name is {c}")
d = (1,2,3,4,5)
dd = bytes(d)
print(dd)
e = (1,2,3,4,5)
ee = bytearray(e)
print(ee)
ee[0] = 6
print(ee)
f = ["what","Sintiyas",a!=b,a+b]
print(f)
f[0] = "Mahmudul"
f.insert(1,"Hasan")
f.append('Ayat')
f.pop(3)
f.remove(a+b)
print(f)
F = ["lisan","Abrar","Hasib","Hamim"]
F.sort()
print(F)
F.sort(reverse=True)
print(F)
ff = F + f
print(ff)
f.extend(F)
print(f)
print(f[0])
print(f[-0])
print(f[0:8])
for FF in range(len(f)):
    print(f)
x = 0
while x < len(f):
    print(f[x])
    x += 1
Ff = ["bros",
    ['Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'],
   ["lisan","Abrar","Hasib","Hamim"],
]
print(Ff)
h = ("what","Sintiyas",a!=b,a+b)
print(h)
H = list(h)
H[0] = "Mahmudul"
H.insert(1,"Hasan")
H.append('Ayat')
H.pop(3)
H.remove(a+b)
h = tuple(H)
print(type(h))
print(h)
for hh in h:
    print(hh)
print('Mahmudul' in h)
(A,B,*C) = h
print(A)
print(B)
print(*C)
print(h*2)
for hhh in range(len(h)):
    print(hhh)
x = 0
while x < len(h):
    print(h[x])
    x += 1
HH = ("lisan","Abrar","Hasib","Hamim",12,1,2,1,2,3,6,34,3,)
Hh = h + HH
print(Hh)
i = {'Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'}
print(i)
i.add("Hasan")
i.remove('Ayat')
print(i)
i.update(HH)
print(i)
j = {'Mahmudul', 'Hasan', 'Sintiyas', 'Ayat'}
I = {1,2,3,4,5,6,7,8,9,10}
j.union(I)
print(j)
i.update(I)
print(i)
for ii in i:
    print(ii)
print(12 in i)
k = { "Schoolinfo" : {
    "Mahmudul":{"Name":"Mahmudul Hasan Sintiyas Ayat",
                "loction":"Bowbazar,Jatrabari",
                "Class": 11 ,
                "roll" : 467 },
    "lisan" : {"Name" : "Lisanur Rahman",
                "loction":"noyakhali",
                "Class": 11 ,
                "roll" : 41},
    "Abrar" : {"Name":"Abrar Jawad",
                "loction":"Bowbazar,Jatrabari",
                "Class": 11 ,
                "roll" : 43},
}}
print(k["Schoolinfo"]["Mahmudul"])
print(k.get("Schoolinfo"))
print(k.values())
print(k.keys())
a,b=b,a
print(a)
print(b)
a+=12
print(a)
 09kikkkjkk