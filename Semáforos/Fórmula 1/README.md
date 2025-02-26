# Exercício de Semáforos: Simulação de Treino de Fórmula 1

## Descrição

Você foi contratado para automatizar um treino de Fórmula 1. As regras estabelecidas pela direção da prova são simples:
- No máximo 5 carros das 7 escuderias (cada escuderia tem 2 carros diferentes, portanto, 14 carros no total) podem entrar na pista simultaneamente.
- Apenas um carro de cada equipe pode estar na pista ao mesmo tempo. O segundo carro deve ficar à espera, caso um companheiro de equipe já esteja na pista.
- Cada piloto deve dar 3 voltas na pista.
- O tempo de cada volta deverá ser exibido e a volta mais rápida de cada piloto deve ser armazenada para, ao final, exibir o grid de largada, ordenado do menor tempo para o maior.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `Main.py`: Script Python que realiza a simulação do treino de Fórmula 1 utilizando threads e semáforos.

## Funcionalidades

O script `Main.py` realiza as seguintes operações:

1. **Inicialização de Semáforos**:
   - Inicializa semáforos para controlar o acesso à pista e para garantir que apenas um carro de cada equipe esteja na pista ao mesmo tempo.

2. **Simulação de Treino**:
   - Cada carro aguarda sua vez para entrar na pista.
   - Cada carro completa três voltas na pista, com tempos de volta gerados aleatoriamente entre 80 e 120 segundos.
   - O melhor tempo de volta de cada carro é registrado.

3. **Exibição do Grid de Largada**:
   - Ao final da simulação, o programa exibe o grid de largada com base na melhor volta de cada carro.

## Como Executar

1. **Pré-requisitos**:
   - Python 3.x instalado.

2. **Execução**:
   - Navegue até o diretório do exercício.
   - Execute o script `Main.py`:
     ```bash
     python Main.py
     ```