aparelho = input("Qual é o nome do seu aparelho? (ex: Geladeira): ")
potencia = input("Potência do aparelho em watts(ex: 500): ")
potencia = potencia.replace(" watts", "")
potencia = float(potencia)

tempo = input("Tempo médio do aparelho em horas por dia (ex: 2 horas): ")
tempo = tempo.replace(" horas", "")
tempo = float(tempo)

energia = (potencia * tempo * 30) / 1000

custo = energia * 0.75

print(f"O consumo de energia do {aparelho} é de {energia:.2f} kWh mensais. O custo mensal é de {custo:.2f} reais.")