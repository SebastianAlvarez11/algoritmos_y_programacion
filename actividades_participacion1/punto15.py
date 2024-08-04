def palindromo(palabra):
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra: ")

if palindromo(palabra):
    print("La palabra", palabra, "es palíndromo")
else:
    print("La palabra", palabra, "no es palíndromo")