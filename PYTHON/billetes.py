
monto = int(input("Ingresa el dinero en dolares: "))
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0

monto_inicial = monto

while monto >= 100:
    c100 = c100 + 1
    monto = monto - 100
    
while monto >= 50:
    c50 = c50 + 1
    monto = monto - 50


while monto >= 20:
    c20 = c20 + 1
    monto = monto - 20


while monto >= 10:
    c10 = c10 + 1
    monto = monto - 10

while monto >= 5:
    c5 = c5 + 1
    monto = monto - 5


while monto >= 2:
    c2 = c2 + 1
    monto = monto - 2


while monto >= 1:
    c1 = c1 + 1
    monto = monto - 1



print(c100, " billete de US 100")
print(c50,  "billetes de US 50")
print(c20, "billetes de US 20")
print(c10, "billetes de US 10")
print(c5, "billetes de US 5")
print(c2, "billetes de US 2")
print(c1, "billetes de US 1")


