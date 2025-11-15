# main.py

from gerenciador import GerenciadorDePecas

def simular_producao():
    """
    Simula a produção de diversas peças e as envia para inspeção.
    """
    
    # --- Dados Simulados da Linha de Produção ---
    # Vamos gerar 25 peças para teste, incluindo peças boas,
    # peças ruins (por 1 motivo) e peças ruins (por múltiplos motivos).
    
    pecas_produzidas = [
        # 10 Peças Boas (para encher 1 caixa)
        {'id': 1, 'peso': 100, 'cor': 'azul', 'comprimento': 15},
        {'id': 2, 'peso': 98, 'cor': 'verde', 'comprimento': 12},
        {'id': 3, 'peso': 102, 'cor': 'azul', 'comprimento': 18},
        {'id': 4, 'peso': 100, 'cor': 'azul', 'comprimento': 15},
        {'id': 5, 'peso': 95, 'cor': 'verde', 'comprimento': 10},
        {'id': 6, 'peso': 105, 'cor': 'azul', 'comprimento': 20},
        {'id': 7, 'peso': 99, 'cor': 'verde', 'comprimento': 11},
        {'id': 8, 'peso': 101, 'cor': 'azul', 'comprimento': 14},
        {'id': 9, 'peso': 100, 'cor': 'verde', 'comprimento': 17},
        {'id': 10, 'peso': 103, 'cor': 'azul', 'comprimento': 19},
        
        # 3 Peças Boas (para a segunda caixa)
        {'id': 11, 'peso': 100, 'cor': 'verde', 'comprimento': 15},
        {'id': 12, 'peso': 97, 'cor': 'azul', 'comprimento': 13},
        {'id': 13, 'peso': 102, 'cor': 'verde', 'comprimento': 16},

        # Peças Reprovadas (Peso)
        {'id': 14, 'peso': 90, 'cor': 'azul', 'comprimento': 15}, # Peso baixo
        {'id': 15, 'peso': 110, 'cor': 'verde', 'comprimento': 15}, # Peso alto

        # Peças Reprovadas (Cor)
        {'id': 16, 'peso': 100, 'cor': 'vermelho', 'comprimento': 15}, # Cor errada
        {'id': 17, 'peso': 100, 'cor': 'amarelo', 'comprimento': 15}, # Cor errada

        # Peças Reprovadas (Comprimento)
        {'id': 18, 'peso': 100, 'cor': 'azul', 'comprimento': 5},  # Curta
        {'id': 19, 'peso': 100, 'cor': 'verde', 'comprimento': 25}, # Longa

        # Peças Reprovadas (Múltiplos Motivos)
        {'id': 20, 'peso': 80, 'cor': 'vermelho', 'comprimento': 15}, # Peso e Cor
        {'id': 21, 'peso': 120, 'cor': 'azul', 'comprimento': 30}, # Peso e Comprimento
        {'id': 22, 'peso': 100, 'cor': 'preto', 'comprimento': 40}, # Cor e Comprimento
        {'id': 23, 'peso': 70, 'cor': 'rosa', 'comprimento': 50}, # Todos os 3
    ]

    # --- Início do Processo ---
    print("Iniciando processo de automação da linha de montagem...")
    
    # 1. Inicializa o gerenciador
    # (Capacidade de 10 peças por caixa é o padrão, mas podemos mudar aqui)
    gerenciador = GerenciadorDePecas(capacidade_caixa=10)

    # 2. Processa cada peça
    for peca in pecas_produzidas:
        print(f"--- Inspecionando Peça ID: {peca['id']} ---")
        aprovada, motivos = gerenciador.inspecionar_peca(peca)
        
        if aprovada:
            print(f"  -> Resultado: APROVADA")
        else:
            print(f"  -> Resultado: REPROVADA. Motivos: {', '.join(motivos)}")

    # 3. Gera o relatório final após processar todas as peças
    gerenciador.gerar_relatorio()


# Ponto de entrada do script
if __name__ == "__main__":
    simular_producao()