import csv
import os.path
import subprocess
import sys

def instalar_tabulate():
    try:
        import tabulate
        print(f'Tabulate já está instalado.')
    except ModuleNotFoundError:
        print('Biblioteca "Tabulate" não encontrada. Instalando...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tabulate'])
        
instalar_tabulate()

from tabulate import tabulate

def validar_pasta_e_arquivo(caminho_pasta, nome_arquivo):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    if not os.path.exists(caminho_pasta):
        print(f'A pasta {caminho_pasta} não existe.')
        return False
    if not os.path.isfile(caminho_arquivo):
        print(f'O arquivo {nome_arquivo} não existe na pasta {caminho_pasta}.')
        return False
    return True

def ler_e_filtrar_frutas(caminho_pasta, nome_arquivo):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        dados = []  # Lista para armazenar os dados das frutas

        # Determinar a largura máxima de cada coluna
        largura_food_name = len("FOOD NAME")
        largura_scientific_name = len("SCIENTIFIC NAME")
        largura_sub_group = len("SUB GROUP")

        for linha in leitor_csv:
            if linha['GROUP'] == 'Fruits':
                food_name = linha['FOOD NAME']
                scientific_name = linha['SCIENTIFIC NAME']
                sub_group = linha['SUB GROUP']

                # Atualizar as larguras máximas
                largura_food_name = max(largura_food_name, len(food_name))
                largura_scientific_name = max(largura_scientific_name, len(scientific_name))
                largura_sub_group = max(largura_sub_group, len(sub_group))

                # Adicionar os dados à lista
                dados.append([food_name, scientific_name, sub_group])

        # Formatar o cabeçalho
        cabecalho = (
            "FOOD NAME".ljust(largura_food_name)
            + " | " + "SCIENTIFIC NAME".ljust(largura_scientific_name)
            + " | " + "SUB GROUP".ljust(largura_sub_group)
        )
        print(cabecalho)
        print("-" * (largura_food_name + largura_scientific_name + largura_sub_group + 6))  # 6 para os separadores " | "

        # Formatar e exibir os dados
        for linha in dados:
            linha_formatada = (
                linha[0].ljust(largura_food_name)
                + " | " + linha[1].ljust(largura_scientific_name)
                + " | " + linha[2].ljust(largura_sub_group)
            )
            print(linha_formatada)

def main():
    caminho_pasta = os.path.join(os.path.expanduser('~'), 'Downloads')
    nome_arquivo = 'generic_food.csv'

    if validar_pasta_e_arquivo(caminho_pasta, nome_arquivo):
        ler_e_filtrar_frutas(caminho_pasta, nome_arquivo)

if __name__ == '__main__':
    main()