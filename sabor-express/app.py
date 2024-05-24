import os

restaurantes = [
  {"nome":"Praça", "categoria":"Japonesa", 'ativo': False},
  {"nome":"Pizza Suprema", "categoria":"Pizza", 'ativo': True},
  {"nome":"Cantina", "categoria":"Italiana", 'ativo': False},
]

def exibir_nome_do_programa():
  print('Sabor Express\n')

def voltar_ao_menu_principal():
  input("Digite uma tecla para voltar ao menu principal")
  main()

def exibir_subtitulo(titulo):
  os.system('cls')
  linha = "*" * (len(titulo) + 4)
  print(linha)
  print(f"{titulo}")
  print(linha)
  print()

def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Alternar estado do restaurante')
  print('4. Sair')

def finalizar_app():
  exibir_subtitulo("App finalizado")

def opcao_invalida():
  print("Opção invalida!\n")
  voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
  """ Essa função é responsável por cadastrar um novo restaurante

  Inputs:
  - Nome do restaurante
  - Categoria

  Outputs:
  - Adiciona um novo restaurante a lista de restaurantes
  """
  exibir_subtitulo("Cadastro de novos restaurantes")
  nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
  categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
  dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
  restaurantes.append(dados_do_restaurante)
  print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
  voltar_ao_menu_principal()

def listar_restaurantes():
  exibir_subtitulo("Listando os restaurantes")

  print(f"- {"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria_restaurante = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo'] else 'desativado'
    print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")

  voltar_ao_menu_principal()

def alternar_estado_restaurante():
  exibir_subtitulo("Alternando estado do restaurante")
  
  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
  restaurante_encontrado = False
  
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo']
      mensagem = f"O restaurante {nome_restaurante} está ativo" if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)
  
  if not restaurante_encontrado:
    print("O restaurante não foi encontrado")

  voltar_ao_menu_principal()

def escolher_opcao():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      alternar_estado_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()