valor = float('{:0.2f}'.format(float(input()))) #TODO

print(valor)

valora = valor % 100
valorb = valor / 100
print(int(valorb) , "nota(s) de R$ 100,00")

valorc = valora % 50
valord = valora / 50
print(int(valord) , "nota(s) de R$ 50,00")

valore = valorc % 20
valorf = valorc / 20
print(int(valorf) , "nota(s) de R$ 20,00")

valorg = valore % 10
valorh = valore / 10
print(int(valorh) , "nota(s) de R$ 10,00")

valori = valorg % 5
valorj = valorg / 5
print(int(valorj) , "nota(s) de R$ 5,00")

valork = valori % 2
valorl = valori / 2
print(int(valorl) , "nota(s) de R$ 2,00")

valorm = valork % 1
valorn = valork / 1
print(int(valorn) , "nota(s) de R$ 1,00")

#0.50
valordv050 = valorm / 0.50
print ('moedas de 050 ' +  str(int(valordv050)));
valordf050 = valorm % 0.50

print("------------------------------")

#0.25
valordv025 = valordf050 / 0.25
print("moedas de 025 " + str(int(valordv025)));
valordf025 = valordf050 % 0.25

print("------------------------------")

#0.10
valordv010 = valordf025 / 0.10
print("moedas de 010 " + str(int(valordv010)));
valordf010 = valordf025 % 0.10

print("------------------------------")

#0.05
valordf010
valordv005 = valordf010 / 0.05
print("moedas de 005 " + str(int(valordv005)));
valordf005 = valordf010 % 0.05

print("------------------------------")

#0.01
valordv001 = valordf005 / 0.01
print("moedas de 001 " + str(int(valordv001)));
#valordf001 = valordf005 % 0.01