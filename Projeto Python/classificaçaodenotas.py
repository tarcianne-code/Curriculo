def classifica_nota(nota):
    if nota < 0 or nota > 100:
        return "Erro! a nota deve estar entre 0 e 100."
    elif nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"
#Leitura da nota
nota_usuario = float(input("Digite sua nota final (0 á 100):"))
#Chama a função e exibe o resultado
resultado = classifica_nota(nota_usuario)
print(f"Sua classificação é: {resultado}")