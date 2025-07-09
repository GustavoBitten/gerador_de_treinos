from classes.ExercicioBase import ExercicioBase

class JoelhoBiSimetrico(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "sumo": [
                "SUNO BARRA",
                "SUNO HALTER"
            ],
            "agachamento": [
                "AGACHAMENTO PASSADA LATERAL",
                "AGACHAMENTO LATERAL",
                "AGACHAMENTO LATERAL DINAMICO",
                "AGACHAMENTO TRILA EXTENSÃO",
                "AGACHAMENTO GILBERT",
                "AGACHAMENTO LEVANDO AS MÃOS À FRENTE",
                "AGACHAMENTO BARRA NAS COSTAS",
                "AGACHAMENTO BARRA NA FRENTE",
                "AGACHAMENTO KTB RACK BILATERAL",
                "AGACHAMENTO OVERHEAD KTB BILATERAL",
                "AGACHAMENTO OVERHEAD BARRA"
            ]
        }

class JoelhoBiAssimetrico(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "AFUNDO": [
                "AFUNDO",
                "AFUNDO HALTER BILATERAL",
                "AFUNDO HALTER UNILATERAL",
                "AFUNDO BARRA NAS COSTAS",
                "AFUNDO BARRA NA FRENTE",
                "AFUNDO OVERHEAD KTB UNILATERAL",
                "AFUNDO OVERHEAD KTB BILATERAL",
                "AFUNDO OVERHEAD BARRA",
                "AFUNDO 1 STEP",
                "AFUNDO 2 STEPS",
                "AFUNDO 1 STEP + HALTER BILATERAL",
                "AFUNDO 1 STEP + HALTER UNILATERAL",
                "AFUNDO 2 STEPS + HALTER BILATERAL",
                "AFUNDO 2 STEPS + HALTER UNILATERAL"
            ],
            "AVANCOS": [
                "AVANÇO",
                "AVANÇO + REVERSO"
            ],
            "BULGARO": [
                "BÚLGARO GOBLET",
                "BÚLGARO + HALTER BILATERAL",
                "BÚLGARO + HALTER UNILATERAL",
                "BÚLGARO + BARRA HEXAGONAL",
                "BÚLGARO + BARRA NAS COSTAS"
            ]
        }


class JoelhoUnilateral(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "joelho_unilateral": [
                "PISTOL",
                "AGACHAMENTO UNILATERAL SENTANDO E LEVANDO DO BANCO",
                "AGACHAMENTO UNILATERAL SENTANDO E LEVANDO DO BANCO LEVANDO O PESO À FRENTE",
                "AGACHAMENTO UNI EM CIMA DO STEP  LEVANDO O PESO À FRENTE",
                "AGACHAMENTO UNI EM CIMA DA CAIXA LEVANDO O PESO À FRENTE",
                "AGACHAMENTO UNI EM CIMA DA CAIXA GOBLET",
                "AGACHAMENTO UNI EM CIMA DA CAIXA KBT RACK",
                "SKATER SQUAT LEVANDO O PESO À FRENTE",
                "BÚLGARO",
                "BÚLGARO GOBLET",
                "BÚLGARO + HALTER BILATERAL",
                "BÚLGARO + HALTER UNILATERAL",
                "BÚLGARO + BARRA HEXAGONAL",
                "BÚLGARO + BARRA NAS COSTAS"
            ]
        }


from classes.ExercicioBase import ExercicioBase

class QuadrilBiSimetrico(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "quadril_bi_simetrico": [
                "TERRA",
                "ELEVAÇÃO/PONTE",
                "TERRA BARRA HEXAGONAL",
                "TERRA BARRA RETA",
                "STIFF",
                "PONTE BANCO",
                "PONTE CHAO",
                "ELEVAÇAO DE QUADRIL MAQUINA",
                "STIFF BARRA",
                "STIFF ASSIMÉTRICO",
                "STIF HALTER BILATERAL"
            ]
        }


class QuadrilUnilateral(ExercicioBase):
    def __init__(self):
        super().__init__()
        self.exercicios = {
            "quadril_unilateral": [
                "AVIÃO",
                "ELEVAÇÃO UNI",
                "TERRA UNI",
                "PONTE UNILATERAL BANCO",
                "PONTE UNILATERAL CHAO",
                "ELEVAÇAO DE QUADRIL UNILATERAL CAIXA",
                "ELEVAÇAO DE QUADRIL UNILATERAL",
                "TERRA UNI HALTER BILATERAL",
                "TERRA UNI HALTER UNILATERAL",
                "TERRA UNI + POLIA UNILATERAL",
                "TERRA UNI + POLIA BILATERAL",
                "TERRA UNI BARRA HEXAGONAL",
                "TERRA UNI BARRA RETA",
                "STIFF HALTER UNILATERAL"
            ]
        }
