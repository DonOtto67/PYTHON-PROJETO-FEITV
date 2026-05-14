import os

caminho = os.path.dirname(os.path.abspath(__file__))

arquivo_usuarios = os.path.join(caminho, "usuarios.txt") 
arquivo_curtidas = os.path.join(caminho, "curtidas.txt") 
arquivo_favoritos = os.path.join(caminho, "favoritos.txt")  
arquivo_videos = os.path.join(caminho, "videos.txt") 

# Verifica se o arquivo existe, senao existir ele cria.
def comecar():
    if not os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, "w", encoding="utf-8") as arquivo:
            pass

    if not os.path.exists(arquivo_curtidas):
        with open(arquivo_curtidas, "w", encoding="utf-8") as arquivo:
            pass

    if not os.path.exists(arquivo_favoritos):
        with open(arquivo_favoritos, "w", encoding="utf-8") as arquivo:
            pass

    if not os.path.exists(arquivo_videos):
        with open(arquivo_videos, "w", encoding="utf-8") as arquivo:
            pass

def carregar():
    usuarios = []

    with open(arquivo_usuarios, "r", encoding="utf-8") as arquivo: #Abre como leitor
        for linha in arquivo: # Fazer com que ele percorra as linhas do arquivo
            linha = linha.strip()
            if linha: # Verifica se a linha esta vazia
                partes = linha.split(";") # Separa a linha em varios pedaços
                usuario = { # Transforma "Usuario" em dicionario
                    "id": int(partes[0]),
                    "nome": partes[1],
                    "senha": partes[2]
                }
                usuarios.append(usuario)
    return usuarios

def cadastrar():
    usuarios = carregar() # Carrega os usuarios 
    print("\n-----Cadastro-----") 
    nome = input("Nome de usuário: ").strip() # Pergunta o nome (sem espaços)
    senha = input("Senha: ").strip() # Pergunta a senha (sem espaços)
    for u in usuarios: # Verifica se o usuario ja existe
        if u["nome"].lower() == nome.lower():
            print("Usuário já existente!") # Se ja existir aparece a mensagem e volta
            return
    novo_id = 1 # Define o primeiro ID
    if usuarios: # Se ja existir um usuario
        novo_id = usuarios[-1]["id"] + 1 # Pega o ultimo item da lista e depois adiciona 1 no proximo ID
    with open(arquivo_usuarios, "a", encoding="utf-8") as f: # abre o arquivo como append (Só adiciona e nao apaga)
        f.write(f"{novo_id};{nome};{senha}\n") # Escreve o novo usuario
    print("Usuário foi cadastrado!") # Escreve

def login(): 
    usuarios = carregar() # Carrega TODOS os usuarios
    print("\n-----Login-----") #Titulo
    nome = input("Nome: ").strip() # Pede o nome (Sem Espaços)
    senha = input("Senha: ").strip() # Pede a senha (Sem Espaços)
    for u in usuarios:
        if u["nome"] == nome and u["senha"] == senha: #Verifica se o nome e a senhas estao iguais aos cadastrados
            print("Login efetuado com sucesso!") # Se der certo
            return u # Termina a funcao se o usuario estiver certo
    print("Nome/Senha incorretos!") # Se nao der certo
    return None # Nao retorna NADA (ai reinicia)

def carregar_videos():
    videos = [] #cria lista vazia

    with open(arquivo_videos, "r", encoding="utf-8") as arquivo: # Abre o arquivo como leitor
        for linha in arquivo: # para percorrer as linhas do aruivo
            linha = linha.strip() # Tira os espacos
            if linha: # Para nao processar linhas vazias
                partes = linha.split(";") #separa com ;
                video = { #cria um dicionario
                    "id": int(partes[0]), #transforma em num inteiro
                    "titulo": partes[1], #Separa
                    "tipo": partes[2], #Separa
                    "genero": partes[3], #Separa
                    "descricao": partes[4], #Separa
                    "ano": partes[5] #Separa
                }
                videos.append(video) #Adiciona na lista
    return videos # CHAMA A LISTA

def curtir_video(usuario, id_video):
    with open(arquivo_curtidas, "r", encoding="utf-8") as arquivo: # ABRE O ARQUIVO DE CURTIDAS COMO LEITOR
        for linha in arquivo: #passa por todas as curtidas ja salvas
            if linha.strip() == f"{usuario['id']};{id_video}": # Cria uma linha com o ID do usuario e do video
                print("Você já curtiu este vídeo!")
                return # Para a funçao
    with open(arquivo_curtidas, "a", encoding="utf-8") as f: # ABRE o ARQUIVO COMO APPEND
        f.write(f"{usuario['id']};{id_video}\n") # Escreve no final do arquivo
    print("Vídeo curtido com sucesso!") # mostra se deu certo

def ver_videos_disponiveis(usuario): # Cria a funçao recebendo o usuario logado
    videos = carregar_videos() #  chama a funçao que le o video.txt
    print("\n--- Lista de vídeos disponíveis ---") # Titulo
    for v in videos: # passa por TODOS os video
        print(f"ID: {v['id']}") # mostra as informaçoes do video
        print(f"Título: {v['titulo']}") # mostra as informaçoes do video
        print(f"Tipo: {v['tipo']}") # mostra as informaçoes do video
        print(f"Gênero: {v['genero']}") # mostra as informaçoes do video
        print(f"Descrição: {v['descricao']}") # mostra as informaçoes do video
        print(f"Ano: {v['ano']}") # mostra as informaçoes do video
        print("-" * 30) #repete o "-" 30 vzs para decorar
    curtir = input( #para digitar o video que quer curtir
        "Digite o ID do vídeo que você deseja curtir (ou deixe em branco para voltar): "
    ).strip()
    if curtir: #Se nao estiver vazio, Se estiver vazio o if vai ser false
        curtir_video(usuario, curtir) # chama a funcao de curtir

def buscar_video(usuario): # Cria a funçao recebendo o usuario logado
    nome = input("Digite o nome do vídeo: ").strip().lower() # O usuario digita o nome do video
    videos = carregar_videos() # Pega todos os video
    encontrados = [] # Cria outra lista
    for v in videos: # cada V é um video
        if nome in v["titulo"].lower(): # Verifica se o nome esta no titulo e permite q o usuario nao tenha q digitar exatamente o nome do video
            encontrados.append(v) # adiciona na lista
    if not encontrados: # Se nao encontrar
        print("Nenhum vídeo encontrado.")
        return # para a funçao
    print("\n--- RESULTADOS ---") # titulo
    for v in encontrados:
        print(f"ID: {v['id']}") # mostra as informaçoes
        print(f"Título: {v['titulo']}") # mostra as informaçoes
        print(f"Tipo: {v['tipo']}") # mostra as informaçoes
        print(f"Gênero: {v['genero']}") # mostra as informaçoes
        print(f"Descrição: {v['descricao']}") # mostra as informaçoes
        print(f"Ano: {v['ano']}") # mostra as informaçoes
        print("-" * 20)
    curtir = input( # pede o ID do video
        "Digite o ID do vídeo que você deseja curtir (ou deixe em branco para voltar): "
    ).strip()
    if curtir: # ve se algo foi digitado
        curtir_video(usuario, curtir) # chama a funçao de curtir

def descurtir_video(usuario, id_video): # Cria a funçao recebendo o usuario e o ID do video
    id_video = int(id_video) # define o ID como inteiro
    curtidos = [] # cria a lista
    with open(arquivo_curtidas, "r", encoding="utf-8") as arquivo: # abre o arquivo como leitor
        for linha in arquivo: # passa em todas as linhas
            if linha.startswith(f"{usuario['id']};"): # verifica se a curtida é do usuario logado
                partes = linha.strip().split(";") # remove os espacos e separa com ";"
                id_video_str = partes[1].strip() # pega o ID do video
                if id_video_str.isdigit(): # Ve se é numero
                    curtidos.append(int(id_video_str)) # adiciona nas curtidas
    if id_video not in curtidos: # ve se ja foi curtido
        print("Você não curtiu nenhum vídeo com este ID.") # se nao curtiu
    else: # se curtiu
        linhas_restantes = [] # cria a lista das linha q nn vao ser removidas
        with open(arquivo_curtidas, "r", encoding="utf-8") as arquivo: # abre o arquivo de novo
            for linha in arquivo: # le as linhas
                if linha.strip() != f"{usuario['id']};{id_video}": # ignora a curtida que vai ser removida
                    linhas_restantes.append(linha) # adiciona as linhas que ficaram
        with open(arquivo_curtidas, "w", encoding="utf-8") as arquivo: # Abre o arquivo com escritor
            arquivo.writelines(linhas_restantes) # escreve as linhas de novo
        print("Curtida removida com sucesso!") # mostra que deu certo

def ver_curtidos(usuario): # cria a funçao e chama o usuario
    curtidos = []  # cria a lista
    with open(arquivo_curtidas, "r", encoding="utf-8") as arquivo: # abre o arquivo como leitor
        for linha in arquivo: # le todas as linhas 
            if linha.startswith(f"{usuario['id']};"): # ve se a curtida foi feita pelo usuario logado
                partes = linha.strip().split(";") # tira espacos e separa
                id_video_str = partes[1].strip() # pega o id do video
                if id_video_str.isdigit(): # ve se é numero
                    curtidos.append(int(id_video_str)) # adiciona na lista
    if not curtidos: # se nao tiver curtidos
        print("Nenhum vídeo curtido ainda.") # aviso
        return # para a funçao
    videos = carregar_videos() # carrega todos os videos
    print("\n--- Seus vídeos curtidos ---") # titulo
    for v in videos: # cada v é um video
        if v["id"] in curtidos: # ve se o ID foi curtido
            print(f"ID: {v['id']}") # mostra as informaçoes
            print(f"Título: {v['titulo']}") # mostra as informaçoes
            print(f"Tipo: {v['tipo']}") # mostra as informaçoes 
            print(f"Gênero: {v['genero']}") # mostra as informaçoes
            print(f"Descrição: {v['descricao']}") # mostra as informaçoes
            print(f"Ano: {v['ano']}") # mostra as informaçoes
            print("-" * 30) # da 30 "-" para deixa bonito
    while True:
        descurtir = input("Você quer descurtir algum vídeo? Digite o ID do vídeo (ou deixe em branco para voltar): ").strip()# pede o ID para descurtir
        if descurtir == "": # se apertar enter
            break # para
        if not descurtir.isdigit(): # ve se e numero
            print("ID inválido! Tente novamente.") # da erro
            continue # faz o loop recomecar
        descurtir_video(usuario, descurtir) # tira a curtida

def favoritar_video(usuario): # cria a funçao e chama o usuario
    videos = carregar_videos() # carrega todos os videos
    print("\n--- Lista de vídeos disponíveis para favoritar ---") # titulo
    for v in videos: # cada v é um video
        print(f"ID: {v['id']}") # mostra as informaçoes
        print(f"Título: {v['titulo']}") # mostra as informaçoes
        print(f"Tipo: {v['tipo']}") # mostra as informaçoes 
        print(f"Gênero: {v['genero']}") # mostra as informaçoes 
        print(f"Descrição: {v['descricao']}") # mostra as informaçoes
        print(f"Ano: {v['ano']}") # mostra as informaçoes
        print("-" * 30) # da 30 "-" para enfeitar
    id_video = input("Digite o ID do vídeo que você deseja favoritar (ou deixe em branco para voltar): ").strip() # pede o ID para favoritar
    if id_video == "": # se der enter
        return # para a funçao
    if not id_video.isdigit(): # ve se é numero
        print("ID inválido! Tente novamente.") # erro
        return # para a funçao
    id_video = int(id_video) # deixa o ID como inteiro
    with open(arquivo_favoritos, "r", encoding="utf-8") as arquivo: # abre o arquivo como leitor
        for linha in arquivo: # le todas as linhas
            if linha.strip() == f"{usuario['id']};{id_video}": # ve se ja foi favoritado
                print("Você já favoritou este vídeo!") # aviso
                return # para 
    with open(arquivo_favoritos, "a", encoding="utf-8") as arquivo: # Abre o arquivo como append
        arquivo.write(f"{usuario['id']};{id_video}\n") # adiciona a curtida
    print("Vídeo favoritado com sucesso!") # aviso de sucesso

def desfavoritar_video(usuario, id_video): # cria a funcao e chama o usuario e o id do video
    id_video = int(id_video)  # Garantir que é um inteiro
    favoritos = [] # cria a lista favoritos
    with open(arquivo_favoritos, "r", encoding="utf-8") as arquivo: # abre como leitor 
        for linha in arquivo: #le todas as linhas
            if linha.startswith(f"{usuario['id']};"): # ve se o ID e o do usuario
                partes = linha.strip().split(";") # tira os espacos e separa
                id_video_str = partes[1].strip() # pega o ID do video
                if id_video_str.isdigit(): # ve se e numero
                    favoritos.append(int(id_video_str)) # adiciona na lista
    if id_video not in favoritos: # ve se esta na lista de favoritos
        print("Você não favoritou nenhum vídeo com este ID.") # ERRO
    else:
        linhas_restantes = [] # cria lista das linhas que vao sobrar
        with open(arquivo_favoritos, "r", encoding="utf-8") as arquivo: # abrir o arquivo como leitor
            for linha in arquivo: # le todas as linhas
                if linha.strip() != f"{usuario['id']};{id_video}": # ignora o favorito que sera removido
                    linhas_restantes.append(linha) # salva as linhas que ficaram
        with open(arquivo_favoritos, "w", encoding="utf-8") as arquivo: # abre como editor 
            arquivo.writelines(linhas_restantes) # escreve as linhas restantes
        print("Favorito removido com sucesso!") # mensagem

def menu_favoritos(usuario): # cria a funcao da interface e chama usuario
    while True:
        print("\n----- FAVORITOS -----") # mostra o menu
        print("1 - Favoritar um vídeo") # mostra o menu
        print("2 - Ver favoritos") # mostra o menu
        print("3 - Excluir favorito") # mostra o menu
        print("4 - Voltar ao menu de vídeos") # mostra o menu
        opcao = input("Escolha uma opção: ").strip() # pergunta qual opcao vai ser escolhida
        if opcao == "1": # se digitar 1
            favoritar_video(usuario) # chama a funcao de favoritar um vídeo
        elif opcao == "2": # se digitar 2
            ver_favoritos(usuario) # chama a funcao de ver os favoritos
        elif opcao == "3": # se digitar 3
            ver_favoritos(usuario) # chama a funcao de ver os favoritos de novo
            id_video = input("Digite o ID do vídeo que você quer desfavoritar (ou deixe em branco para voltar): ").strip() # pergunta o ID do video
            if id_video: # ve se digitou alguma coisa
                if not id_video.isdigit(): # ve se e numero
                    print("ID inválido! Tente novamente.") # mostra erro
                    continue # para a funcao
                desfavoritar_video(usuario, id_video) # Chamar a função de desfavoritar
        elif opcao == "4": # se digitar 4
            break # para
        else: # se digitar outra coisa
            print("Opção inválida!") # erro

def ver_favoritos(usuario): # cria a funcao para ver os favoritos e chama o usuario
    favoritos = [] # cria a lista favoritos
    with open(arquivo_favoritos, "r", encoding="utf-8") as arquivo: # abrir o arquivo como leitor
        for linha in arquivo: # le todas as linhas
            if linha.startswith(f"{usuario['id']};"): # ve se a linha e do usuario ativo
                partes = linha.strip().split(";") # tira espacos e separa
                id_video_str = partes[1].strip() # pega ID do video
                if id_video_str.isdigit(): # ve se e numero
                    favoritos.append(int(id_video_str)) # adiciona na lista
    if not favoritos: # se nao tiver favoritos
        print("Nenhum vídeo favoritado ainda.") # mostra mensagem
        return # para a funcao
    videos = carregar_videos() # carregas os video
    print("\n--- Seus vídeos favoritados ---") # titulo
    for v in videos: # cada v e um video
        if v["id"] in favoritos: # ve se o ID esta nos favoritos
            print(f"ID: {v['id']}") # mostra as informaçoes
            print(f"Título: {v['titulo']}") # mostra as informaçoes
            print(f"Tipo: {v['tipo']}") # mostra as informaçoes
            print(f"Gênero: {v['genero']}") # mostra as informaçoes
            print(f"Descrição: {v['descricao']}") # mostra as informaçoes
            print(f"Ano: {v['ano']}") # mostra as informaçoes
            print("-" * 30) # mostra 30 "-" para decorar

def menu_videos(usuario): # cria a funcao do menu dos videos e chama o usuario
    while True:
        print("\n----- MENU DE VÍDEOS -----") # Cria os topicos
        print("1 - Ver vídeos disponíveis") # Cria os topicos
        print("2 - Pesquisar vídeo") # Cria os topicos
        print("3 - Ver vídeos curtidos") # Cria os topicos
        print("4 - Favoritos") # Cria os topicos
        print("5 - Logout") # Cria os topicos
        opcao = input("Escolha uma opção: ").strip() # pergunta qual opcao deve ser selecionada
        if opcao == "1": # se digitar 1 
            ver_videos_disponiveis(usuario) # chama a funcao para ver os videos
        elif opcao == "2": # se digitar 2
            buscar_video(usuario) # chama a funcao para buscar o video
        elif opcao == "3": # se digitar 3 
            ver_curtidos(usuario) # chama a funcao para ver os curtidos
        elif opcao == "4": # se digitar 4
            menu_favoritos(usuario) # chama a funcao para ver a interface dos favoritos
        elif opcao == "5": # se digitar 5 
            print("Fazendo logout...") # sai do usuario logado
            break # para o while
        else:
            print("Opção inválida!") # opcoes invalidas

def menu(): # cria a funcao do menu inicial
    comecar() # chama a funcao de comeco para garantir os arquivos
    while True:
        print("\n-----FEITV-----") # Cria os topicos
        print("1 - Cadastrar Usuário") # Cria os topicos
        print("2 - Login") # Cria os topicos
        print("3 - Sair") # Cria os topicos
        opcao = input("Escolha uma opção: ").strip() # pergunta qual opcao vai sert selecionada
        if opcao == "1": # se digitar 1 
            cadastrar() # chama a funcao de cadastro
        elif opcao == "2":  # se digitar 2
            usuario = login() # chama o login
            if usuario: # ve se o login funcionou 
                print(f"Seja Bem-Vindo de Volta, {usuario['nome']}!") # mensagem de recepcao
                menu_videos(usuario) # abre o menu dos videos
        elif opcao == "3":  # se digitar 3
            print("ENCERRANDO...") #mensagem de parada
            break # para
        else:
            print("Opção inválida!") # digitou algo errado


if __name__ == "__main__": # E usado quando o arquivo e executado diretamente
    menu() # comeca o menu
