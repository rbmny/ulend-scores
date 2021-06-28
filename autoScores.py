import pandas as pd

df = pd.read_excel (r'/Users/ricardobomeny/Desktop/ULEND/RatingsPM.xlsx')
# print(df)
dfR = df['Rating']
dfS = df['Score']

scorePre = int(input('Score Pré Análise: '))
scoreCredito = int(input('Score Crédito: '))

for i in range(19):
    if scoreCredito >= dfS[i]:
        compRow = i
        newScore = dfS[i]
        rating = dfR[i]
        print('Rating =', dfR[i])
        break
# print(newScore, rating)
# print(df.loc[df['Rating'] == rating])

garantiaImovel120 = df['Imovel 120%'][compRow]
garantiaImovel80 = df['Imovel 80%'][compRow]
garantiaRecebiveis50 = df['Recebiveis 50%'][compRow]
garantiaRecebiveis150 = df['Recebiveis 150%'][compRow]
garantia20 = df['Garantia 20%'][compRow]
garantia50 = df['Garantia 50%'][compRow]
aval =  df['Aval'][compRow]

def gi120():
    print('Garantia de Imovel 120% =',str(garantiaImovel120*100)+'% + CDI a.m')
def gi80():
    print('Garantia de Imovel 80% =',str(garantiaImovel80*100)+'% + CDI a.m')
def gr50():
    print('Garantia de Recebíveis 50% =',str(garantiaRecebiveis50*100)+'% + CDI a.m')
def gr150():
    print('Garantia de Recebíveis 150% =',str(garantiaRecebiveis150*100)+'% + CDI a.m')
def ga20():
    print('Garantia de Aplicação 20% =',str(garantia20*100)+'% + CDI a.m')
def ga50():
    print('Garantia de Aplicação 50% =',str(garantia50*100)+'% + CDI a.m')
def av():
    print('Aval =',str(aval*100)+'% a.m')


if scorePre < 1000:
    print('Cobertura mínima de garantia real: 0%')
    print('Garantias Disponíveis:')
    gi120()
    gi80()
    gr50()
    gr150()
    ga20()
    ga50()
    av()
if scorePre >= 1000 and scorePre < 1500:
    print('Cobertura mínima de garantia real: 25%')
    print('Garantias Disponíveis:')
    gi120()
    gi80()
    gr50()
    gr150()
    ga20()
    ga50()
if scorePre >= 1500 and scorePre < 2100:
     print('Cobertura mínima de garantia real: 100%')
     print('Garantias Disponíveis:')
     gi120()
     gi80()
     ga20()
     ga50()
if scorePre >= 2100:
    print('Crédito Reprovado')
