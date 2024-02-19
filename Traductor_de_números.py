numero = eval(input("Escriba un número y el programa lo mostrará en texto: "))

aux = (str(numero))

def unidades(numero):
    if numero == 0: return "Cero"
    elif numero == 1 : return "Uno"
    elif numero == 2: return "Dos"
    elif numero == 3: return "Tres"
    elif numero == 4: return "Cuatro"
    elif numero == 5: return "Cinco"
    elif numero == 6: return "Seis"
    elif numero == 7: return "Siete"
    elif numero == 8: return "Ocho"
    elif numero == 9: return "Nueve"
    
def veintes (numero):
    if(numero == 10): return("Diez")
    elif(numero == 11): return("Once")
    elif(numero == 12): return("Doce")
    elif(numero == 13): return("Trece")
    elif(numero == 14): return("Catorce")
    elif(numero == 15): return("Quince")
    elif(numero == 16): return("Dieciseis")
    elif(numero == 17): return("Diecisiete")
    elif(numero == 18): return("Dieciocho")
    elif(numero == 19): return("Diecinueve")
    elif(numero == 20): return("Veinte")
    elif(numero == 21): return("Veintiuno")
    elif(numero == 22): return("Veintidós")
    elif(numero == 23): return("Veintitrés")
    elif(numero == 24): return("Veinticuatro")
    elif(numero == 25): return("Veinticinco")
    elif(numero == 26): return("Veintiséis")
    elif(numero == 27): return("Veintisiete")
    elif(numero == 28): return("Veintiocho")
    elif(numero == 29): return("Veintinueve")
    
def treintas (numero):
    if(numero == 30): return("Treinta")
    elif(numero >= 31 and numero<= 39):
        treintas = unidades(int(aux[-1]))
        return("Treinta y " + str(treintas))

def cuarentas (numero):
    if(numero == 40): return("Cuarenta")
    elif(numero >= 41 and numero<= 49):
        cuarentas = unidades(int(aux[-1]))
        return("Cuarenta y " + str(cuarentas))
    
def cincuentas (numero):
    if(numero == 50): return("Cincuenta")
    elif(numero >= 51 and numero<= 59):
        cincuentas = unidades(int(aux[-1]))
        return("Cincuenta y " + str(cincuentas))
    
def sesentas (numero):
    if(numero == 60): return("Sesenta")
    elif(numero >= 61 and numero<= 69):
        sesentas = unidades(int(aux[-1]))
        return("Sesenta y " + str(sesentas))
    
def setentas(numero):
    if numero == 70: return "Setenta"
    elif numero >= 71 and numero <= 79:
        unidades_setenta = unidades(int(aux[-1]))
        return "Setenta y " + str(unidades_setenta)

def ochentas(numero):
    if numero == 80: return "Ochenta"
    elif numero >= 81 and numero <= 89:
        unidades_ochenta = unidades(int(aux[-1]))
        return "Ochenta y " + str(unidades_ochenta)

def noventas(numero):
    if numero == 90: return "Noventa"
    elif numero >= 91 and numero <= 99:
        unidades_noventa = unidades(int(aux[-1]))
        return "Noventa y " + str(unidades_noventa)

def dosdigitos(numero):
    
    if(len(str(numero)) == 2):
    
        if(veintes(numero) is not None): print(veintes(numero))
    
        if(treintas(numero) is not None): print(treintas(numero))
    
        if(cuarentas(numero) is not None): print(cuarentas(numero))
        
        if(cincuentas(numero) is not None): print(cincuentas(numero))
    
        if(sesentas(numero) is not None): print(sesentas(numero))
    
        if setentas(numero) is not None: print(setentas(numero))

        if ochentas(numero) is not None: print(ochentas(numero))

        if noventas(numero) is not None: print(noventas(numero))
    
def tresdigitos(numero):
    
    if(len(str(numero)) == 3):

        aux2 = numero%100
        
        if(unidades(int(aux[0])) is not None):
            
            if(numero == 100): print("Cien")
            elif(int(aux[0]) == 1): print("Ciento", end = " ")
            else: print(unidades(int(aux[0])) + "cientos", end = " ")
        
        if(dosdigitos(aux2) is not None): print(dosdigitos(aux2))
        
        if(int(aux[1]) == 0):
            if(unidades(aux2) is not None): print(unidades(aux2))
        
def cuatrodigitos(numero):

    if(len(aux) == 4):
        
        aux2 = int(aux[-3:])
        
        if(unidades(int(aux[0])) is not None):
            
            if(int(aux[0]) == 1): print("Mil", end = " ")
            else: print(unidades(int(aux[0])) + "mil", end = " ")
            
        if(tresdigitos(aux2) is not None): print(tresdigitos(aux2))
        if(int(aux[-3]) == 0 and dosdigitos(int(aux[-2])) is not None): print(dosdigitos(int(aux[-2])))
        if(int(aux[-2]) == 0 and unidades(int(aux[-1])) is not None): print(unidades(int(aux[-1])))

print("")

if(len(aux) == 1): print(unidades(numero))

dosdigitos(numero)
tresdigitos(numero)
cuatrodigitos(numero)


#4 = millares, 5 = decenas de millares, 6 = centenas de millares, 7 = millones 8 = decenas de millones
#9 = centenas de millones, 10, 11 y 12 = miles de millones, 13 = billón, 14 = decenas de billones
#15 = centenas de billones, 16, 17 y 18 = miles de billones = 19 = trillón 1'000,000'000,000'000,000