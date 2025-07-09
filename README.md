# Gerador de Treinos

Este é um gerador de treinos de exercícios que cria rotinas personalizadas de mobilidade, força e exercícios funcionais.

## Funcionalidades

O gerador oferece três tipos principais de treinos:

### 🧘‍♂️ Mobilidade
- Exercícios para tornozelo, quadril, região torácica e ombros
- Focado em aquecimento e preparação para o treino

### 💪 Treino A (Membros Superiores + Core)
- Exercícios de empurrar (horizontal e vertical)
- Exercícios de puxar (horizontal e vertical)
- Exercícios de core (anti-hiperextensão e anti-rotação)

### 🦵 Treino B (Membros Inferiores + Core + Pliometria)
- Exercícios para joelhos (bilateral simétrico, bilateral assimétrico, unilateral)
- Exercícios para quadril (bilateral simétrico, unilateral)
- Exercícios de core (anti-flexão lateral, rotação)
- Exercícios pliométricos
- Exercícios para foot core

## Como usar

1. Execute o arquivo principal:
```bash
python generator.py
```

2. Escolha uma das opções do menu:
   - **1**: Gerar treino completo (Mobilidade + Treino A + Treino B)
   - **2**: Gerar apenas Mobilidade
   - **3**: Gerar apenas Treino A
   - **4**: Gerar apenas Treino B
   - **5**: Gerar tudo (formato antigo)
   - **6**: Gerar e salvar treino completo em arquivo
   - **0**: Sair

3. Os treinos são exibidos em formato numerado e podem ser salvos em arquivos de texto na pasta `treinos/`

## Estrutura do Projeto

```
gerador_de_treinos/
├── generator.py              # Arquivo principal
├── classes/
│   └── ExercicioBase.py     # Classe base para exercícios
├── execicios/
│   ├── extras/
│   │   ├── mobilidade.py    # Exercícios de mobilidade
│   │   ├── outros.py        # Outros exercícios (foot core)
│   │   └── pliometria.py    # Exercícios pliométricos
│   └── força/
│       ├── core.py          # Exercícios de core
│       ├── mmii.py          # Exercícios de membros inferiores
│       └── mmss.py          # Exercícios de membros superiores
└── treinos/                 # Pasta onde são salvos os treinos
```

## Exemplo de Treino Gerado

```
=== MOBILIDADE ===
1. Arqueiro frontal
2. 90/90
3. Gato arrepiado
4. Rotação de ombro com bastão

=== TREINO A ===
1. FLEXÃO FECHADA
2. SUPINO HALTER ALTERNADO
3. BARRA AUSTRALIANA
4. PRESS LANDMINE BILATERAL AJOELHADO
5. REMADA CURVADA
6. PUXADA NA POLIA BILATERAL AJOELHADO
7. PRANCHA VENTRAL SLIDE
8. PALLOF PRESS COM ELÁSTICO POSIÇÃO AJOELHADO

=== TREINO B ===
1. AGACHAMENTO KTB RACK BILATERAL
2. AGACHAMENTO LEVANDO AS MÃOS À FRENTE
3. TERRA UNI HALTER UNILATERAL
4. STIFF
5. CAMINHADA DO FAZENDEIRO COM FLEXÃO DE QUADRIL E KTB BILATERAL
6. PANTU PAREDE
7. CHOP SEMI-AJOELHADO NO CROSS
8. Jump Lateral-Vertical C
9. ELEVAÇÃO/PONTE
```

## Características

- ✅ **Aleatoriedade**: Cada execução gera uma combinação diferente de exercícios
- ✅ **Variedade**: Amplo banco de exercícios para cada categoria
- ✅ **Flexibilidade**: Possibilidade de gerar treinos parciais ou completos
- ✅ **Salvamento**: Opção de salvar treinos em arquivos com timestamp
- ✅ **Formatação clara**: Treinos apresentados em formato fácil de ler e copiar

## Requisitos

- Python 3.6+
- Nenhuma dependência externa necessária

## Contribuição

Para adicionar novos exercícios:

1. Identifique a categoria do exercício
2. Edite o arquivo correspondente em `execicios/`
3. Adicione o exercício na lista apropriada dentro da classe correspondente

## Autor

Criado para facilitar a geração de treinos variados e estruturados.
