# Exercício de Docker: Compilação e Execução de Código Java

## Descrição

Este exercício demonstra como usar o Docker para compilar e executar um programa Java. O programa solicita ao usuário que insira dois números inteiros e, em seguida, exibe a soma desses números.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `Main.py`: Script Python que automatiza a criação do contêiner Docker, a criação e modificação do arquivo Java, a compilação e a execução do código Java dentro do contêiner.
- `tmp/Teste.java`: Arquivo Java que contém o código a ser compilado e executado.

## Funcionalidades

O script `Main.py` realiza as seguintes operações:

1. **Criar Contêiner Docker**:
   - Cria um contêiner Docker usando a imagem `openjdk:21-jdk` e monta um volume do diretório do host para o contêiner.

2. **Criar Arquivo Java**:
   - Cria um arquivo `Teste.java` com um código Java básico que exibe uma mensagem.

3. **Compilar Código Java**:
   - Compila o arquivo `Teste.java` dentro do contêiner Docker.

4. **Executar Código Java**:
   - Executa a classe `Teste` compilada dentro do contêiner Docker.

5. **Modificar Arquivo Java**:
   - Modifica o arquivo `Teste.java` para solicitar ao usuário que insira dois números inteiros e exibe a soma desses números.

6. **Compilar e Executar Código Java Modificado**:
   - Compila e executa o arquivo `Teste.java` modificado dentro do contêiner Docker.

## Como Executar

1. **Pré-requisitos**:
   - Docker instalado.
   - Python 3.x instalado.

2. **Execução**:
   - Navegue até o diretório do exercício.
   - Execute o script `Main.py`:
     ```bash
     python Main.py
     ```

## Código Java

O arquivo [Teste.java](http://_vscodecontentref_/1) contém o seguinte código:

```java
import java.util.Scanner;

public class Teste {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Informe o 1º número inteiro: ");
        int a = sc.nextInt();
        System.out.print("Informe o 2º número inteiro: ");
        int b = sc.nextInt();
        int res = a + b;
        System.out.println("Soma = " + res);
        sc.close();
    }
}