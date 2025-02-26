# Exercício de Docker: Configuração de Servidor Apache

## Descrição

Este exercício demonstra como usar o Docker para configurar e executar um servidor Apache. O script Python automatiza a criação de um contêiner Docker com Apache, cria um arquivo HTML básico e verifica se o servidor está funcionando corretamente.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `Main.py`: Script Python que automatiza a criação do contêiner Docker, a criação do arquivo HTML, a verificação do servidor e a remoção do contêiner.

## Funcionalidades

O script `Main.py` realiza as seguintes operações:

1. **Parar Contêineres Nginx**:

   - Verifica se há contêineres Nginx em execução e os para e remove, se necessário.

2. **Criar Pasta para Arquivos Web**:

   - Cria a pasta `/var/www` no host para armazenar os arquivos HTML.

3. **Criar Arquivo HTML**:

   - Cria um arquivo `index.html` com conteúdo básico.

4. **Criar Contêiner Apache**:

   - Cria um contêiner Docker usando a imagem `lecolevati/apache-httpd:2.4.63` e monta a pasta `/var/www` do host no contêiner.

5. **Verificar Servidor**:

   - Verifica se o servidor Apache está funcionando corretamente acessando `http://localhost`.

6. **Remover Contêiner Apache**:
   - Para e remove o contêiner Apache após a execução.

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
