def contar_vocales(palabra):
    # Definir las vocales
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    # Inicializar el diccionario para contar cada vocal
    conteo = {vocal: 0 for vocal in vocales}
    # Contar las vocales en la palabra
    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1
    return conteo

# Solicitar la palabra al usuario
palabra = input("Ingrese una palabra: ")

# Contar las vocales y mostrar el resultado
conteo_vocales = contar_vocales(palabra)
print("Conteo de vocales:")
for vocal, cantidad in conteo_vocales.items():
    if cantidad > 0:
        print(f"{vocal}: {cantidad}")
