print('Programa para calcular lucro total do vendedor ao final do mes')
print()

funcionario = input ("Nome do vendedor: ")
salario_fixo = float (input ('Informe o salário fixo do vendedor: '))
total_vendas = float (input ('Informe o total de vendas do mês do funcionário: '))
imposto1 = salario_fixo * 0.10
comissao_vendas = total_vendas * 0.15
comissao_vendas_liquido = comissao_vendas - (comissao_vendas*0.10)


lucroTotal = (salario_fixo - imposto1) + comissao_vendas_liquido

print ("Funcionário: ",funcionario, "Salário Fixo: ", salario_fixo, "Salário com comissão: ", lucroTotal)