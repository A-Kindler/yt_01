a =1
b=2
c = a-b
print(a+b)
print(c)

#ineger : ganze zahlen
# str text
#floats : kommazahl

d = "2"
d = int(d)
d = str(d)
c = str(c)

print(d+c)
t = "hallo"
q = " ich bin joan"
print(q+t)

print(type(f"meine note in MAthe ist eine {c}!"))

print("meine note in Mathe ist eine " + str(c)+"!")

p="joan"

def funktion1(arg1,arg2):
    p = arg1 + arg2
    return p

o = funktion1(6,7) - funktion1(4,1)

print(o)






zahl = 5
print(zahl == 5)

# ==
# !=
# <
# >
# >=
# <=



if zahl==5 :
    print("ausführen")






import os

src_pfad = "C:/Users/Ansgar/projekte/yt_01/src/main.py"


print("funktion ergibt: " + str(os.path.isfile(src_pfad)))

if os.path.isfile(src_pfad):
    print("Die Datei 'main.py' existiert im Ordner 'src'.")
elif zahl == 5:
    print("Die Datei 'main.py' existiert NICHT im Ordner 'src'.")
elif 1==1:
    print(12)
else:
    print("fuck")


nummer = 1

while nummer<10:
    print(nummer)
    nummer = nummer+1


print(type(True))

# Listen
list1 = [a,b,zahl]

list2 = ["joan","ansgar","max"]

print(list1)
print(list2)

erster_collaborateur = list2[2]
print(erster_collaborateur)

print("FOR LOOP:")

topics = ["Hund der sich verliebt", "katze die kratzt","mensch der fliegen kann"]


for variable in topics:
    prompt = "erstelle eine geschichte über "+variable
    print(prompt)   


