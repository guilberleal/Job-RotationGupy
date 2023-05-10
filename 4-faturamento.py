faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do valor total mensal
total_mensal = sum(faturamento_mensal.values())

# Cálculo do percentual de representação de cada estado
percentuais = {estado: (faturamento / total_mensal) * 100 for estado, faturamento in faturamento_mensal.items()}

# Impressão dos resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
