curso = "Curso de Python"
frutas = ["banana", "maçã", "laranja"]
saques = [100, 200, 300, 400]

print("Curso" in curso)         # True
print("Java" in curso)      # False
print("Java" not in curso)  # True

print("maçã" in frutas)        # True
print("uva" in frutas)         # False
print("uva" not in frutas)     # True

print(200 in saques)          # True
print(500 in saques)          # False
print(500 not in saques)      # True