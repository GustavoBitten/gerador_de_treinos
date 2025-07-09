import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from classes.ExercicioBase import ExercicioBase
class MobilidadeTornozelo(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "Dorsiflexao": [
                "Arqueiro frontal",
                "Arqueiro lateral",
                "Arqueiro com calço",
                "Arqueiro na caixa",
                "Arqueiro com resistência",
                "Tornozelo parede",
                "Cocoras alternada",
                "Arqueiro com KTB",
                "Dorsi com rotação",
            ],
            "Flexao plantar": [
                "Mobilidade de flexão plantar"
            ]
        }


class MobilidadeQuadril(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "Mobilidade de quadril": [
                "Escorpião invertido",
                "Escorpião invertido alternado",
                "Escorpião",
                "Escorpião alternado"
                "Elevação da perna estendida",
                "Suástica deitado",
                "Rotação de quadril",
                "Rotação bilateral",
                "Quadril 4 apoios",
                "Quadril rotacional",
                "90/90",
                "Quadril com caminhada",
                "Quadril 4 apoios",
                "Quadril 4 apoios alternada",
                "Dissociação de quadril"
            ]
        }

class MobilidadeToracica(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "Maior mobilidade do mundo": [
                "Maior mobilidade do mundo",
                "Maior mobilidade do mundo alternado",
            ],
            "Torácica rotacional": [
                "Torácica rolo",
                "Torácica rotacional alternando",
                "Torácica 3 apoios",
                "Gato arrepiado",
                "Torácica deitado",
                "Torácica bastão rotação unilateral",
                "Torácica bastão rotação alternado"
            ],
        }

class MobilidadeOmbro(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "Abertura de ombro": [
                "Abertura de ombro caixote",
                "Abertura de ombro chão",
                "Abertura de ombro parede",
                "Abertura de ombro com bastão",
            ],
            "Rotação de ombro": [
                "Rotação de ombro com bastão",
                "Rotação de ombro com KTB",
                "Rotação de ombro nas costas",
            ],
            "Extensão de ombro": [
                "Extensão de ombro com bastão",
                "Extensão de ombro parede",
                "Extensão de ombro chão",
            ],
        }
