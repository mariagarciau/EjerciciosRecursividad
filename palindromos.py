def palindromos(cadena,inicio,fin):
    def quitarAcentos(cadena):
        cadena=cadena.lower()
        cadena=cadena.replace("","")
        cadena=cadena.replace("á","A")
        cadena=cadena.replace("é","E")
        cadena=cadena.replace("í","I")
        cadena=cadena.replace("ó","O")
        cadena=cadena.replace("ú","U")
        return cadena
    if inicio>=fin:
        return True
    if cadena[inicio]==cadena[fin]:
        return palindromos(cadena,inicio+1,fin-1)
    else:
        return False