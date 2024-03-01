print("Hello World")
# variables
name = "Sintiyas Ayat"
print(name)
a = 12
b = 8
c = "20 is that all you got"
print(a + b)
#how to find bata type print(type(c)) kono bata kon dorone ta der korar jonno
print(type(c))
print(c)
g="jkg9"
print(type(g))
gg=797j
print(gg)
print(name+ " " + c)
#Booltype Bata true folse ber korar jonno ues hoy
x = 8
y = 10
print(y==x)
print(y>x)
print(type(y>x))
#str format type
name2 = "Anisa"
name3= "Ayat"
roll = 9
roll2 = 8
print(f"{name3} and {name2} how mush apple we have and my roll is {roll}")
#byte type bata ai gola image jonno ues hoy kintu byte change kora jay nh
bc = [1,2,3,4,5]
bcc = bytes(bc)
print(bcc[1])
#bytearry type  bata ai gola image jonno ues hoy
acc = [9,2,3,4,5,6]
ac = bytearray(acc)
ac[0] = 90
print(ac[0])
#none type bata
n = None
print(n)
print(type(n))
#list type bata
li = ['son of masud','ayat','lisan']
print(type(li))
print(li)
#tuple type bata immuture type
tup = (0,1,3,4,5,6,7,8,9,)
print(type(tup))
print(tup)
#range type bata
ran = range(1,9)
print(type(ran))
print(ran)
for i in ran:
    print(i)
#Arithmetic Oparetors
# + = Addition
# - = Suptraction
# * = Multiplication
# / = Division
# % = Modulus
#** = Exponentiation
#// = Floor Division
ab = 20
ba = 10
bc = 3
print(ab + ba)#Addition
print(ab - ba)#Suptraction
print(ab * ba)#multiplition
print(ab /bc)#Division
print(ab % bc)#modulus
print(ab **bc)#exponentiation
print(ab//bc)#Floor Division
#assignment operator sob operator ei methor diye us kora jabe
ass = 10
ass//=3
print(ass)
# sapping variables
A = 50
B = 60
A,B = B,A
print(A)
#uesr input neya
x = input('please inter you name :')
print(x)
#type casting diye ak type ar bata onno type ropantor korte pari
strtype = '13'
print(type(strtype))
print(int(strtype))
print(type(int(strtype)))
#list change
li[0] = "hasan"
print(li[0])
#list ar sese bata kibabe add korbo
li.append(10)
print(li)
#list je kono jaygay kibabe bata add korbo
li.insert(3,'job')
print(li)
#list ar je kono index re dehkte chai le
print(li[0])
#.romove diye je kono kisu list ar same jinis type kore oi tah romove
li.remove('hasan')
#list kono kisu index call kore remove
li.pop(0)
print(li)
#list ar sob kisu remove korte kaje ase
li.clear()
print(li)
lis = ['hasan', 'ayat', 'lisan','job', 10]
#for new  variables in ager variables : diya siriyal by list print kora jay
for liss in lis:
    print(liss)
#for in loop ar in sese range(len()) loop diya list ar index koto gola jana jay
for lia in range(len(lis)):
    print(lia)
#while loop
xx = 0
while xx < len(lis):
    print(lis[xx])
    xx = xx + 1

xx = 0
while xx < 3:
    print(lis[xx])
    xx = xx + 1
# Python List Comprehension for loop ues kore comprehension
num = [1,2,3,4,5]
for f in num:
    print(f*2)
# Python List Comprehension list maje rakhei comprehension kora
num2 = [1,2,3,4,5]
gh = [hg + 2 for hg in num2]
print(gh)
# soft list aelomelo thak serial by anbo ki vabe
so = [9,8,654,32,46,7,89,1,2,3]
so.sort()
print(so)
# gosano list ke ki vabe  aelomelo korbo
so.sort(reverse=True)
print(so)
#list copy
lish = li.copy()
print(lish)
#join list kibabe korbo
new = ['Mahmudul',"Hasan","Sintiyas",'Ayat',]
new2 = [1,2,3,4,5]
new3 = new2 + new
print(new3)
#join list bainamik vabe kibabe korbo
new.extend(new2)
print(new)
new4 = [1,2,2,3,4,]
new3.extend(new4)
print(new3)
#Martrix holo dui tah alada dimensional create list modthe
lia = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    11
]
print(lia)
print(type(lia))
print(lia[0][4])





















































