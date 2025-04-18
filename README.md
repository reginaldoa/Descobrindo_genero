# Descobrindo_genero

Este é um projeto simples em Python que utiliza o algoritmo Random Forest Classifier do scikit-learn para prever o sexo (masculino ou feminino) com base em altura e peso.


O modelo é treinado com uma base simples de dados fictícios com altura (em cm), peso (em kg) e o sexo:

# [altura, peso]
[160, 55] → Feminino  
[170, 65] → Feminino  
[180, 80] → Masculino  
[175, 75] → Masculino  
[165, 60] → Feminino  
[185, 90] → Masculino  


⚙️ Como Funciona
O usuário informa a altura e o peso.
O modelo retorna a previsão do sexo com base nos dados fornecidos.
Também exibe a probabilidade de cada classe (feminino e masculino).


▶️ Como Executar
Instale as dependências:
pip install scikit-learn



Rode o script no terminal:
python nome_do_arquivo.py

Informe sua altura e peso quando solicitado e veja o resultado!

📌 Exemplo de Saída
Digite a altura (cm): 172  
Digite o peso (kg): 68  

Previsão: Feminino  
Probabilidades → Feminino: 85.3%, Masculino: 14.7%


🧠 Tecnologia Utilizada
Python 3
scikit-learn (RandomForestClassifier)
