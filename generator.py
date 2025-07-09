from typing import List
import random
from datetime import datetime
import os

from execicios.extras.mobilidade import MobilidadeOmbro, MobilidadeQuadril, MobilidadeToracica, MobilidadeTornozelo
from execicios.força.mmii import JoelhoBiAssimetrico, JoelhoBiSimetrico, JoelhoUnilateral, QuadrilBiSimetrico, QuadrilUnilateral
from execicios.força.mmss import EmpurrarHorizontal, EmpurrarVertical, PuxarHorizontal, PuxarVertical
from execicios.força.core import AntiHiperextensao, AntiRotacao, AntiFlexaoLateral, Rotacao
from execicios.extras.pliometria import Pliometria
from execicios.extras.outros import FootCore

# Instanciar as classes

mobilidade_tornozelo = MobilidadeTornozelo()
mobilidade_quadril = MobilidadeQuadril()
mobilidade_toracica = MobilidadeToracica()
mobilidade_ombro = MobilidadeOmbro()

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

def formatar_lista_exercicios(nome_treino: str, exercicios: List[str]) -> str:
    """Formata a lista de exercícios em um formato fácil de copiar e colar"""
    resultado = f"\n=== {nome_treino} ===\n"
    for i, exercicio in enumerate(exercicios, 1):
        resultado += f"{i}. {exercicio}\n"
    return resultado

def gerar_exercicios() -> List[str]:
    mobilidade: List[str] = [
        mobilidade_tornozelo.selecionar_aleatorio(),
        mobilidade_quadril.selecionar_aleatorio(),
        mobilidade_toracica.selecionar_aleatorio(),
        mobilidade_ombro.selecionar_aleatorio()
    ]

    random.shuffle(mobilidade)

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

    # Formato original (para compatibilidade)
    print("Mobilidade:", mobilidade)
    print("Treino A:", treino_a)
    print("Treino B:", treino_b)
    
    # Formato formatado para fácil cópia
    print("\n" + "="*50)
    print("FORMATO PARA COPIAR E COLAR")
    print("="*50)
    
    print(formatar_lista_exercicios("MOBILIDADE", mobilidade))
    print(formatar_lista_exercicios("TREINO A", treino_a))
    print(formatar_lista_exercicios("TREINO B", treino_b))
    
    # Versão em texto simples (uma linha por exercício)
    print("\n" + "="*50)
    print("VERSÃO TEXTO SIMPLES")
    print("="*50)
    
    print("\nMOBILIDADE:")
    for exercicio in mobilidade:
        print(f"- {exercicio}")
    
    print("\nTREINO A:")
    for exercicio in treino_a:
        print(f"- {exercicio}")
    
    print("\nTREINO B:")
    for exercicio in treino_b:
        print(f"- {exercicio}")

def gerar_mobilidade():
    """Gera apenas exercícios de mobilidade"""
    mobilidade: List[str] = [
        mobilidade_tornozelo.selecionar_aleatorio(),
        mobilidade_quadril.selecionar_aleatorio(),
        mobilidade_toracica.selecionar_aleatorio(),
        mobilidade_ombro.selecionar_aleatorio()
    ]
    random.shuffle(mobilidade)
    return mobilidade

def gerar_treino_a():
    """Gera apenas o Treino A"""
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
    return treino_a

def gerar_treino_b():
    """Gera apenas o Treino B"""
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
    return treino_b

def imprimir_lista_simples(nome_treino: str, exercicios: List[str]):
    """Imprime uma lista simples para copiar e colar rapidamente"""
    print(f"\n{nome_treino}:")
    for exercicio in exercicios:
        print(exercicio)

def salvar_treino_em_arquivo(nome_arquivo: str, mobilidade: List[str], treino_a: List[str], treino_b: List[str]):
    """Salva os treinos em um arquivo de texto"""
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(formatar_lista_exercicios("MOBILIDADE", mobilidade))
        arquivo.write(formatar_lista_exercicios("TREINO A", treino_a))
        arquivo.write(formatar_lista_exercicios("TREINO B", treino_b))
    print(f"Treino salvo em '{nome_arquivo}'")

def salvar_treino_arquivo(nome_treino: str, exercicios: List[str], nome_arquivo: str = None):
    """Salva o treino em um arquivo de texto"""
    if nome_arquivo is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"treino_{timestamp}.txt"
    
    # Criar diretório 'treinos' se não existir
    treinos_dir = "treinos"
    if not os.path.exists(treinos_dir):
        os.makedirs(treinos_dir)
    
    caminho_arquivo = os.path.join(treinos_dir, nome_arquivo)
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"=== {nome_treino} ===\n")
        arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}\n\n")
        
        for i, exercicio in enumerate(exercicios, 1):
            arquivo.write(f"{i}. {exercicio}\n")
    
    return caminho_arquivo

def salvar_treino_completo_arquivo():
    """Salva um treino completo em arquivo"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"treino_completo_{timestamp}.txt"
    
    # Criar diretório 'treinos' se não existir
    treinos_dir = "treinos"
    if not os.path.exists(treinos_dir):
        os.makedirs(treinos_dir)
    
    caminho_arquivo = os.path.join(treinos_dir, nome_arquivo)
    
    mobilidade = gerar_mobilidade()
    treino_a = gerar_treino_a()
    treino_b = gerar_treino_b()
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("=== TREINO COMPLETO ===\n")
        arquivo.write(f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}\n\n")
        
        arquivo.write("=== MOBILIDADE ===\n")
        for i, exercicio in enumerate(mobilidade, 1):
            arquivo.write(f"{i}. {exercicio}\n")
        
        arquivo.write("\n=== TREINO A ===\n")
        for i, exercicio in enumerate(treino_a, 1):
            arquivo.write(f"{i}. {exercicio}\n")
        
        arquivo.write("\n=== TREINO B ===\n")
        for i, exercicio in enumerate(treino_b, 1):
            arquivo.write(f"{i}. {exercicio}\n")
    
    return caminho_arquivo, mobilidade, treino_a, treino_b

def main():
    """Função principal com opções de geração"""
    while True:
        print("\n=== GERADOR DE TREINOS ===")
        print("1. Gerar treino completo (Mobilidade + Treino A + Treino B)")
        print("2. Gerar apenas Mobilidade")
        print("3. Gerar apenas Treino A")
        print("4. Gerar apenas Treino B")
        print("5. Gerar tudo (formato antigo)")
        print("6. Gerar e salvar treino completo em arquivo")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (0-6): ").strip()
            
            if opcao == "0":
                print("Saindo do gerador de treinos...")
                break
            elif opcao == "1":
                print("\n" + "="*50)
                print("TREINO COMPLETO")
                print("="*50)
                
                mobilidade = gerar_mobilidade()
                treino_a = gerar_treino_a()
                treino_b = gerar_treino_b()
                
                print(formatar_lista_exercicios("MOBILIDADE", mobilidade))
                print(formatar_lista_exercicios("TREINO A", treino_a))
                print(formatar_lista_exercicios("TREINO B", treino_b))
                
                # Perguntar se quer salvar
                salvar = input("\nDeseja salvar este treino em arquivo? (s/n): ").strip().lower()
                if salvar == 's':
                    arquivo, _, _, _ = salvar_treino_completo_arquivo()
                    print(f"✅ Treino salvo em: {arquivo}")
                
            elif opcao == "2":
                mobilidade = gerar_mobilidade()
                print(formatar_lista_exercicios("MOBILIDADE", mobilidade))
                
                # Perguntar se quer salvar
                salvar = input("\nDeseja salvar este treino em arquivo? (s/n): ").strip().lower()
                if salvar == 's':
                    arquivo = salvar_treino_arquivo("MOBILIDADE", mobilidade)
                    print(f"✅ Treino salvo em: {arquivo}")
                
            elif opcao == "3":
                treino_a = gerar_treino_a()
                print(formatar_lista_exercicios("TREINO A", treino_a))
                
                # Perguntar se quer salvar
                salvar = input("\nDeseja salvar este treino em arquivo? (s/n): ").strip().lower()
                if salvar == 's':
                    arquivo = salvar_treino_arquivo("TREINO A", treino_a)
                    print(f"✅ Treino salvo em: {arquivo}")
                
            elif opcao == "4":
                treino_b = gerar_treino_b()
                print(formatar_lista_exercicios("TREINO B", treino_b))
                
                # Perguntar se quer salvar
                salvar = input("\nDeseja salvar este treino em arquivo? (s/n): ").strip().lower()
                if salvar == 's':
                    arquivo = salvar_treino_arquivo("TREINO B", treino_b)
                    print(f"✅ Treino salvo em: {arquivo}")
                
            elif opcao == "5":
                gerar_exercicios()
                
            elif opcao == "6":
                print("\n" + "="*50)
                print("GERANDO E SALVANDO TREINO COMPLETO")
                print("="*50)
                
                arquivo, mobilidade, treino_a, treino_b = salvar_treino_completo_arquivo()
                
                print(formatar_lista_exercicios("MOBILIDADE", mobilidade))
                print(formatar_lista_exercicios("TREINO A", treino_a))
                print(formatar_lista_exercicios("TREINO B", treino_b))
                print(f"\n✅ Treino salvo automaticamente em: {arquivo}")
                
            else:
                print("Opção inválida! Escolha entre 0 e 6.")
                
        except KeyboardInterrupt:
            print("\n\nSaindo do gerador de treinos...")
            break
        except Exception as e:
            print(f"Erro: {e}")
            
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
