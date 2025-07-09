import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from classes.ExercicioBase import ExercicioBase

class FootCore(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "footcore": [
                "STEP DUPLO",
                "PISTOL STEP DUPLO",
                "TROCA DE KTB STEP DUPLO",
                "STEP SIMPLES",
                "TROCA DE KTB AFUNDO",
                "ISOMÉTRICO EMPURRAR",
                "PISTO EMPURRAR",
                "GARRA MINI BAND",
                "PANTU PAREDE",
                "PAREDE ISO"
            ]
        }


if __name__ == "__main__":
    foot = FootCore()
    print(foot.selecionar_aleatorio())