#García Rivera Ángel Iván

print("Ingrese la medida de su cuadrilatero y el programa indicará si es un cuadrado, rectángulo u otro")

lado_1 = eval(input("Primer lado: "))
lado_2 = eval(input("Segundo lado: "))
lado_3 = eval(input("Tercer lado: "))
lado_4 = eval(input("Cuarto lado: "))

if lado_1 == lado_2 and lado_1 == lado_3 and lado_1 == lado_4:
    print("Su cuadrilatero es un cuadrado")
elif lado_1 == lado_3 and lado_2 == lado_4:
    print("Su cuadrilatero es un rectángulo")
else:
    print("Usted tiene otro tipo de cuadrilatero")