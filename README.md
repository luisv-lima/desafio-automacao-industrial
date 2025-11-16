# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Este projeto é um protótipo em Python para um desafio industrial, simulando a automação do controle de qualidade e da logística de armazenamento em uma linha de montagem.

O sistema é capaz de receber dados de peças fabricadas, inspecioná-las automaticamente e gerenciar seu armazenamento em caixas.

---

## ⚙️ Explicação do Funcionamento

O projeto é dividido em dois arquivos principais:

1.  **`gerenciador.py`**:
    * Este arquivo contém a classe `GerenciadorDePecas`, que é o cérebro de toda a operação.
    * Ela armazena os **critérios de qualidade** (regras de negócio):
        * Peso: entre 95g e 105g
        * Cor: "azul" ou "verde"
        * Comprimento: entre 10cm e 20cm
    * Ela também gerencia o **estado do armazenamento**:
        * Controla uma `caixa_atual` que recebe peças aprovadas.
        * Quando a caixa atinge a capacidade (10 peças), ela é "fechada" (movida para a lista `caixas_fechadas`) e uma nova é iniciada.
    * Ela mantém os **contadores** para o relatório final (peças aprovadas, reprovadas e os motivos de reprovação).

2.  **`main.py`**:
    * Este arquivo age como o **simulador da linha de produção**.
    * Ele contém uma lista de peças de teste (`pecas_produzidas`) com dados variados (peças boas, peças com um defeito, peças com múltiplos defeitos).
    * Ele instancia (cria) o `GerenciadorDePecas` e usa um loop `for` para enviar cada peça simulada para o método de inspeção.
    * Ao final, ele chama a função `gerar_relatorio()` para exibir os resultados consolidados.

---

## 🚀 Como Rodar o Programa

Para executar a simulação, siga os passos abaixo.

1.  **Pré-requisitos:**
    * É necessário ter o **Python 3** instalado em sua máquina.

2.  **Clone ou Baixe o Repositório:**
    * Se você tem o Git, clone o repositório:
        ```bash
        git clone [https://github.com/seu-nome-de-usuario/desafio-automacao-industrial.git](https://github.com/seu-nome-de-usuario/desafio-automacao-industrial.git)
        ```
    * (Substitua `seu-nome-de-usuario` pelo seu nome de usuário no GitHub).
    * Caso contrário, baixe o arquivo ZIP do projeto e descompacte-o.

3.  **Navegue até a Pasta:**
    * Abra seu terminal (Prompt de Comando, PowerShell, etc.) e navegue até a pasta do projeto:
        ```bash
        cd caminho/para/desafio_automacao
        ```
        *(Ex: `cd D:\Projetos\desafio_automacao`)*

4.  **Execute o Programa:**
    * Digite o seguinte comando para rodar o `main.py`:
        ```bash
        python main.py
        ```
    * O programa executará a simulação e imprimirá o log de inspeção e o relatório final diretamente no seu terminal.

---

## 📊 Exemplos de Entradas e Saídas

### Entradas

A entrada do sistema não é interativa (o usuário não digita dados). Ela está pré-definida na lista `pecas_produzidas` dentro do arquivo `main.py`.

* **Exemplo de Peça Válida (Será APROVADA):**
    ```python
    {'id': 1, 'peso': 100, 'cor': 'azul', 'comprimento': 15}
    ```

* **Exemplo de Peça Inválida (Será REPROVADA):**
    ```python
    # Peso muito baixo e Cor não permitida
    {'id': 20, 'peso': 80, 'cor': 'vermelho', 'comprimento': 15}
    ```

### Saídas

A saída é o log impresso no terminal, mostrando o resultado de cada inspeção e o relatório consolidado final.

Iniciando processo de automação da linha de montagem... --- Inspecionando Peça ID: 1 --- -> Resultado: APROVADA --- Inspecionando Peça ID: 2 --- -> Resultado: APROVADA ... (logs de todas as peças) ... --- Inspecionando Peça ID: 20 --- -> Resultado: REPROVADA. Motivos: Peso, Cor ... --- Inspecionando Peça ID: 23 --- -> Resultado: REPROVADA. Motivos: Peso, Cor, Comprimento

======================================== RELATÓRIO FINAL DE PRODUÇÃO E QUALIDADE
📈 Total de Peças Aprovadas: 13 📉 Total de Peças Reprovadas: 10

🔍 Detalhamento de Reprovações:

Peso: 5 peças

Cor: 5 peças

Comprimento: 5 peças

📦 Quantidade de Caixas Utilizadas: 2

Caixas Fechadas (Completas): 1

Caixa Atual (Em andamento): 3 / 10 peças

========================================
