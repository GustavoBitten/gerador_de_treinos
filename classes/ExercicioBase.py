import random

class ExercicioBase:
    def selecionar_aleatorio(self, grupo=None):
        if grupo is None:
            if not self.exercicios:
                return None
            grupo = random.choice(list(self.exercicios.keys()))
        lista = self.exercicios.get(grupo, [])
        if not lista:
            return None
        idx = random.randint(0, len(lista) - 1)
        return lista[idx]
