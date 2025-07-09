import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
project_root = '/home/maleguga/prj-personal/gerador_de_treinos'
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from classes.ExercicioBase import ExercicioBase

class Pliometria(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "Jump": [
                "Jump Linear-Vertical SCM",
                "Jump Linear-Vertical CMV",
                "Jump Linear-Vertical CD",
                "Jump Linear-Vertical C",
                "Jump Linear-Vertical SP",
                "Jump Linear-Horizontal SCM",
                "Jump Linear-Horizontal CMV",
                "Jump Linear-Horizontal CD",
                "Jump Linear-Horizontal C",
                "Jump Linear-Horizontal SP",
                "Jump Lateral-Vertical SCM",
                "Jump Lateral-Vertical CMV",
                "Jump Lateral-Vertical CD",
                "Jump Lateral-Vertical C",
                "Jump Lateral-Vertical SP",
                "Jump Lateral-Horizontal SCM",
                "Jump Lateral-Horizontal CMV",
                "Jump Lateral-Horizontal CD",
                "Jump Lateral-Horizontal C",
                "Jump Lateral-Horizontal SP",
                "Jump Rotacional-Vertical SCM",
                "Jump Rotacional-Vertical CMV",
                "Jump Rotacional-Vertical CD",
                "Jump Rotacional-Vertical C",
                "Jump Rotacional-Vertical SP",
                "Jump Rotacional-Horizontal SCM",
                "Jump Rotacional-Horizontal CMV",
                "Jump Rotacional-Horizontal CD",
                "Jump Rotacional-Horizontal C",
                "Jump Rotacional-Horizontal SP",
            ],
            "Bound": [
                "Bound Linear-Vertical SCM",
                "Bound Linear-Vertical CMV",
                "Bound Linear-Vertical CD",
                "Bound Linear-Vertical C",
                "Bound Linear-Vertical SP",
                "Bound Linear-Horizontal SCM",
                "Bound Linear-Horizontal CMV",
                "Bound Linear-Horizontal CD",
                "Bound Linear-Horizontal C",
                "Bound Linear-Horizontal SP",
                "Bound Lateral-Vertical SCM",
                "Bound Lateral-Vertical CMV",
                "Bound Lateral-Vertical CD",
                "Bound Lateral-Vertical C",
                "Bound Lateral-Vertical SP",
                "Bound Lateral-Horizontal SCM",
                "Bound Lateral-Horizontal CMV",
                "Bound Lateral-Horizontal CD",
                "Bound Lateral-Horizontal C",
                "Bound Lateral-Horizontal SP",
                "Bound Rotacional-Vertical SCM",
                "Bound Rotacional-Vertical CMV",
                "Bound Rotacional-Vertical CD",
                "Bound Rotacional-Vertical C",
                "Bound Rotacional-Vertical SP",
                "Bound Rotacional-Horizontal SCM",
                "Bound Rotacional-Horizontal CMV",
                "Bound Rotacional-Horizontal CD",
                "Bound Rotacional-Horizontal C",
                "Bound Rotacional-Horizontal SP",
            ],
            "Hop": [
                "Hop Linear-Vertical SCM",
                "Hop Linear-Vertical CMV",
                "Hop Linear-Vertical CD",
                "Hop Linear-Vertical C",
                "Hop Linear-Vertical SP",
                "Hop Linear-Horizontal SCM",
                "Hop Linear-Horizontal CMV",
                "Hop Linear-Horizontal CD",
                "Hop Linear-Horizontal C",
                "Hop Linear-Horizontal SP",
                "Hop Lateral-Vertical SCM",
                "Hop Lateral-Vertical CMV",
                "Hop Lateral-Vertical CD",
                "Hop Lateral-Vertical C",
                "Hop Lateral-Vertical SP",
                "Hop Lateral-Horizontal SCM",
                "Hop Lateral-Horizontal CMV",
                "Hop Lateral-Horizontal CD",
                "Hop Lateral-Horizontal C",
                "Hop Lateral-Horizontal SP",
                "Hop Rotacional-Vertical SCM",
                "Hop Rotacional-Vertical CMV",
                "Hop Rotacional-Vertical CD",
                "Hop Rotacional-Vertical C",
                "Hop Rotacional-Vertical SP",
                "Hop Rotacional-Horizontal SCM",
                "Hop Rotacional-Horizontal CMV",
                "Hop Rotacional-Horizontal CD",
                "Hop Rotacional-Horizontal C",
                "Hop Rotacional-Horizontal SP"
            ]
        }


if __name__ == "__main__":
    plio = Pliometria()
    print(plio.selecionar_aleatorio())
