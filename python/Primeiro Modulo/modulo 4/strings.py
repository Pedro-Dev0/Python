curso = " pYtHon "

print(curso.lower())  # Convierte a minúsculas
print(curso.upper())  # Convierte a mayúsculas 
print(curso.title())  # Primera letra de cada palabra en mayúscula

print(curso)
# imprime mas eliminando espaços 
print(curso.strip())  # Elimina espacios al inicio y al final
print(curso.lstrip())  # Elimina espacios al inicio
print(curso.rstrip())  # Elimina espacios al final

# centraliza o texto e coloca o caractere escolhido para preencher os espaços vazios e o join a cada caractere da string uni os com o caractere escolhido

print(curso.center(20, "*"))  # Centra el texto en un campo de 20 caracteres, rellenando con '*'
print(".".join(curso)) # Une cada carácter de la cadena con '.'