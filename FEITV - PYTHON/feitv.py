import os

arquivo_usuarios = "usuarios.txt"
arquivo_curtidas = "curtidas.txt"

def comecar():
    if not os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, "w", encoding="utf-8") as f:
            pass

    if not os.path.exists(arquivo_curtidas):
        with open(arquivo_curtidas, "w", encoding="utf-8") as f:
            pass

def carregar():
    usuarios = []

    with open(arquivo_usuarios, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if linha:
                partes = linha.split(";")

                usuario = {
                    "id": int(partes[0]),
                    "nome": partes[1],
                    "senha": partes[2]
                }
                usuarios.append(usuario)
    return usuarios

def cadastrar():
    usuarios = carregar()

    print("\n-----Cadastro-----")
    nome = input("Nome de usuário: ").strip()
    senha = input("Senha: ").strip()

    for u in usuarios:
        if u["nome"].lower() == nome.lower():
            print("Usuário já existente!")
            return

    novo_id = 1
    if usuarios:
        novo_id = usuarios[-1]["id"] + 1

    with open(arquivo_usuarios, "a", encoding="utf-8") as f:
        f.write(f"{novo_id};{nome};{senha}\n")
    print("Usuário foi cadastrado!")

def login():
    usuarios = carregar()

    print("\n-----Login-----")
    nome = input("Nome: ").strip()
    senha = input("Senha: ").strip()

    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha:
            print("Login efetuado com sucesso!")
            return u
    print("Nome/Senha incorretos!")
    return None

def menu():
    comecar()

    while True:
        print("\n-----FEITV-----")
        print("1 - Cadastrar Usuário")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            usuario = login()
            if usuario:
                print(f"Seja Bem-Vindo de Volta, {usuario['nome']}!")
                menu_videos(usuario)

        elif opcao == "3":
            print("ENCERRANDO...")
            break

        else:
            print("Opção inválida!")

def carregar_videos():
    videos = []

    with open("videos.txt", "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            if linha:
                partes = linha.split(";")

                video = {
                    "id": int(partes[0]),
                    "titulo": partes[1],
                    "tipo": partes[2],
                    "genero": partes[3],
                    "descricao": partes[4],
                    "ano": partes[5]
                }

                videos.append(video)

    return videos

def menu_videos(usuario):
    while True:
        print("\n----- MENU DE VÍDEOS -----")
        print("1 - Ver vídeos disponíveis")
        print("2 - Pesquisar vídeo")
        print("3 - Ver vídeos curtidos")
        print("4 - Logout")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ver_videos_disponiveis(usuario)
        elif opcao == "2":
            buscar_video(usuario)
        elif opcao == "3":
            ver_curtidos(usuario)
        elif opcao == "4":
            print("Fazendo logout...")
            break
        else:
            print("Opção inválida!")

def buscar_video(usuario):
    nome = input("Digite o nome do vídeo: ").strip().lower()
    videos = carregar_videos()

    encontrados = []

    for v in videos:
        if nome in v["titulo"].lower():
            encontrados.append(v)

    if not encontrados:
        print("Nenhum vídeo encontrado.")
        return

    print("\n--- RESULTADOS ---")
    for v in encontrados:
        print(f"ID: {v['id']}")
        print(f"Título: {v['titulo']}")
        print(f"Tipo: {v['tipo']}")
        print(f"Gênero: {v['genero']}")
        print(f"Descrição: {v['descricao']}")
        print(f"Ano: {v['ano']}")
        print("-" * 20)

    curtir = input("Digite o ID do vídeo que você deseja curtir (ou deixe em branco para voltar): ").strip()
    if curtir:
        curtir_video(usuario, curtir)

def ver_videos_disponiveis(usuario):
    videos = carregar_videos()
    print("\n--- Lista de vídeos disponíveis ---")
    for v in videos:
        print(f"ID: {v['id']}")
        print(f"Título: {v['titulo']}")
        print(f"Tipo: {v['tipo']}")
        print(f"Gênero: {v['genero']}")
        print(f"Descrição: {v['descricao']}")
        print(f"Ano: {v['ano']}")
        print("-" * 30)
    
    curtir = input("Digite o ID do vídeo que você deseja curtir (ou deixe em branco para voltar): ").strip()
    if curtir:
        curtir_video(usuario, curtir)

def curtir_video(usuario, id_video):
    with open(arquivo_curtidas, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() == f"{usuario['id']};{id_video}":
                print("Você já curtiu este vídeo!")
                return

    with open(arquivo_curtidas, "a", encoding="utf-8") as f:
        f.write(f"{usuario['id']};{id_video}\n")

    print("Vídeo curtido com sucesso!")

def ver_curtidos(usuario):
    with open(arquivo_curtidas, "r", encoding="utf-8") as f:
        curtidos = []
        for linha in f:
            if linha.startswith(f"{usuario['id']};"):
                partes = linha.strip().split(";")
                id_video_str = partes[1].strip()
                if id_video_str.isdigit():  # Verifica se é um número
                    id_video = int(id_video_str)
                    curtidos.append(id_video)
                

    if not curtidos:
        print("Nenhum vídeo curtido ainda.")
        return

    videos = carregar_videos()
    print("\n--- Seus vídeos curtidos ---")
    for v in videos:
        if v["id"] in curtidos:
            print(f"ID: {v['id']}")
            print(f"Título: {v['titulo']}")
            print(f"Tipo: {v['tipo']}")
            print(f"Gênero: {v['genero']}")
            print(f"Descrição: {v['descricao']}")
            print(f"Ano: {v['ano']}")
            print("-" * 30)


if __name__ == "__main__":
    menu()