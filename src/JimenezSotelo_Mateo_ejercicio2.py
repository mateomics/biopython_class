import random

class gen():
    # Constructor
    def __init__(self, inicio, fin, secuencia, organismo, funcion='desconocida') -> None:
        self.longitud = fin - inicio + 1 # Por slicing en python
        self.inicio = inicio
        self.fin = fin
        self.secuencia = secuencia.strip().upper() # todo en mayúsculas
        self.organismo = organismo
        self.funcion = funcion

    def codones(self, marco=1) -> list: # 1-3. 1 por default
        return [self.secuencia[i:i+3] for i in range(marco - 1, len(self.secuencia)-2, 3)] # -2 para que siempre regrese codones completos

    def codon_paro(self, codones_seq) -> bool:
        return any(codon in (codones_paro := ['UGA', 'UAG', 'UAA', 'TGA', 'TAG', 'TAA']) for codon in codones_seq) # si coinciden con alguno, sea DNA o RNA
    
    def contenido_gc(self) -> float:
        return 100 * (self.secuencia.count('G') + self.secuencia.count('C')) / len(self.secuencia) # En porcentaje
    
gen_prueba = gen(322, 456, ''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(34)), 'Humano')

codones_seq = gen_prueba.codones(2)
print(f'Secuencia del gen: {gen_prueba.secuencia}\nCodones: {codones_seq}') # Segundo marco de lectura
print(f'Codón de paro: {gen_prueba.codon_paro(codones_seq)}\nContendo de GC: {gen_prueba.contenido_gc()}%')