from sklearn.ensemble import RandomForestClassifier

# Dados simples: altura (cm), peso (kg)
# 0 = feminino, 1 = masculino
dados = [
    [160, 55],  # mulher
    [170, 65],  # mulher
    [180, 80],  # homem
    [175, 75],  # homem
    [165, 60],  # mulher
    [185, 90]   # homem
]

# Labels (respostas)
labels = [0, 0, 1, 1, 0, 1]

# Cria o modelo (Random Forest)
modelo = RandomForestClassifier()
modelo.fit(dados, labels)

# Função para fazer a previsão com input do usuário
def prever_sexo():
    # Input de altura e peso
    altura = float(input("Digite a altura (cm): "))
    peso = float(input("Digite o peso (kg): "))
    
    # Faz a previsão
    entrada = [[altura, peso]]
    probabilidade = modelo.predict_proba(entrada)[0]  # [prob_feminino, prob_masculino]
    
    prob_feminino = probabilidade[0] * 100
    prob_masculino = probabilidade[1] * 100
    
    # Resultado mais provável
    classe_prevista = modelo.predict(entrada)[0]
    sexo = "Masculino" if classe_prevista == 1 else "Feminino"
    
    print(f'\nPrevisão: {sexo}')
    print(f'Probabilidades → Feminino: {prob_feminino:.1f}%, Masculino: {prob_masculino:.1f}%')

# Chama a função
prever_sexo()
