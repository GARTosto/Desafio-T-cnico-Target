def contar_letra_a(texto):
    quantidade = sum(1 for char in texto if char.lower() == 'a')
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes.")
    else:
        print("A letra 'a' não aparece na string.")

# Teste com uma string informada
string = input("Digite uma string: ")
contar_letra_a(string)
