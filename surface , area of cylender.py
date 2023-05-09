Pi = 3.14
h_cylindar = float(input('Height of cylindar: '))
r_cylindar = float(input('Radius of cylindar: '))
print('volume is: %.2f '% (Pi*(r_cylindar**2)*h_cylindar))
print('Surface area is %.2f '%(2*Pi*r_cylindar*(h_cylindar+r_cylindar)))