curso = " pYtHon "

print(curso.lower())  # Convierte a minúsculas
print(curso.upper())  # Convierte a mayúsculas 
print(curso.capitalize())  # Primera letra en mayúscula
print(curso.title())  # Primera letra de cada palabra en mayúscula
print(curso)
print(curso.strip())  # Elimina espacios al inicio y al final
print(curso.lstrip())  # Elimina espacios al inicio
print(curso.rstrip())  # Elimina espacios al final

print(curso.center(20, "*"))  # Centra el texto en un campo de 20 caracteres, rellenando con '*'
print(".".join(curso)) # Une cada carácter de la cadena con '.'