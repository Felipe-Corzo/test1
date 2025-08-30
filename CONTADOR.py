import os
os.system('clear')
palabra = input("Ingrese una palabra: ")
conteo_vocales = {'a': 0, 'e': 0,'i': 0,'o': 0,'u': 0}

for letra in palabra:
    if letra in conteo_vocales:
        conteo_vocales[letra] = str(int(conteo_vocales[letra]) + 1)


print(f'Tu palabra tiene {conteo_vocales["a"]} vocales a, ')
print(f'Tu palabra tiene {conteo_vocales["e"]} vocales e, ')
print(f'Tu palabra tiene {conteo_vocales["i"]} vocales i, ')
print(f'Tu palabra tiene {conteo_vocales["o"]} vocales o, ')  
print(f'Tu palabra tiene {conteo_vocales["u"]} vocales u, ')