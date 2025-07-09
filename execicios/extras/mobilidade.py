import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
project_root = '/home/maleguga/prj-personal/gerador_de_treinos'
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from classes.ExercicioBase import ExercicioBase

# Arquivo para exercícios de mobilidade - aguardando conteúdo
class MobilidadeTo(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {

        }


Tornozero

Aru

if __name__ == "__main__":
    mob = Mobilidade()
    print(mob.selecionar_aleatorio())
