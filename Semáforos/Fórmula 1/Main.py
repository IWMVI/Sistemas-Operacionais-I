import random
import threading
import time

NUM_EQUIPES = 7
CARROS_POR_EQUIPE = 2
MAX_CARROS_PISTA = 5
VOLTAS_POR_PILOTO = 3

sem_pista = threading.Semaphore(MAX_CARROS_PISTA)
sem_equipes = [threading.Semaphore(1) for _ in range(NUM_EQUIPES)]

melhores_voltas = {}

def carro_na_pista(equipe, carro):
    nome_piloto = f'Equipe {equipe + 1} - Carro {carro + 1}'
    print(f'{nome_piloto} está aguardando para entrar na pista.')
    
    with sem_equipes[equipe]:
        with sem_pista:
            print(f'{nome_piloto} entrou na pista.')
            tempos_voltas = []
            
            for volta in range(VOLTAS_POR_PILOTO):
                tempo_volta = random.uniform(80.0, 120.0)
                tempos_voltas.append(tempo_volta)
                print(f'{nome_piloto} completou a volta {volta + 1} em {tempo_volta:.2f} segundos.')
                time.sleep(1)
            
            melhor_volta = min(tempos_voltas)
            melhores_voltas[nome_piloto] = melhor_volta
            
            print(f'{nome_piloto} saiu da pista. Melhor volta: {melhor_volta:.2f} segundos')
            
def main():
    print('Iniciando.')
    threads = []
    
    for equipe in range(NUM_EQUIPES):
        for carro in range(CARROS_POR_EQUIPE):
            thread = threading.Thread(target=carro_na_pista, args=(equipe, carro))
            threads.append(thread)
            thread.start()
            
    for thread in threads:
        thread.join()
        
    print(f'\nGrid de Largada:')
    grid_ordenado = sorted(melhores_voltas.items(), key=lambda x: x[1])
    for posicao, (piloto, tempo) in enumerate(grid_ordenado, start= 1):
        print(f'{posicao}º lugar: {piloto} - Melhor volta: {tempo:.2f} segundos')
        
if __name__ == '__main__':
    main()