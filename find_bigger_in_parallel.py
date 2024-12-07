import numpy as np
from multiprocessing import Pool
from vector import vector_by_scalar

def totalize_vector(vector, scalar):
    """Totaliza o vetor resultante da multiplicação."""
    result_vector = vector_by_scalar(vector, scalar)
    total_sum = np.sum(result_vector)
    return total_sum, scalar

def biggest_sums(results):
    max_value = max(results, key=lambda x: x[0])[0]
    return [(total if total == max_value else 0.0 + scalar) for total, scalar in results]

if __name__ == "__main__":

    vector = np.random.uniform(1, 100, size=1000)
    scalars = [2, 3, 4, 5, 6, 7, 8, 9]


    with Pool(8) as pool:
        results = pool.starmap(totalize_vector, [(vector, scalar) for scalar in scalars])

    final_results = biggest_sums(results)

    for scalar, result in zip(scalars, final_results):
        print(f"Escalar: {scalar}, Resultado: {result}")

