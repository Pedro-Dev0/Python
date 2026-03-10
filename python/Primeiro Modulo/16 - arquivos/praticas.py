try:
    with open("lorem.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"erro ao abrir arquivo {exc}")