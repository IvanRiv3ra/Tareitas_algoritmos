#García Rivera Ángel Iván

UNIDADES = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
DECENAS = ['', 'diez', 'veinti', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'] # Modificación en las decenas
CENTENAS = ['', 'cien', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
ESPECIALES = {11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince'}

def convertir_numero_a_letras(n):
    if n in ESPECIALES:
        return ESPECIALES[n]
    elif n < 10:
        return UNIDADES[n]
    elif n < 30:
        if n % 10 == 0:
            return DECENAS[n // 10]
        else:
            return DECENAS[n // 10] + ' y ' + UNIDADES[n % 10]
    elif n < 100:
        if n % 10 == 0:
            return DECENAS[n // 10]
        else:
            return DECENAS[n // 10] + ' y ' + UNIDADES[n % 10] # Cambio aquí
    elif n < 1000:
        if n % 100 == 0:
            return CENTENAS[n // 100]
        else:
            return CENTENAS[n // 100] + ' ' + convertir_numero_a_letras(n % 100)
    elif n < 1000000:
        if n // 1000 == 1:
            if n % 1000 == 0:
                return 'mil'
            else:
                return 'mil ' + convertir_numero_a_letras(n % 1000)
        else:
            if n % 1000 == 0:
                return convertir_numero_a_letras(n // 1000) + ' mil'
            else:
                return convertir_numero_a_letras(n // 1000) + ' mil ' + convertir_numero_a_letras(n % 1000)
    elif n < 1000000000:
        if n // 1000000 == 1:
            if n % 1000000 == 0:
                return 'un millón'
            else:
                return 'un millón ' + convertir_numero_a_letras(n % 1000000)
        else:
            if n % 1000000 == 0:
                return convertir_numero_a_letras(n // 1000000) + ' millones'
            else:
                return convertir_numero_a_letras(n // 1000000) + ' millones ' + convertir_numero_a_letras(n % 1000000)
    elif n < 1000000000000:
        if n // 1000000000 == 1:
            if n % 1000000000 == 0:
                return 'mil millones'
            else:
                return 'mil millones ' + convertir_numero_a_letras(n % 1000000000)
        else:
            if n % 1000000000 == 0:
                return convertir_numero_a_letras(n // 1000000000) + ' mil millones'
            else:
                return convertir_numero_a_letras(n // 1000000000) + ' mil millones ' + convertir_numero_a_letras(n % 1000000000)
    elif n < 1000000000000000:
        if n // 1000000000000 == 1:
            if n % 1000000000000 == 0:
                return 'un billón'
            else:
                return 'un billón ' + convertir_numero_a_letras(n % 1000000000000)
        else:
            if n % 1000000000000 == 0:
                return convertir_numero_a_letras(n // 1000000000000) + ' billones'
            else:
                return convertir_numero_a_letras(n // 1000000000000) + ' billones ' + convertir_numero_a_letras(n % 1000000000000)
    elif n < 1000000000000000000:
        if n // 1000000000000000 == 1:
            if n % 1000000000000000 == 0:
                return 'un trillón'
            else:
                return 'un trillón ' + convertir_numero_a_letras(n % 1000000000000000)
        else:
            if n % 1000000000000000 == 0:
                return convertir_numero_a_letras(n // 1000000000000000) + ' trillones'
            else:
                return convertir_numero_a_letras(n // 1000000000000000) + ' trillones ' + convertir_numero_a_letras(n % 1000000000000000)
    else:
        return 'Número fuera de rango'

# Prueba
numero = int(input("Por favor, ingrese un número para convertir a letras: "))
print(f"{convertir_numero_a_letras(numero)}")
