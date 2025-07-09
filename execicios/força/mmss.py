import sys
import os



from classes.ExercicioBase import ExercicioBase

class EmpurrarHorizontal(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "SUPINO RETO": [
                "SUPINO HALTER ALTERNADO",
                "SUPINO COM BARRA",
                "SUPINO UNI COM HALTER (CARGA ALTA)",
                "SUPINO BILATERAL COM HALTER (CARGA ALTA)"
            ],
            "FLEXÃO DE BRAÇO": [
                "FLEXÃO DE BRAÇO COMPLETA",
                "FLEXÃO FECHADA",
                "FLEXÃO DE BRAÇO COMPLETA + RESISTÊNCIA DO ELÁSTICO",
                "FLEXÃO DE BRAÇO COM PÉ NO BANCO",
                "FLEXÃO DE BRAÇO APOIADO NA ALÇA DO KTB",
                "FLEXÃO DE BRAÇO APOIADO NA ALÇA DO KTB + PÉ NO BANCO"
            ],
            "SUPINO INCLINADO": [
                "SUPINO INCLINADO UNILATERAL COM HALTER",
                "SUPINO INCLINADO BILATERAL COM HALTER",
                "SUPINO INCLINADO COM BARRA"
            ],
            "CRUCIFIXO": [
                "CRUCIFIXO COM HALTER",
                "CRUCIFIXO maquiina"
            ]
        }

if __name__ == "__main__":
    emp = EmpurrarHorizontal()
    print(emp.selecionar_aleatorio())


from classes.ExercicioBase import ExercicioBase

class EmpurrarVertical(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "PRESS": [
                "PRESS UNILATERAL DE PÉ COM KTB",
                "PRESS UNILATERAL SPLIT COM KTB",
                "PRESS UNILATERAL SENTADO COM KTB",
                "PRESS BILATERAL SEMI-AJOELHADO COM KTB",
                "PRESS BILATERAL AJOELHADO COM KTB",
                "PRESS BILATERAL DE PÉ COM KTB",
                "PRESS BILATERAL SPLIT COM KTB",
                "PRESS BILATERAL SENTADO COM KTB",
                "PRESS SEMI-AJOELHADO COM BARRA",
                "PRESS AJOELHADO COM BARRA",
                "PRESS DE PÉ COM BARRA",
                "PRESS SPLIT COM BARRA",
                "PRESS SENTADO COM BARRA",
                "PRESS LANDMINE UNILATERAL SEMI-AJOELHADO",
                "PRESS LANDMINE UNILATERAL AJOELHADO",
                "PRESS LANDMINE UNILATERAL DE PÉ",
                "PRESS LANDMINE UNILATERAL SPLIT",
                "PRESS LANDMINE UNILATERAL BASE UNIPODAL",
                "PRESS LANDMINE BILATERAL SEMI-AJOELHADO",
                "PRESS LANDMINE BILATERAL AJOELHADO",
                "PRESS LANDMINE BILATERAL DE PÉ",
                "PRESS LANDMINE BILATERAL SPLIT",
                "PRESS LANDMINE BILATERAL BASE UNIPODAL"
            ],
            "OMBRO LATERAL": [
                "OMBRO LATERAL Cross",
                "OMBRO LATERAL halter"
            ],
            "OMBRO FRONTAL": [
                "OMBRO FRONTAL CROSS",
                "OMBRO FRONTAL Anilha",
                "OMBRO FRONTAL halter"
            ],
            "PARALELA": [
                "PARALELA"
            ]
        }

if __name__ == "__main__":
    emp = EmpurrarVertical()
    print(emp.selecionar_aleatorio())

    import sys
import os



from classes.ExercicioBase import ExercicioBase

class PuxarHorizontal(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "REMADA CURVADA": [
                "REMADA CURVADA",
                "REMADA CURVADA APOIO NO BANCO  HALTER",
                "REMADA CURVADA SEM APOIO 1 HALTER",
                "REMADA CURVADA SEM APOIO 2 HALTERES",
                "REMADA CURVADA BARRA Supinada",
                "REMADA CURVADA BARRA Pronada"
            ],
            "REMADA MAQUINA": [
                "REMADA MAQUINA"
            ],
            "BARRA AUSTRALIANA": [
                "BARRA AUSTRALIANA"
            ],
            "SERROTE": [
                "SERROTE"
            ],
            "FACEPULL": [
                "FACEPULL",
                "FACEPULL DE PÉ",
                "FACEPULL AJOELHADO",
                "FACEPULL SEMIAJOELHADO",
                "FACEPULL SENTADO"
            ]
        }

if __name__ == "__main__":
    pux = PuxarHorizontal()
    print(pux.selecionar_aleatorio())


    import sys
import os



from classes.ExercicioBase import ExercicioBase

class PuxarVertical(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "BARRA FIXA": [
                "BARRA FIXA",
                "BARRA FIXA COMPLETA"
            ],
            "PUXADA NA POLIA": [
                "PUXADA NA POLIA UNILATERAL SENTADO",
                "PUXADA NA POLIA UNILATERAL AJOLEHADO",
                "PUXADA NA POLIA BILATERAL AJOELHADO",
                "PUXADA NA POLIA UNILATERAL DE PÉ",
                "PUXADA NA POLIA BILATERAL DE PÉ"
            ]
        }

if __name__ == "__main__":
    pux = PuxarVertical()
    print(pux.selecionar_aleatorio())

