import requests

def menu():
    print("\nMenu - Escolha uma opção")
    print("1 - Listar todos os carros")
    print("2 - Pesquisar carro por placa")
    print("3 - Cadastrar um carro")
    print("4 - Deletar um carro")
    print("5 - Editar um carro")
    print("6 - Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"

    while True:
        opcao = menu()

        if opcao == "1":
            r = requests.get(f"{url}/carros")
            print("\nLista de carros:")
            print(r.json())

        elif opcao == "2":
            placa = input("Digite a placa do carro: ")
            r = requests.get(f"{url}/carros/{placa}")
            if r.status_code == 200:
                print("\nCarro encontrado:")
                print(r.json())
            else:
                print("Carro não encontrado!")

        elif opcao == "3":
            placa = input("Digite a placa do carro: ")
            modelo = input("Digite o modelo do carro: ")
            nome = input("Digite o nome do dono: ")
            marca = input("Digite a marca do carro: ")
            carro = {
                "placa": placa,
                "modelo": modelo,
                "nome": nome,
                "marca": marca
            }
            r = requests.post(f"{url}/carros", json=carro)
            if r.status_code in [200, 201]:
                print("\nCarro cadastrado com sucesso!")
                print(r.json())
            else:
                print("Erro ao cadastrar carro:", r.text)

        elif opcao == "4":
            placa = input("Digite a placa do carro a deletar: ")
            r = requests.delete(f"{url}/carros/{placa}")
            if r.status_code == 200:
                print("\nCarro deletado com sucesso!")
            else:
                print("Carro não encontrado!")

        elif opcao == "5":
            placa = input("Digite a placa do carro que deseja editar: ")
            novo_modelo = input("Digite o novo modelo: ")
            novo_nome = input("Digite o novo nome: ")
            nova_marca = input("Digite a nova marca: ")

            carro_editado = {
                "placa": placa,  # continua com a mesma placa
                "modelo": novo_modelo,
                "nome": novo_nome,
                "marca": nova_marca
            }

            r = requests.put(f"{url}/carros/{placa}", json=carro_editado)
            if r.status_code == 200:
                print("\nCarro editado com sucesso!")
                print(r.json())
            else:
                print("Erro ao editar carro:", r.text)

        elif opcao == "6":
            print("Saindo...")
            break
