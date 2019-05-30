valor = float(input())

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

print ('valorm ' +  str(valorm))
valordv050 = valorm / 0.50
print ('valordv ' +  str(valordv050))
valordf050 = valorm % 0.50
print('valordf ' + str(valordf050))



#0.25

#0.10
'''
valordf10 = valorm % 0.10
print('df ' + str(valordf10))
strs = str(valorm)
valorq10 = int(strs[2:]) / 10
print (int(valorq10),"moedas de 10")
'''
#5

#1


