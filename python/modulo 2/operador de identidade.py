curso = "Python"
nome_curso = curso
saldo, limite = 200, 200

print(nome_curso is curso)  # True
print(saldo is limite)      # True 

# is é um operador de identidade que verifica se dois objetos estão na mesma localização na memória.
print(saldo is not limite)  # False
print(nome_curso is not curso)  # False

# No exemplo acima, 'nome_curso' aponta para o mesmo objeto que 'curso', então 'nome_curso is curso' retorna True.