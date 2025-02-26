import os
import subprocess


def parar_nginx():
    print('Verificando se há contêiners Nginx em execução...')
    try:
        listar_nginx = ['docker', 'ps', '-q', '--filter', 'name=nginx']
        nginx_conteiners = subprocess.run(listar_nginx, capture_output=True, text=True).stdout.strip()
        if nginx_conteiners:
            print('Parando e removendo contêineres Nginx...')
            subprocess.run(['docker', 'stop'] + nginx_conteiners.split(),check=True)
            
            subprocess.run(['docker', 'rm'] + nginx_conteiners.split(), check=True)
            
            print('Contêineres Nginx parados e removidos com sucesso!')
        else:
            print('Nenhum contêiner Nginx em execução.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao parar ou remover contêineres Nginx: {e}')
        
def criar_apache_conteiner():
    print('Criando o contêiner Apache 2...')
    comando = [
        'docker', 'run', '-d', '--name', 'Apache2', '-v', '/var/www:/usr/local/apache2/htdocs',\
            '-p', '80:80', '--restart', 'always',\
                'lecolevati/apache-httpd:2.4.63'
    ]
    subprocess.run(comando, check=True)
    print('Contêiner do Apache 2 criado com sucesso!')
    
def criar_pasta_www():
    print('Criando a pasta /var/www...')
    os.makedirs('/var/www', exist_ok=True)
    print('Pasta /var/www cirada com sucesso!')

def criar_index_html():
    print('Criando o arquivo index.html...')
    conteudo_html = """
    <head>
        <body>
            <div>
                <p>
                    <h1>Apache 2 rodando no Docker</h1>
                </p>
            </div>
        </body>
    </head>
    """
    with open('/var/www/index.html', 'w') as arquivo:
        arquivo.write(conteudo_html.strip())
        print('Arquivo index.html criado com sucesso!')
        
def verificar_servidor():
    print('Verificando se o servidor está funcionando...')
    try:
        resultado = subprocess.run(['curl', 'http://localhost'], capture_output=True, text=True)
        if resultado.returncode == 0:
            print('Resposta do servidor: ')
            print(resultado.stdout)
        else:
            print('Erro ao acessar o servidor.')
    except Exception as e:
        print(f'Erro ao verificar o servidor: {e}')
        
def remover_apache_container():
    print("Parando e removendo o contêiner Apache2...")
    try:
        subprocess.run(["docker", "stop", "Apache2"], check=True)
        subprocess.run(["docker", "rm", "Apache2"], check=True)
        print("Contêiner Apache2 parado e removido com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao parar ou remover o contêiner Apache2: {e}")
        
def main():
    try:
        parar_nginx()
        criar_pasta_www()
        criar_index_html()
        criar_apache_conteiner()
        verificar_servidor()
    except subprocess.CalledProcessError as e:
        print(f'Erro durante a execução do comando: {e}')
    except Exception as e:
        print(f'Erro inexperado: {e}')
    finally:
        remover_apache_container()
        
if __name__ == '__main__':
    main()