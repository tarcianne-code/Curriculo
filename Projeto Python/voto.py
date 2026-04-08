#Recebe a idade do úsuario
idade=int(input("Digite sua idade mano:"))
#Determina a situação do voto com base na idade
if idade<16:
     situacao_voto="Proibido irmão"
elif 16<=idade<18:
     situacao_voto="Opcional né pae, se for votar vota nulo mano"
elif 18<=idade<70:
     situacao_voto="Obrigátorio coroa"
else:
     situacao_voto="Opcional pae"
#Exibe o resultado
print(f"A situação de voto para as pessoas com {idade} anos é:{situacao_voto}.")