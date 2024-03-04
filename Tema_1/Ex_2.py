p = 0
while 1 + 10 ** (-p) != 1:
    p = p+1

print('Precizia mașinii este:', p-1)
p = p-1

x = 1.0
y = 10**(-p-1)
z = 10**(-p-1)

# Demonstrare ca adunarea nu e asociativa
if (x+y)+z != x+(y+z):
    print('Adunarea nu e asociativa pentru x =', x, 'y =', y, 'z =', z)
else:
    print('Adunarea e asociativa pentru x =', x, 'y =', y, 'z =', z)

# Găsirea unui x, y, z pentru care înmulțirea nu e asociativa
x = 10**(-p-1)
y = 10**(-p-1)
z = 10**(-p-2)

if (x*y)*z != x*(y*z):
    print('Înmulțirea nu e asociativa pentru x =', x, 'y =', y, 'z =', z)
else:
    print('Înmulțirea e asociativa pentru x =', x, 'y =', y, 'z =', z)


print((x*y)*z)
print(x*(y*z))