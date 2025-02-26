import subprocess
import os

IMAGE_NAME = 'openjdk:21-jdk'
HOST_DIR = 'D:/Sistemas Operacionais I/Docker/Exercício 02/tmp'
CONTAINER_DIR = '/tmp/java'

def criar_container():
    print('Criando o contêiner jdk21...')
    comando = [
        'docker', 'run', '-d', '--name', 'jdk21', '-v', f'{HOST_DIR}:{CONTAINER_DIR}', IMAGE_NAME, 'tail', '-f', '/dev/null'
    ]
    subprocess.run(comando, check=True)
    print('Contêiner criado com sucesso.')

def criar_arquivo_java():
    print('Criando o arquivo Teste.java...')
    codigo_java = """
    public class Teste {
        public static void main(String[] args){
            System.out.println("Nome: | RA: ");
        }
    }
    """
    os.makedirs(HOST_DIR, exist_ok=True)
    with open(os.path.join(HOST_DIR, 'Teste.java'), 'w') as arquivo:
        arquivo.write(codigo_java.strip())
        print(f'Arquivo Teste.java criado em {HOST_DIR}.')

def compilar_java():
    print('Compilando Teste.java no contêiner...')
    comando = [
        'docker', 'exec', '-it', 'jdk21', 'javac', '-d', f'{CONTAINER_DIR}/bin', f'{CONTAINER_DIR}/Teste.java'
    ]
    subprocess.run(comando, check=True)
    print('Arquivo Teste.java compilado com sucesso!')

def executar_java():
    print('Executando a classe Teste...')
    comando = [
        'docker', 'exec', '-it', 'jdk21', 'java', '-classpath', f'{CONTAINER_DIR}/bin', 'Teste'
    ]
    subprocess.run(comando, check=True)

def modificar_arquivo_java():
    print('Modificando o arquivo Teste.java...')
    codigo_java = """
    import java.util.Scanner;
    
    public class Teste {
        public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            System.out.print("Informe o 1 numero inteiro: ");
            int a = sc.nextInt();
            System.out.print("Informe o 2 numero inteiro: ");
            int b = sc.nextInt();
            int res = a + b;
            System.out.println("Soma = " + res);
            sc.close();
        }
    }
    """
    with open(os.path.join(HOST_DIR, 'Teste.java'), 'w') as arquivo:
        arquivo.write(codigo_java.strip())
    
    print('Arquivo Teste.java modificado com sucesso!')

def main():
    try:
        criar_container()
        criar_arquivo_java()
        compilar_java()
        executar_java()
        modificar_arquivo_java()
        compilar_java()
        executar_java()
    except subprocess.CalledProcessError as e:
        print(f'Erro durante a execução do comando: {e}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        print('Parando e removendo o contêiner...')
        subprocess.run(['docker', 'stop', 'jdk21'], check=True)
        subprocess.run(['docker', 'rm', 'jdk21'], check=True)
        print('Contêiner removido com sucesso!')

if __name__ == '__main__':
    main()