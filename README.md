# Mini Projeto Avaliativo - Olist

Script de sanitização de dados desenvolvido utilizando apenas bibliotecas nativas do Python.

---

## Descrição do Projeto

Este projeto tem como objetivo construir um pipeline de sanitização de dados a partir de arquivos CSV da base Olist.

Durante o processamento são realizadas operações de limpeza, padronização e validação dos dados, produzindo estatísticas que auxiliam na análise da qualidade da base.

Foram utilizados os seguintes arquivos:

* olist_products_dataset.csv
* olist_orders_dataset.csv

O sistema realiza:

* Tratamento de dados ausentes;
* Padronização de strings;
* Limpeza utilizando Expressões Regulares (Regex);
* Conversão de datas utilizando datetime;
* Validação de regra de negócio;
* Geração de relatório estatístico final.

---

## Estrutura do Projeto

```text
Projeto/
│
├── funcoes.py
├── main.ipynb
├── README.md
└── .gitignore
```

---

## Bibliotecas Utilizadas

Bibliotecas nativas do Python:

* csv
* re
* datetime

Nenhuma biblioteca externa foi utilizada.

---

## Obtenção dos Dados

Os arquivos CSV não estão incluídos neste repositório.

Para obter os datasets utilizados no projeto:

1. Acesse o repositório:

   https://github.com/fiesc-junior-prado/mine_projeto_bloco_1

2. Clique em **Code** → **Download ZIP**.

3. Extraia os arquivos e copie para a pasta raiz do projeto:

   * olist_products_dataset.csv
   * olist_orders_dataset.csv

4. Certifique-se de que os arquivos estejam na mesma pasta que:

   * funcoes.py
   * main.ipynb

Estrutura esperada para execução:

```text
Projeto/
│
├── funcoes.py
├── main.ipynb
├── olist_products_dataset.csv
├── olist_orders_dataset.csv
├── README.md
└── .gitignore
```

## Guia de Execução

### Windows

1. Instale o Python 3;
2. Instale o Visual Studio Code;
3. Instale as extensões Python e Jupyter;
4. Abra a pasta do projeto;
5. Abra o arquivo main.ipynb;
6. Execute todas as células.

### Linux

1. Verifique a instalação do Python:

```bash
python3 --version
```

2. Instale o VS Code ou Jupyter Notebook;
3. Abra a pasta do projeto;
4. Execute o notebook main.ipynb.

### macOS

1. Verifique a instalação do Python:

```bash
python3 --version
```

2. Instale o VS Code;
3. Instale as extensões Python e Jupyter;
4. Abra a pasta do projeto;
5. Execute o notebook main.ipynb.

---

## Funcionalidades Implementadas

### 1. Tratamento de Dados Ausentes

* Categorias vazias recebem o valor "Sem Categoria";
* Registros com dimensões físicas ausentes ou inválidas são descartados.

### 2. Padronização de Strings

* Conversão para letras minúsculas;
* Remoção de espaços excedentes;
* Limpeza utilizando Expressões Regulares.

### 3. Conversão de Datas

A coluna `order_approved_at` é convertida do formato original para o padrão brasileiro:

```text
2017-05-16 15:05:35
↓
16/05/2017
```

### 4. Validação de Regra de Negócio

Foi analisada a hipótese:

> Pedidos cancelados tendem a apresentar ausência de data de entrega.

### 5. Relatório Estatístico

O sistema apresenta:

* Total de linhas processadas;
* Categorias corrigidas;
* Registros descartados;
* Pedidos cancelados;
* Resultado da validação da hipótese.

---

## Exemplo de Execução

```text
===== RELATÓRIO FINAL =====
Total de linhas processadas de produtos: 32951
Categorias corrigidas: 610
Registros descartados: 6
Pedidos cancelados: 625
Datas nulas com status cancelado: 619
Hipótese de negócio não confirmada.
```
## Análise da Hipótese de Negócio

A hipótese avaliada neste projeto foi:

> Pedidos sem data de entrega estão associados a pedidos cancelados.

Os resultados obtidos indicaram que a hipótese não foi confirmada.
Embora tenham sido identificados pedidos cancelados sem data de entrega, também foram encontrados registros sem data de entrega associados a outros status operacionais. Isso demonstra que a ausência da data de entrega não é um indicador exclusivo de cancelamento do pedido.

---

## Reflexão Teórica sobre Machine Learning

A qualidade dos dados é um dos fatores mais importantes para o sucesso de modelos de Machine Learning. Os sistemas aprendem a partir dos dados e, para tomar decisões, precisam identificar padrões. Dados inconsistentes, incompletos ou mal formatados podem dificultar a obtenção de conclusões que representem corretamente a realidade. Isso pode introduzir vieses em análises estatísticas e em futuros modelos de Inteligência Artificial.

A etapa de sanitização realizada neste projeto demonstra a importância do pré-processamento dos dados antes da aplicação de técnicas de Inteligência Artificial. Ao corrigir inconsistências, tratar valores ausentes e padronizar informações, aumenta-se a confiabilidade dos dados utilizados em análises futuras. Dessa forma, reduz-se o risco de interpretações equivocadas e melhora-se a qualidade das informações que poderão ser utilizadas por algoritmos de aprendizado de máquina.

---

## Autora

Projeto desenvolvido para fins acadêmicos na disciplina de Machine Learning e Visão Computacional.
