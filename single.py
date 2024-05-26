import time
from multiprocessing import Pool


def intensive_computation(n):
    result = 0
    for i in range(n):
        result += i*i
    return result

def single_core():
    n = 10000000
    start_time = time.time()
    result = intensive_computation(n)
    end_time = time.time()
    print(f"Resultado: {result}")
    print(f"Tempo de execução em um único núcleo: {end_time - start_time} segundos")

if __name__ == "__main__":
    single_core()
