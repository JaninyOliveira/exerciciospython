print('Programa para calcular equivalência de idade em anos para equivalência da idade no formato ano(s), mes(es) e dia(s) ')
print()

idadeDias = int (input ('Informe a idade em dias: '))
anos = int(idadeDias /365)
meses = int(int(idadeDias % 365)/30)
dias = int(int(idadeDias % 365)%30)
print ("Idade:","(",idadeDias,")", "#",anos," anos,",meses," meses e ",dias," dias.")