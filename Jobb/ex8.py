#8 - Crie u programa que receba  do usuário nome, idade, altura, cidade e estado e exiba a seguinte frase na tela : "Olá, meu nome é ___, tenho __ anos de idade. Moro na cidade de__________/__". Use prift

nome = input('qual seu nome? ')
idade = input('qual sua idade? ')
altura = input('qual sua altura? ')
cidade = input('qual sua cidade? ')
estado = input('qual seu estado? ')
print(f'Olá, meu nome é {nome}, tenho {idade} anos de idade. Moro na cidade de {cidade}/{estado}')