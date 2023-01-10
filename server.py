from src.infra.config.database import buscar, atualizaSitEmail, conectar, close, inserindoEmail, buscarsituacao
from src.infra.repositorios.repositoriosFuncs import validaCampo, validaCampoEmail, validaEmail, enviaremail


print("Insirar sua chave para entrar no sistemas")
#validar chave toker, verificando se existe no banco
chave_entrada = input("Digite sua chave: ").strip() # leitura da chave removendo todos os espaços

while True:
    valido = False
    valido = buscar(chave_entrada, "instituicao", "chave_toker") #chave_entrada

    if valido == True:
        #print("Login Valido!")
        print("Seja bem-vindo!")
        break
    else:
        print("ERRO! Chave inválido!")
        chave_entrada = input("Digite sua chave uma válida: ").strip()

#validar campo assunto, verificando ser está vazio campo
print("Entre com Assunto do e-mail!")
infAssunto = input("Digite o Assunto: ")
validaCampo(infAssunto, "Assunto")
#validar campo texto, verificando ser está vazio campo
print("Entre com Texto do e-mail!")
infTexto = input("Digite o Texto: ")
validaCampo(infTexto, "Texto")


print("Entre com endereço de e-mail!")
infEmail = input("Digite o endereço de e-mail: ").replace(" ","")
#salvar o email no banco com o situação Não verificado
a = validaCampoEmail(infEmail, "Endereço de e-mail")
#verificar se o email ja existe no banco, caso exista pular a parte inserir o email
if a == True:
    print("Campo valido", infEmail)
    b = buscar(infEmail, "lista_email2", "email")
    if b == False:
        inserindoEmail(infEmail, "lista_email2", chave_entrada)

#validar o email
teste = validaEmail(infEmail) #esperando resposta de validação Joao Victor
#se email for valido alterar no banco a situação para valido
if teste == True:
    if buscarsituacao(infEmail, "lista_email2", "email", 2) == False:
        atualizaSitEmail("lista_email2", 2, infEmail) #para validos 
else:
    if buscarsituacao(infEmail, "lista_email2", "email", 1) == False:
        atualizaSitEmail("lista_email2", 1, infEmail) #para invalidos

#enviar email
if buscarsituacao(infEmail, "lista_email2", "email", 2) == True:
    enviaremail(infAssunto, infTexto, infEmail)
    print("Email enviado!")
else:
    print("Email não enviado!")
