"""
Projeto objetiva desenvolver um script em Python (utilizando apenas bibliotecas nativas como csv, re, datetime 
e operadores padrões do python) para construir um pipeline de sanitização. 

"""
import csv
import re
from datetime import datetime

"""
Carrega o arquivo de produtos CSV para arquivo e sanitiza:
1.Validação e Tratamento de Dados Ausentes: 
Criar uma lógica iterativa para ler o arquivo de produtos.
Sempre que encontrar um valor nulo/vazio na coluna product_category_name, 
ele deve ser preenchido com a string "Sem Categoria". 
Para os valores nulos nas dimensões físicas (product_weight_g, product_length_cm, etc.), você deve criar
uma regra de corte (ex: descartar o registro ou atribuir um valor numérico padrão, como média por exemplo),
justificando a sua escolha técnica nos comentários do código.

As dimensões físicas: "product_weight_g","product_length_cm","product_height_cm","product_width_cm",
foram verificadas e para seus valores nulos, o registro foi descartado, pois, 
para a Logística do negócio, produtos sem dimensões não podem ser considerados em termos de análise de dados, 
também para transporte e produtos.

2.Padronização de Strings e Regex: Garantir que todos os nomes de categorias de produtos sejam convertidos estritamente
para letras minúsculas (.lower()) e aplicar a remoção de espaços em branco excedentes 
no início e no fim das strings (.strip()). 
Além disso, utilize Expressões Regulares (módulo re) para limpar eventuais caracteres especiais ou 
pontuações indevidas dos nomes das categorias.
"""

def ler_e_sanitizar_produtos(arquivo_produtos):
    produtos = []
    total_linhas = 0
    categorias_corrigidas = 0
    registros_descartados = 0

    with open(arquivo_produtos, 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            total_linhas += 1

            if not linha['product_category_name']:
                linha['product_category_name'] = 'Sem Categoria'
                categorias_corrigidas += 1
            else:
                linha['product_category_name'] = re.sub(
                    r'[^a-zA-ZÀ-ÿ\s]', '',
                    linha['product_category_name'].lower().strip()
                )

            if (
                linha['product_weight_g'] in ['', '0'] or
                linha['product_length_cm'] in ['', '0'] or
                linha['product_height_cm'] in ['', '0'] or
                linha['product_width_cm'] in ['', '0']
            ):
                registros_descartados += 1
                continue

            produtos.append(linha)

    estatisticas = {
        'total_linhas': total_linhas,
        'categorias_corrigidas': categorias_corrigidas,
        'registros_descartados': registros_descartados
    }

    return produtos, estatisticas

"""
4.Formatação Temporal (Datetime): 
Utilize o módulo nativo datetime para ler a coluna de data de aprovação do pedido (order_approved_at) e convertê-la 
do formato de string original (ex: "2017-05-16 15:05:35") para um formato de data simplificado brasileiro (ex: "16/05/2017"). 
Como será utilizado na análise de pedidos, está antes do item 3.
"""

def converter_data(data_texto):
    if not data_texto:
        return ''

    data = datetime.strptime(data_texto, '%Y-%m-%d %H:%M:%S')
    return data.strftime('%d/%m/%Y')

"""
3.Lógica de Regra de Negócio (Filtros e Validação): 
A diretoria identificou que muitas datas de entrega (order_delivered_customer_date) estão vazias. 
Utilizando estruturas condicionais (if/elif/else), separe esses registros e comprove a hipótese de negócio da Olist:
essas datas estão nulas obrigatoriamente porque o status do pedido (order_status) consta como cancelado (canceled)? 
"""

def analisar_pedidos(arquivo_pedidos):
    
    pedidos_cancelados = 0
    datas_nulas_canceladas = 0
    datas_nulas_nao_canceladas = 0

    with open(arquivo_pedidos, 'r', encoding='utf-8', newline='') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            if linha['order_status'] == 'canceled':
                pedidos_cancelados += 1

            if not linha['order_delivered_customer_date']:
                if linha['order_status'] == 'canceled':
                    datas_nulas_canceladas += 1
                else:
                    datas_nulas_nao_canceladas += 1

            if linha['order_approved_at']:
                linha['order_approved_at'] = converter_data(
                    linha['order_approved_at']
                )

    return {
        'pedidos_cancelados': pedidos_cancelados,
        'datas_nulas_canceladas': datas_nulas_canceladas,
        'datas_nulas_nao_canceladas': datas_nulas_nao_canceladas
        }

"""
Relatório de Status Manual
5.Relatório de Status Manual: Ao final do processamento, seu script deve calcular e exibir na tela 
um sumário estatístico construído manualmente (
contagem total de linhas processadas, 
total de registros nulos corrigidos e
total de pedidos cancelados identificados), 
validando se a base está sanitizada.
"""

def relatorio_final(estat_produtos, estat_pedidos):
    print('===== RELATÓRIO FINAL =====')
    print(f"Total de linhas processadas de produtos: {estat_produtos['total_linhas']}")
    print(f"Categorias corrigidas: {estat_produtos['categorias_corrigidas']}")
    print(f"Registros descartados: {estat_produtos['registros_descartados']}")
    print(f"Pedidos cancelados: {estat_pedidos['pedidos_cancelados']}")
    print(f"Datas nulas com status cancelado: {estat_pedidos['datas_nulas_canceladas']}")
    if estat_pedidos['datas_nulas_nao_canceladas'] == 0:
        print("Hipótese de negócio confirmada.")
    else:
        print("Hipótese de negócio não confirmada.")