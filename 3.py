'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

import json

faturamento_json = '''
{
    'faturamento_diario': [100, 200, 0, 300, 0, 500, 400, 0, 600, 700, 800, 0]
}
'''

dados = json.loads(faturamento_json)
faturamento = [dia for dia in dados['faturamento_diario'] if dia > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = sum(1 for dia in faturamento if dia > media_mensal)

print('Menor valor: R${}'.format(menor_valor))
print('Maior valor: R${}'.format(maior_valor))
print('Dias acima da média: {}'.format(dias_acima_media))