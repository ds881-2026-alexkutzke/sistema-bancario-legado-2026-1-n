# Prática 1: Sistema Bancário (Ambiente Sem Restrições)

Este repositório contém o código-base para a primeira etapa da prática de versionamento. O objetivo é demonstrar os riscos de um fluxo de trabalho sem políticas de proteção na branch principal (`main`) e a aplicação de rastreabilidade utilizando GitHub Issues.

## 1. Código-Base Inicial

O repositório já contém o arquivo `conta.py` com a seguinte estrutura:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def obter_saldo(self):
        return self.saldo

```

## 2. Preparação do Ambiente Local

Todos os alunos designados para as tarefas devem clonar o repositório e acessar o diretório do projeto:

```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>

# Acessar a pasta do projeto
cd <NOME_DA_PASTA>

```

## 3. Execução das Tarefas (Commits Diretos)

Neste cenário, não há bloqueios na branch `main`. As alterações serão enviadas diretamente para o ambiente de produção simulado.

### Aluno 1: Alterar validação de saque (Issue #1)

**Objetivo:** Introduzir uma falha lógica na validação de saldo para demonstrar a quebra do sistema.

**Passo 1:** Abra o arquivo `conta.py` e altere o método `sacar`, removendo a validação de limite de saldo.

```python
    def sacar(self, valor):
        if valor > 0: 
            self.saldo -= valor
            return True
        return False

```

**Passo 2:** Execute os comandos abaixo no terminal para registrar e enviar a alteração, fechando a Issue correspondente:

```bash
# Atualizar repositório local
git pull origin main

# Preparar o arquivo modificado
git add conta.py

# Criar o commit associando à Issue 1
git commit -m "feat: altera regra de saque. closes #1"

# Enviar alteração diretamente para a main remota
git push origin main

```

### Aluno 2: Implementar método de transferência (Issue #2)

**Objetivo:** Adicionar uma funcionalidade válida simultaneamente às alterações de outros desenvolvedores.

**Passo 1:** Abra o arquivo `conta.py` e adicione o método `transferir` ao final da classe `ContaBancaria`.

```python
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False

```

**Passo 2:** Execute os comandos de integração:

```bash
# Atualizar repositório local (para baixar as alterações do Aluno 1, se houver)
git pull origin main

# Preparar o arquivo modificado
git add conta.py

# Criar o commit associando à Issue 2
git commit -m "feat: implementa metodo de transferencia. closes #2"

# Enviar alteração diretamente para a main remota
git push origin main

```

## 4. Reversão de Falhas em Produção (Rollback)

Após a injeção do código defeituoso pelo Aluno 1 na branch `main`, a aplicação passará a aceitar saldos negativos. Como não houve revisão de código (Code Review) ou testes automatizados, a correção deve ser feita em caráter de urgência via terminal.

Execute os passos abaixo para reverter a alteração:

```bash
# 1. Identificar o hash do commit problemático
git log --oneline

# 2. Executar a reversão (substitua <hash> pelo ID do commit do Aluno 1)
git revert <hash>

# O editor de texto do terminal será aberto. Salve e feche para confirmar a mensagem de reversão.

# 3. Enviar a correção para a branch remota
git push origin main

```
