import sys
import os

# Adiciona o diretório raiz do projeto ao Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from classes.ExercicioBase import ExercicioBase

class AntiHiperextensao(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "PRANCHA": [
                "PRANCHA VENTRAL",
                "PRACHA ALTA",
                "PRANCHA VENTRAL COM AUMENTO NO BRAÇO DE ALAVANCA",
                "PRANCHA ALTA COM AUMENTO NO BRAÇO DE ALAVANCA",
                "PRANCHA VENTRAL NA BOLA",
                "PRANCHA NA BOLA VAI FRENTE E VOLTA",
                "PRANCHA VENTRAL NA BOLA AUMENTO NO BRAÇO DE ALAVANCA",
                "PRANCHA ALTA NA BOLA",
                "PRANCHA ALTA NA BOLA VAI A FRENTE E VOLTA",
                "PRANCHA ALTA NA BOLA AUMENTO NO BRAÇO DE ALAVANCA",
                "PRANCHA VENTRAL SLIDE",
                "PRANCHA ALTA SLIDE",
                "PRANCHA ALTA NO TRX"
            ],
            "RODINHA": [
                "ABDOMINAL RODINHA JOELHO NO CHÃO AUXILIO DO ELÁSTICO",
                "ABDOMINAL RODINHA RESISTÊNCIA DO ELÁSTICO",
                "ABDOMINAL RODINHA POSIÇÃO DE URSO COM AUXILIO DO ELÁSTICO",
                "ABDOMINAL RODINHA POSIÇÃO DE URSO",
                "ABDOMINAL RODINHA POSIÇÃO DE URSO COM RESISTÊNCIA DO ELÁSTICO"
            ]
        }


class AntiRotacao(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "PRANCHA_ANTI_ROTACAO": [
                "PRANCHA ALTA TOCANDO OMBRO",
                "PRANCHA ALTA TOCANDO OMBRO EM ISOMETRIA",
                "PRANCHA ALTA PUXANDO KTB",
                "PRANCHA ALTA PUXANDO ELÁSTICO",
                "PRANCHA ISOMÉTRICA 3 APOIOS",
                "PRANCHA ALTA 3 APOIOS",
                "PRANCHA PUXANDO KTB TIRANDO O PÉ DO CHÃO",
                "PRANCHA NA BOLA 3 APOIOS",
                "PRANCHA ALTA NA BOLA FAZENDO FLEXÃO DE QUADRIL",
                "PRANCHA BAIXA EMPURRANDO KTB PARA FRENTE"
            ],
            "PALLOF_PRESS": [
                "PALLOF PRESS COM ELÁSTICO POSIÇÃO AJOELHADO",
                "PALLOF PRESS COM ELÁSTICO POSIÇÃO SEMI AJOELHADO",
                "PALLOF PRESS COM ELÁSTICO POSIÇÃO EM PÉ",
                "PALLOF PRESS COM ELÁSTICO POSIÇÃO DE SPLIT",
                "PALLOF PRESS COM ELÁSTICO POSIÇÃO UNI PODAL",
                "PALLOF PRESS EM PÉ COM ANILHA NO ELÁSTICO"
            ]
        }


class AntiFlexaoLateral(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "PRANCHA_LATERAL": [
                "PRANCHA LATERAL"
            ],
            "ELASTICO_ACIMA_CABECA": [
                "AJOELHADO COM ELÁSTICO A CIMA DA CABEÇA",
                "SEMI AJOELHADO COM ELÁSTICO A CIMA DA CABEÇA",
                "EM PÉ COM ELÁSTICO PARA CIMA DA CABEÇA",
                "EM POSIÇÃO DE SPLIT COM ELÁSTICO PARA CIMA DA CABEÇA",
                "UNI PODAL COM ELÁSTICO PARA CIMA DA CABEÇA"
            ],
            "FAZENDEIRO": [
                "FAZENDEIRO ISOMÉTRICO COM HALTER",
                "CAMINHADA DO FAZENDEIRO COM HALTER UNILATERAL",
                "CAMINHADA DO FAZENDEIRO COM HALTER BILATERAL",
                "CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E HALTER UNILATERAL",
                "CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E HALTER BILATERAL",
                "FAZENDEIRO ISOMÉTRICO COM KTB",
                "CAMINHADA DO FAZENDEIRO COM KTB UNILATERAL",
                "CAMINHADA DO FAZENDEIRO COM KTB BILATERAL",
                "CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E KTB UNILATERAL",
                "CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E KTB BILATERAL",
                "CAMINHADA DO FAZENDEIRO COM 1KTB A CIMA DA CABEÇA",
                "CAMINHADA DO FAZENDEIRO COM 2KTB A CIMA DA CABEÇA",
                "FAZENDEIRO ISOMÉTRICO COM BARRA NAS COSTAS",
                "CAMINHADA DO FAZENDEIRO COM BARRA NAS COSTAS",
                "CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E BARRA NAS COSTAS",
                "CAMINHADA DO FAZENDEIRO COM BARRA A CIMA DA CABEÇA"
            ]
        }


class Rotacao(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "CHOP": [
                "CHOP AJOELHADO NO CROSS",
                "CHOP SEMI-AJOELHADO NO CROSS",
                "CHOP EM PÉ NO CROSS",
                "CHOP SPLIT NO CROSS",
                "CHOP UNILATERAL NO CROSS"
            ],
            "LIFT": [
                "LIFT AJOELHADO NO CROSS",
                "LIFT SEMI-AJOELHADO NO CROSS",
                "LIFT EM PÉ NO CROSS",
                "LIFT SPLIT NO CROSS",
                "LIFT UNILATERAL NO CROSS"
            ]
        }


if __name__ == "__main__":
    anti_hip = AntiHiperextensao()
    anti_rot = AntiRotacao()
    anti_flex = AntiFlexaoLateral()
    rotacao = Rotacao()
    
    print("Anti Hiperextensão:", anti_hip.selecionar_aleatorio())
    print("Anti Rotação:", anti_rot.selecionar_aleatorio())
    print("Anti Flexão Lateral:", anti_flex.selecionar_aleatorio())
    print("Rotação:", rotacao.selecionar_aleatorio())


