import json

# Leitura do arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamento_mensal = json.load(file)

# Cálculo do menor valor de faturamento
menor_faturamento = min(faturamento_mensal)

# Cálculo do maior valor de faturamento
maior_faturamento = max(faturamento_mensal)

# Cálculo da média mensal, ignorando dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in faturamento_mensal if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Cálculo do número de dias com faturamento superior à média mensal
dias_acima_da_media = len([faturamento for faturamento in faturamento_mensal if faturamento > media_mensal])

# Impressão dos resultados
print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")