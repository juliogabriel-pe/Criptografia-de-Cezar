
def menu(): #Finished
    link = "http://www.bosontreinamentos.com.br/seguranca/criptografia-cifra-de-cesar/"

    print('Bem Vindo ao CriptoZero\n')
    print('Esse programa foi feito baseado na criptografia de César\n')
    print(f'Para saber mais sobre a criptografia de César: {link}\n')
    print('1 - Criptografar uma mensagem')
    print('2 - Descriptografar uma mensagem\n')
    print('0 - Sair do Programa')
    
    resposta = input('Digite um valor: ')
    
    if resposta.isnumeric() == True:
        print('Resposta armazenada... Executando!\n')
    else:
        print('Erro! Você digitou algo diferente de numero!\n')
    return resposta


def Criptografar(): #Finished
    print('\nBem vindo a aba de criptografia!\n')
    textoParaCriptografar = input('Digite o texto para criptografar: ')
    textoParaCriptografar = list(textoParaCriptografar)
    quantidadeDeLetras = len(textoParaCriptografar)
    rot = int(input('Digite a quantidade de rotação: '))

    i = 0
    texto_cifrado = ''

    while i < quantidadeDeLetras:
        textoParaCriptografar[i] = chr(ord(textoParaCriptografar[i]) + rot)
        texto_cifrado += textoParaCriptografar[i]
        i += 1

    print(f'\nTexto Criptografado: {texto_cifrado}\n')

#def Descriptografar: