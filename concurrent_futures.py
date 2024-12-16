import time
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

DB = {
    12345: ("Ana Clara Silva", 8.5),
    23456: ("Bruno Pereira de Souza", 7.2),
    34567: ("Lindamar Oliveira", 9.1),
    45678: ("Welington Santos", 6.8),
    56789: ("Eduarda Lima Silva", 5.0),
    67890: ("Felipe Costa", 9.9),
    13579: ("Gabriela Almeida", 7.7),
    24680: ("Henrique Pereira de Souza", 8.0),
    11223: ("Isabela Rodrigues", 6.5),
    44556: ("João Fernandes", 9.3)
}

def get_record_by_id(matricula: int):
    time.sleep(3)
    return DB.get(matricula, ("Desconhecido", 0.0))

def get_all_records():
    time.sleep(30)
    return DB

def concurrent_futures():
    matr_list = [12345, 23456, 34567, 45678, 56789]

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(get_record_by_id, m) for m in matr_list]

        concurrent.futures.wait(futures)

        results = [f.result() for f in futures]

        for (nome, nota) in results:
            print(f"Registro obtido: {nome}, Nota: {nota}")

        notas = [r[1] for r in results]
        media = sum(notas) / len(notas)
        print(f"Média das notas das consultas: {media:.2f}")

        future_all = executor.submit(get_all_records)

        single_future = executor.submit(get_record_by_id, 67890)
        single_result = single_future.result()
        print("Consulta enquanto aguarda get_all_records:", single_result)

        cancelled = future_all.cancel()
        print("Tentativa de cancelar get_all_records:", "Sucesso" if cancelled else "Falha")

        if not cancelled:
            print("Aguardando get_all_records terminar...")
            all_records = future_all.result()
            print("Total de registros:", len(all_records))
            
if __name__ == "__main__":
    concurrent_futures()