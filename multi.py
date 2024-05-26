from mpi4py import MPI
import time

def intensive_computation(n):
    result = 0
    for i in range(n):
        result += i*i
    return result

def distributed():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    n = 10000000  
    n_per_process = n // size

    start_time = MPI.Wtime()
    local_sum = intensive_computation(n_per_process)
    global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)
    end_time = MPI.Wtime()

    if rank == 0:
        print(f"Resultado: {global_sum}")
        print(f"Tempo de execução distribuído: {end_time - start_time} segundos")

if __name__ == "__main__":
    distributed()
