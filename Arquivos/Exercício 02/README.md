# Análise de Popularidade de Jogos na Steam

## Descrição

Este programa analisa a popularidade dos jogos na plataforma Steam utilizando dados do arquivo `SteamCharts.csv`. O arquivo contém informações sobre a popularidade dos jogos, divididas por ano e mês, com mais de 83 mil registros. As informações de interesse para a análise são o nome do jogo, o ano, o mês e a média de jogadores ativos (`avg`).

## Funcionalidades

O programa possui as seguintes funcionalidades:

1. **Exibir Jogos por Ano, Mês e Média de Jogadores Ativos**:
   - Recebe como parâmetros o ano, o mês e um valor esperado para a média de jogadores ativos.
   - Exibe no console os jogos que correspondem aos parâmetros fornecidos, no formato:
     ```
     Nome do jogo | Média de jogadores ativos
     ```

2. **Filtrar e Salvar Jogos por Ano e Mês**:
   - Recebe como parâmetros o ano, o mês, um caminho de diretório válido e um nome de arquivo válido.
   - Filtra as linhas do arquivo `SteamCharts.csv` de acordo com o ano e o mês fornecidos.
   - Gera um novo arquivo CSV no diretório especificado, com o seguinte formato:
     ```
     nome do jogo ; média dos jogadores ativos
     ```

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `Main.py`: Contém a lógica principal do programa, incluindo a leitura do arquivo CSV, filtragem dos dados e exibição dos resultados.
- `SteamCharts.csv`: Arquivo CSV contendo os dados de popularidade dos jogos na Steam.
- `README.md`: Este arquivo, contendo a descrição do projeto e instruções de uso.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado.
   - Bibliotecas `requests` e `tabulate` instaladas. Caso não estejam instaladas, o programa tentará instalá-las automaticamente.

2. **Execução**:
   - Certifique-se de que o arquivo `SteamCharts.csv` está no diretório `Downloads` do seu usuário.
   - Execute o arquivo `Main.py`:
     ```bash
     python Main.py
     ```

## Exemplo de Uso

### Exibir Jogos por Ano, Mês e Média de Jogadores Ativos

No método `main`, o programa chama a função `filtrar_e_exibir` com os seguintes parâmetros:
```python
filtrar_e_exibir(caminho_arquivo, ano=2018, mes='January', media_esperada=500)