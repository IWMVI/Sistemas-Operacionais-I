# Exercício de Leitura e Filtragem de Dados CSV

Este projeto consiste em uma aplicação Python que lê um arquivo CSV (`generic_food.csv`), valida a existência da pasta e do arquivo, filtra os alimentos do grupo "Fruits" e exibe os resultados no console em formato tabular.

## Requisitos

### Arquivo CSV:
- O arquivo `generic_food.csv` deve estar localizado na pasta `C:\TEMP`.
- O arquivo pode ser baixado do seguinte link: `generic_food.csv`.

### Estrutura do CSV:
O arquivo CSV deve conter as colunas:
- `FOOD NAME`
- `SCIENTIFIC NAME`
- `GROUP`
- `SUBGROUP`

### Ambiente de Execução:
- Python 3.x instalado.
- Biblioteca `tabulate` instalada (o script instala automaticamente caso não esteja presente).

## Funcionalidades

### Validação de Pasta e Arquivo:
- Verifica se a pasta `C:\TEMP` existe.
- Verifica se o arquivo `generic_food.csv` está presente na pasta.

### Filtragem de Dados:
- Lê o arquivo CSV.
- Filtra os alimentos cujo `GROUP` é "Fruits".

### Exibição dos Resultados:
- Exibe os dados no console em formato tabular, com as colunas:
  - `FOOD NAME`
  - `SCIENTIFIC NAME`
  - `SUBGROUP`

## Como Executar

### Preparação:
1. Baixe o arquivo `generic_food.csv` e coloque-o na pasta `C:\TEMP`.
2. Certifique-se de que o Python 3.x está instalado no seu sistema.

### Execução:
1. Clone este repositório ou copie o código para um arquivo Python (por exemplo, `main.py`).
2. Execute o script Python:

```bash
python Main.py
```

### Saída Esperada:
- O script exibirá no console os alimentos do grupo "Fruits" no seguinte formato:

| FOOD NAME        | SCIENTIFIC NAME       | SUBGROUP          |
|------------------|-----------------------|-------------------|
| Kiwi             | Actinidia chinensis   | Tropical fruits   |
| Pineapple        | Ananas comosus        | Tropical fruits   |
| Custard apple    | Annona reticulata     | Tropical fruits   |
| ...              | ...                   | ...               |

Dataset: [https://drive.google.com/open?id=1fsyrpTXbJuUcLa0TZKcu0g4aNLnNmiuB&usp=drive_fs](https://drive.google.com/open?id=1fsyrpTXbJuUcLa0TZKcu0g4aNLnNmiuB&usp=drive_fs)
