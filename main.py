from usuario import Usuario

continuar = 1
lista_usuarios = []

while continuar != 0:
    try:
        nome= input("Digite o seu nome: ")
        sobrenome = input("Qual o seu sobrenome? ")
        idade = int (input("Digite sua idade: "))
        usuario= Usuario(nome,idade,sobrenome)

        lista_usuarios.append(usuario)

        if usuario.idade == 99:
            break
        if usuario.idade == 98:
            continue

        print(f"Olá, {usuario.nome} {usuario.sobrenome},  sua idade é: {usuario.idade} anos")

        if idade <= 17:
            print(f"{usuario.nome} é adolescente")
        elif idade >= 18 and idade <= 50:
            print(f"{usuario.nome} é adulto")
        else:
            print(f"{usuario.nome} é idoso")
        continuar = int(input("Deseja continuar cadastrando? 0 - Sair 1 - Continuar"))
    except ValueError:
        print("Você deve informnar um número válido")
else:
    print("Lista de usuarios cadastrados: ")
    for x in lista_usuarios:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade {x.idade}")


    print("O loop entrou no else")

