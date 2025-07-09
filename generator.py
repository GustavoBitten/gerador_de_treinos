from typing import List
import random

from execicios.força.mmii import JoelhoBiAssimetrico, JoelhoBiSimetrico, JoelhoUnilateral, QuadrilBiSimetrico, QuadrilUnilateral
from execicios.força.mmss import EmpurrarHorizontal, EmpurrarVertical, PuxarHorizontal, PuxarVertical
from execicios.força.core import AntiHiperextensao, AntiRotacao, AntiFlexaoLateral, Rotacao
from execicios.extras.pliometria import Pliometria
from execicios.extras.outros import FootCore

# Instanciar as classes
empurrar_horizontal = EmpurrarHorizontal()
empurrar_vertical = EmpurrarVertical()
puxar_horizontal = PuxarHorizontal()
puxar_vertical = PuxarVertical()

joelho_bi_assimetrico = JoelhoBiAssimetrico()
joelho_bi_simetrico = JoelhoBiSimetrico()
joelho_unilateral = JoelhoUnilateral()
quadril_bi_simetrico = QuadrilBiSimetrico()
quadril_unilateral = QuadrilUnilateral()

anti_hiperextensao = AntiHiperextensao()
anti_rotacao = AntiRotacao()
anti_flexao_lateral = AntiFlexaoLateral()
rotacao = Rotacao()
pliometria = Pliometria()
footcore = FootCore()

def gerar_exercicios() -> List[str]:
    mobilidade: List[str] = [

    ]

    random.shuffle(treino_a)
    print("Treino A:", treino_a)
    treino_a: List[str] = [
        empurrar_horizontal.selecionar_aleatorio(),
        empurrar_horizontal.selecionar_aleatorio(),
        empurrar_vertical.selecionar_aleatorio(),
        empurrar_vertical.selecionar_aleatorio(),
        puxar_horizontal.selecionar_aleatorio(),
        puxar_vertical.selecionar_aleatorio(),
        anti_hiperextensao.selecionar_aleatorio(),
        anti_rotacao.selecionar_aleatorio()
    ]
    random.shuffle(treino_a)
    print("Treino A:", treino_a)

    treino_b: List[str] = [
        joelho_bi_assimetrico.selecionar_aleatorio(),
        joelho_bi_simetrico.selecionar_aleatorio(),
        joelho_unilateral.selecionar_aleatorio(),
        quadril_bi_simetrico.selecionar_aleatorio(),
        quadril_unilateral.selecionar_aleatorio(),
        anti_flexao_lateral.selecionar_aleatorio(),
        rotacao.selecionar_aleatorio(),
        pliometria.selecionar_aleatorio(),
        footcore.selecionar_aleatorio()
    ]
    random.shuffle(treino_b)
    print("Treino B:", treino_b)



if __name__ == "__main__":
    gerar_exercicios()
