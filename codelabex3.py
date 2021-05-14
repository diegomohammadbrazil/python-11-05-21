solteiros=casados=separados=viuvos = 0

while True:

    while True:

idade = int(input('Idade: '))

if idade<0:

    idade = abs(idade)
    
    print('Por favor, digite uma idade válida!')

else:
 idade == 0

while True:

    print("Estado civil =

[1] Solteiro,

[2] Casado,

[3] Separado(a)

[4] Viúvo(a)")

 
 est_civil = (input('Digite a opção correspondente: ')).strip()

if est_civil not in ('1', '2', '3', '4'):

    print('Opção inválida!')
continue

print(f'Registrado!\n')

if est_civil == '1':
    solteiros += 1

    elif est_civil == '2'
casados += 1
    
elif est_civil == '3'

separados += 1

else
viuvos += 1

break

print('Fim do registro')

print(f'''

Foram cadastrados {solteiros} solteiros, {casados} casados, {separados} separados e {viuvos} viúvos''')