import csv
import os
import subprocess
import sys
import requests
from tabulate import tabulate

def instalar_tabulate():
    try:
        import tabulate
        print(f'Tabulate já está instalado.')
    except ModuleNotFoundError:
        print(f'Biblioteca "Tabulate" não encontrada. Instalando...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tabulate'])

def instalar_requests():
    try:
        import requests
        print(f'Requests já está instalado.')
    except ModuleNotFoundError:
        print(f'Biblioteca "Requests" não encontrada. Instalando...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])

instalar_tabulate()
instalar_requests()

def baixar_arquivo_csv(url, caminho_saida):
    try:
        print(f'Baixando o arquivo de {url}...')
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(caminho_saida, 'wb') as arquivo:
                for chunk in response.iter_content(chunk_size=8192):
                    arquivo.write(chunk)
            print(f'Arquivo salvo em {caminho_saida}')
            return True
        else:
            print(f'Erro ao baixar o arquivo. Código de status: {response.status_code}')
            return False
    except Exception as e:
        print(f'Erro durante o download: {e}')
        return False

def validar_pasta_e_arquivo(caminho_pasta, nome_arquivo):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    if not os.path.exists(caminho_pasta):
        print(f'A pasta {caminho_pasta} não existe.')
        return False
    if not os.path.isfile(caminho_arquivo):
        print(f'O arquivo {nome_arquivo} não existe na pasta: {caminho_pasta}.')
        # Tenta baixar o arquivo
        url = "https://drive.google.com/uc?export=download&id=1QT29x3lMj4_j9Ca9XRyjWzuUjtTjNi58"
        if not baixar_arquivo_csv(url, caminho_arquivo):
            return False
        
    return True

def ler_cabecalhos_csv(caminho_arquivo):
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            return leitor_csv.fieldnames
    except UnicodeDecodeError:
        # Se UTF-8 falhar, tenta ISO-8859-1
        with open(caminho_arquivo, mode='r', encoding='ISO-8859-1') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            return leitor_csv.fieldnames

def filtrar_e_exibir(caminho_arquivo, ano, mes, media_esperada):
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            dados = []
            for linha in leitor_csv:
                try:
                    if (int(linha['year']) == ano and
                        (linha['month']) == mes and
                        float(linha['avg']) >= media_esperada):
                        dados.append([linha['gamename'], linha['avg']])
                except ValueError:
                    continue
                
            print(tabulate(dados, headers=['Nome do jogo', 'Média de jogadores ativos'], tablefmt='pretty'))
    except UnicodeDecodeError:
        # Se UTF-8 falhar, tenta ISO-8859-1
        with open(caminho_arquivo, mode='r', encoding='ISO-8859-1') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            dados = []
            for linha in leitor_csv:
                try:
                    if (int(linha['year']) == ano and
                        (linha['month']) == mes and
                        float(linha['avg']) >= media_esperada):
                        dados.append([linha['gamename'], linha['avg']])
                except ValueError:
                    continue
                
            print(tabulate(dados, headers=['Nome do jogo', 'Média de jogadores ativos'], tablefmt='pretty'))

def filtrar_e_salvar(caminho_arquivo, ano, mes, caminho_diretorio, nome_arquivo_saida):
    caminho_saida = os.path.join(caminho_diretorio, nome_arquivo_saida)
    
    if not os.path.exists(caminho_diretorio):
        print(f'O diretório {caminho_diretorio} não existe.')
        return
    
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo,\
            open(caminho_saida, mode='w', newline='', encoding='utf-8') as saida:
            
            leitor_csv = csv.DictReader(arquivo)
            escritor_csv = csv.writer(saida, delimiter=';')
            escritor_csv.writerow(['Nome do jogo', 'Média de Jogadores Ativos'])
            
            for linha in leitor_csv:
                if (int(linha['year']) == ano and
                    (linha['month']) == mes):
                    escritor_csv.writerow([linha['gamename'], linha['avg']])
            
            print(f'Arquivo salvo em: {caminho_saida}')
    except UnicodeDecodeError:
        # Se UTF-8 falhar, tenta ISO-8859-1
        with open(caminho_arquivo, mode='r', encoding='ISO-8859-1') as arquivo,\
            open(caminho_saida, mode='w', newline='', encoding='utf-8') as saida:
            
            leitor_csv = csv.DictReader(arquivo)
            escritor_csv = csv.writer(saida, delimiter=';')
            escritor_csv.writerow(['Nome do jogo', 'Média de Jogadores Ativos'])
            
            for linha in leitor_csv:
                if (int(linha['year']) == ano and
                    (linha['month']) == mes):
                    escritor_csv.writerow([linha['gamename'], linha['avg']])
            
            print(f'Arquivo salvo em: {caminho_saida}')
        
def main():
    caminho_pasta = os.path.join(os.path.expanduser('~'), 'Downloads')
    nome_arquivo = 'SteamCharts.csv'
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    
    if not validar_pasta_e_arquivo(caminho_pasta, nome_arquivo):
        return

    # Exemplo de uso do método filtrar_e_exibir
    filtrar_e_exibir(caminho_arquivo, ano=2018, mes='January', media_esperada=500)

    filtrar_e_salvar(caminho_arquivo, ano=2022, mes='January', caminho_diretorio=caminho_pasta, nome_arquivo_saida='jogos_2022_12.csv')

if __name__ == '__main__':
    main()