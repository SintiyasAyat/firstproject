print("HelloWorld")
a = 20
b = 3
c = "Sintiyas ayat"
print(f'My name is {c} and my roll is {a//b}')
d = [1,2,3,4,5]
dd = bytes(d)
print(type(dd))
print(dd)
e = [1,2,3,4,5]
ee =bytearray(e)
print(type(ee))
ee[0]=6
print(ee)
f = ['Sintiyas','Ayat ','ku',a!=b,a+b,]
f[0] = 'Mahmudul'
f.append('is everythings alright')
f.insert(1,'Hasan')
f.remove(a!=b)
f.pop(3)
print(type(f))
for g in f:
    print(g)
h = 0
while h <len(f):
    print(f[h])
    h = h + 1

h = 0
while h < 2 :
    print(f[h])
    h=h+1
n = None
print(n)
li = [10,1,2,3,4,5,6,7,8]
li.sort()
print(li)
li.sort(reverse=True)
print(li)
lis = li + f
print(lis)
f.extend(li)
print(f)
ran = range(1,9)
print(type(ran))
print(ran)
for hh in ran:
    print(hh)