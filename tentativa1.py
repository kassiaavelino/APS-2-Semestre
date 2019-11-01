from time import sleep
import os
#lista contendo o alfabeto que será utilizado na cifragem
alfabeto = [' ','.',',','á','à','é','è','ã','ó','ò','õ',
'a','ô','ê','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
'1','2','3','4','5','6','7','8','9','0','A','B','C','D',
'E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z',
]

#variável chave será o número utilizado para cifrar e decifrar a mensagem    
def cifrar (msg, chave):
    #armazenará o resultado da cifragem
    msgCifrada = ''
    #Esse loop percorrerá cada caractere da mensagem que virá a ser cifrada
    for caracter in msg:    
#        esse contador será utilzado para verificar em qual indice o caractere da volta está no vetor alfabeto
        for i in range(len(alfabeto)):
            if (alfabeto[i] == caracter):
                if ((i+chave) > len(alfabeto)):
                    msgCifrada = msgCifrada + alfabeto[i + chave]
                else:    
                    msgCifrada = msgCifrada + alfabeto[i + chave]
    return msgCifrada

def decifrar (msg, chave):
    #armazenará o resultado da cifragem
    msgDecifrada = ''
    #Esse loop percorrerá cada caractere da mensagem que virá a ser cifrada
    for caracter in msg:
#        esse contador será utilzado para verificar em qual indice o caractere da volta está no vetor alfabeto
        for i in range(len(alfabeto)):
            
            if (alfabeto[i] == caracter):
                msgDecifrada = msgDecifrada + alfabeto[i - chave]          
    return msgDecifrada            

#essa função servirá para entrada de dados
def inputDados():
    msg = input('\nDigite a mensagem: \n')
    print("=-="*34)
    chave = int(input('Digite um numero inteiro de 1 à 25:\n'))
    print("=-="*34)
    return msg, chave

#essa chave servirá para apresentação dos dados
def outputDados(msg, chave):
    print('\nPara a chave: {}\nO resultado é: {}'.format( chave, msg))
    print('')
    print("=-="*34)

def main():    
    #essa aqui é a estrutura de apresentação do menu
    while(True):
        sleep(1)
        opcMenu = int (input("Selecione a opção desejada\n1. Cifrar\n2. Decifrar\n3. Sair\n"))
        if(opcMenu == 1):
            msg, chave = inputDados()
            result = cifrar(msg, chave)
            outputDados(result, chave) 
            msg_c = open('cifrada.txt','a')
            msg_c.write("\n"+ msg)
            msg_c.close()  

        elif(opcMenu == 2):
            msg, chave = inputDados()
            result = decifrar(msg, chave)
            outputDados(result, chave) 
            msg_c = open('decifrada.txt','a')
            msg_c.write("\n" + msg)
            msg_c.close()  

        elif(opcMenu == 3):
            print("Encerrando a aplicação...")
            break
main()