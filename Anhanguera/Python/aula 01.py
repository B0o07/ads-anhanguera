print("Hello, World!")

x = 1
nome = str(input("Qual o seu nome: "))
nota1 = float(input("Qual a sua nota: "))
nota2 = float(input("Qual a sua nota: "))
nota3 = float(input("Qual a sua nota: "))
nota4 = float(input("Qual a sua nota: "))
fez_inscricao = True
media = (nota1 + nota2 + nota3 + nota4)/4
#Observe que utilizamos a função float(), pois sem ela, o Python entenderia que as notas seriam String.

print(type(x))
print(type(nome))
print(type(nota1))
print(type(nota2))
print(type(nota3))
print(type(nota4))
print(type(fez_inscricao))

#Formatadores de caracteres.
print("Olá %s, bem vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!" % (nome))

#F_string
print(f"Olá {nome}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro Hello World!")

#Condição para a aprovação do aluno.
if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

#Dadas as notas mostramos a média final e a situação do aluno.
print(f"A média das notas é: {media}")
print(f"Situação do Aluno: {situacao}")
