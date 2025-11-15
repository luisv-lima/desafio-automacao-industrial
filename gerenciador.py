# gerenciador.py

class GerenciadorDePecas:
    """
    Classe para gerenciar a inspeção, aprovação e armazenamento
    de peças em caixas.
    """
    
    def __init__(self, capacidade_caixa=10):
        # --- Critérios de Qualidade ---
        self.PESO_MIN = 95
        self.PESO_MAX = 105
        self.CORES_PERMITIDAS = ['azul', 'verde']
        self.COMPRIMENTO_MIN = 10
        self.COMPRIMENTO_MAX = 20
        
        # --- Controle de Armazenamento ---
        self.capacidade_caixa = capacidade_caixa
        self.caixas_fechadas = []  # Armazena caixas cheias
        self.caixa_atual = []      # Caixa atualmente em enchimento

        # --- Contadores para Relatório ---
        self.total_aprovadas = 0
        self.total_reprovadas = 0
        self.motivos_reprovacao = {
            "Peso": 0,
            "Cor": 0,
            "Comprimento": 0
        }

    def inspecionar_peca(self, peca):
        """
        Recebe um dicionário 'peca' e avalia seus critérios de qualidade.
        Armazena a peça se aprovada ou registra a falha se reprovada.
        """
        motivos_falha = []

        # 1. Avaliar Critérios
        if not (self.PESO_MIN <= peca['peso'] <= self.PESO_MAX):
            motivos_falha.append("Peso")
            
        if peca['cor'].lower() not in self.CORES_PERMITIDAS:
            motivos_falha.append("Cor")
            
        if not (self.COMPRIMENTO_MIN <= peca['comprimento'] <= self.COMPRIMENTO_MAX):
            motivos_falha.append("Comprimento")

        # 2. Tomar Decisão
        if not motivos_falha:
            # APROVADA
            self.total_aprovadas += 1
            self._armazenar_peca(peca)
            return True, None
        else:
            # REPROVADA
            self.total_reprovadas += 1
            # Registra todos os motivos de falha da peça
            for motivo in motivos_falha:
                if motivo in self.motivos_reprovacao:
                    self.motivos_reprovacao[motivo] += 1
            return False, motivos_falha

    def _armazenar_peca(self, peca):
        """
        Método privado para adicionar uma peça aprovada à caixa atual
        e fechar a caixa se ela atingir a capacidade.
        """
        self.caixa_atual.append(peca)
        
        # Verifica se a caixa atual está cheia
        if len(self.caixa_atual) == self.capacidade_caixa:
            self.caixas_fechadas.append(self.caixa_atual)
            self.caixa_atual = []  # Inicia uma nova caixa vazia

    def gerar_relatorio(self):
        """
        Imprime um relatório consolidado da produção.
        """
        print("\n" + "="*40)
        print("    RELATÓRIO FINAL DE PRODUÇÃO E QUALIDADE")
        print("="*40)
        
        print(f"\n📈 Total de Peças Aprovadas: {self.total_aprovadas}")
        print(f"📉 Total de Peças Reprovadas: {self.total_reprovadas}")
        
        print("\n🔍 Detalhamento de Reprovações:")
        if self.total_reprovadas == 0:
            print("   Nenhuma peça reprovada.")
        else:
            for motivo, contagem in self.motivos_reprovacao.items():
                if contagem > 0:
                    print(f"   - {motivo}: {contagem} peças")
                    
        # Calcula o total de caixas usadas
        total_caixas = len(self.caixas_fechadas)
        if len(self.caixa_atual) > 0:
            # Conta a caixa atual, mesmo que incompleta
            total_caixas += 1
            
        print(f"\n📦 Quantidade de Caixas Utilizadas: {total_caixas}")
        print("   - Caixas Fechadas (Completas):", len(self.caixas_fechadas))
        if len(self.caixa_atual) > 0:
            print(f"   - Caixa Atual (Em andamento): {len(self.caixa_atual)} / {self.capacidade_caixa} peças")
        
        print("\n" + "="*40)