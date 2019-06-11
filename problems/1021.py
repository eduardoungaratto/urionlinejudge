valor = float('{:0.3f}'.format(float(input()))) #TODO

print("NOTAS:");

valora = valor % 100
valorb = valor / 100
print("nota(s) de R$ 100,00" + str(int(valorb)));

valorc = valora % 50
valord = valora / 50
print("nota(s) de R$ 50,00" + str(int(valord)));

valore = valorc % 20
valorf = valorc / 20
print("nota(s) de R$ 20,00" + str(int(valorf)));

valorg = valore % 10
valorh = valore / 10
print("nota(s) de R$ 10,00" + str(int(valorh)));

valori = valorg % 5
valorj = valorg / 5
print("nota(s) de R$ 5,00" + str(int(valorj)));

valork = valori % 2
valorl = valori / 2
print("nota(s) de R$ 2,00" + str(int(valorl)));

print("MOEDAS:");

valorm = valork % 1
valorn = valork / 1
print("moeda(s) de R$ 1,00" + str(int(valorn)));

#0.50
valordv050 = valorm / 0.50
print ('moeda(s) de R$ 0.50 ' +  str(int(valordv050)));
valordf050 = valorm % 0.50

#0.25
valordv025 = valordf050 / 0.25
print("moeda(s) de R$ 0.25 " + str(int(valordv025)));
valordf025 = valordf050 % 0.25

#0.10
valordv010 = valordf025 / 0.10
print("moeda(s) de R$ 0.10 " + str(int(valordv010)));
valordf010 = valordf025 % 0.10

#0.05
valordf010
valordv005 = valordf010 / 0.05
print("moeda(s) de R$ 0.05 " + str(int(valordv005)));
valordf005 = valordf010 % 0.05

#0.01
valordv001 = valordf005 / 0.01
print(str(int(valordv001)) + "moeda(s) de R$ 0.01");
#valordf001 = valordf005 % 0.01