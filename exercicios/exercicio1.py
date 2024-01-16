from math import ceil

nome = str(input('qual eo seu nome?: '))
ano_atual = int(input('em que ano estamos mesmo?: '))
ano_nacimento = int(input('em que ano voce nasceu mesmo?: '))

while ano_nacimento < ano_atual: 
    
    idade = ano_atual - ano_nacimento

print(f'{nome} entao quer dizer que nesse ano voce faz ou vai fazer {idade} anos de idade')

validacao = str(input(f'{nome} eu fiquei sabendo que ganhou uma viajem para os estados unidos como presente de aniversario, e verdade isso?: y/n: '))

if validacao == 'y':

    repetir = int(input(f'{nome}, se voçe nao tiver certeza de quantos reais voce tem, voçe pode escolher a quantidade que chutes que voce quer dar: '))

    c = 1

    while c <= repetir:
        reais = int(input(f'{nome} quantos reais voce acha que tem mesmo?: '))
        dolar = 4.91

        conversao = ceil(reais/dolar)

        print(f'{nome} entao voce teria em torno de {conversao} de dollars pra gastar a vontade nos estados unidos')

        c = c + 1

elif validacao == 'n':
    validacao = input(f'entao a fofoca que eu escutei so pode estar errada, por um acaso seu nome nao é {nome}? y/n: ')

print('agora baseado nisso voce pode se planejar um pouco melhor pra viajar')