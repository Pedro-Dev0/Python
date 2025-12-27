import textwrap
"""
Módulo: automação de banco
Resumo:
Este módulo implementa um pequeno sistema bancário interativo em linha de comando
que permite criar usuários e contas, depositar, sacar, ver extrato e listar contas.
Foi organizado em funções pequenas e reutilizáveis para cada operação e uma função
main() que controla o fluxo principal da aplicação.
Visão geral das estruturas de dados:
- saldo: float — saldo da conta corrente (usado globalmente na simulação por sessão).
- extrato: str — histórico de movimentações formatado em texto.
- numero_saques: int — contador de saques realizados na sessão.
- usuarios: list[dict] — lista de usuários, cada usuário é um dicionário com chaves:
    "nome", "data_nascimento", "cpf", "endereco".
- contas: list[dict] — lista de contas, cada conta é um dicionário com chaves:
    "agencia", "numero_conta", "usuario" (onde "usuario" é um dicionário da lista usuarios).
- constantes: AGENCIA (str), limite (float) por saque, LIMITE_SAQUES (int).
Descrição das funções:
menu()
- Objetivo: apresentar o menu ao usuário e ler a opção escolhida.
- Comportamento: formata uma string com opções (depositar, sacar, extrato, nova conta,
  listar contas, novo usuário, sair) e chama input() para retornar a opção.
- Observação: usa textwrap.dedent para formatação limpa.
depositar(saldo, valor, extrato, /)
- Objetivo: processar um depósito.
- Parâmetros:
    saldo (float): saldo atual;
    valor (float): valor a depositar;
    extrato (str): histórico atual.
- Retorno: tupla (saldo_atualizado, extrato_atualizado).
- Validações:
    - Se valor > 0: atualiza saldo e adiciona linha no extrato.
    - Caso contrário: imprime mensagem de erro e não altera estado.
sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)
- Objetivo: processar um saque com várias regras de validação.
- Parâmetros (nomeados obrigatoriamente devido ao *):
    saldo (float), valor (float), extrato (str),
    limite (float): limite máximo por saque,
    numero_saques (int): saques já efetuados,
    limite_saques (int): máximo de saques permitidos por sessão.
- Retorno: tupla (saldo_atualizado, extrato_atualizado, numero_saques_atualizado).
- Regras de validação, checadas nessa ordem:
    1. excedeu_saldo: valor > saldo -> falha por saldo insuficiente.
    2. excedeu_limite: valor > limite -> falha por exceder limite por saque.
    3. excedeu_saques: numero_saques >= limite_saques -> falha por atingir limite de saques.
    4. valor > 0: executa o saque (debita saldo, registra extrato, incrementa contador).
    5. caso contrário, imprime que o valor é inválido.
- Observação: comportamento idempotente em erro (não altera estado).
exibir_extrato(saldo, /, *, extrato)
- Objetivo: mostrar o extrato atual e o saldo.
- Parâmetros:
    saldo (float) posicional obrigatório;
    extrato (str) argumento nomeado.
- Comportamento:
    - Imprime um cabeçalho, mostra mensagem padrão se não houver movimentações,
      exibe o extrato (se houver) e o saldo formatado com duas casas decimais.
nova_conta(agencia, numero_conta, usuarios)
- Objetivo: criar uma nova conta associada a um usuário existente.
- Fluxo:
    - Pede CPF via input() e usa filtrar_usuario() para localizar o usuário.
    - Se usuário existir: cria e retorna um dicionário de conta com agência,
      número e referência ao usuário; imprime mensagem de sucesso.
    - Se não existir: informa que o usuário não foi encontrado e retorna None.
- Observação: não incrementa numero_conta internamente; isso é tratado no main().
- Objetivo: imprimir informações de todas as contas cadastradas.
- Comportamento:
    - Itera sobre a lista de contas e imprime agência, número da conta e nome do titular
      formatados, separando cada conta com uma linha de "=".
    - Usa textwrap.dedent para limpar indentação da string de exibição.
- Objetivo: criar um novo usuário e adicioná-lo à lista usuarios.
- Fluxo:
    - Solicita CPF e verifica existência com filtrar_usuario().
    - Se já existir usuário com o CPF: informa e retorna sem alterações.
    - Se não existir: solicita nome, data de nascimento e endereço, cria um dicionário
      com as informações e faz append na lista usuarios; imprime mensagem de sucesso.
filtrar_usuario(cpf, usuarios)
- Objetivo: localizar um usuário pelo CPF.
- Retorno: o primeiro dicionário de usuário que coincidir com o CPF ou None.
- Implementação: usa list comprehension para filtrar e retorna o primeiro elemento
  ou None se a lista filtrada estiver vazia.
- Objetivo: função simples para imprimir uma mensagem de despedida.
- Uso: chamada quando o usuário escolhe sair do menu.
- Objetivo: inicializar estado, definir constantes e executar o loop principal do programa.
- Inicializações:
    AGENCIA = "0001", LIMITE_SAQUES = 3, limite = 500 (valor máximo por saque),
    saldo = 0.0, extrato = "", numero_saques = 0, usuarios = [], contas = [],
- Loop principal:
    - Chama menu() para obter a opção do usuário.
    - Para cada opção:
        d: solicita valor, chama depositar() e atualiza saldo/extrato.
        s: solicita valor, chama sacar() com argumentos nomeados e atualiza saldo/extrato/contador.
        e: chama exibir_extrato().
        nc: chama nova_conta(); se retorna conta válida, adiciona em contas e incrementa numero_conta.
        lc: chama listar_contas().
        nu: chama novo_usuario().
        q: chama sair() e encerra o loop (break).
        qualquer outra: imprime "Operação inválida".
- Observação: todas as entradas dependem de input(); o estado é mantido apenas enquanto o programa roda.
Boas práticas e pontos de atenção (análise):
- Separação de responsabilidades: cada função tem uma responsabilidade clara (boa prática).
- Segurança/validações:
    - Conversões diretas com float(input(...)) podem lançar exceção ValueError se o usuário digitar texto inválido; seria ideal tratar exceções.
    - CPF não é validado além da igualdade textual; não há verificação de formato ou duplicidade além do campo.
- Persistência: os dados (usuarios, contas, saldo, extrato) existem somente em memória durante a execução; ao fechar, tudo é perdido.
- Uso de argumentos posicionais (/) e somente-nomeados (*) demonstra controle explícito da API das funções.
- Concorrência/multiplas contas: o modelo atual mantém um único saldo/extrato/numero_saques global por execução, ou seja, não há modelagem de saldos por conta. Para suportar múltiplas contas simultâneas, seria necessário associar saldo/extrato a cada conta (por exemplo, adicionando campos na estrutura de conta).
- Internacionalização/formatação: mensagens e formatação monetária estão em real (R$) fixo; para robustez, usar formatação localizável.
Sugestões de melhorias:
- Tratar exceções de input (ValueError) e validar entradas (CPF, valores negativos, formato de data).
- Mover saldo/extrato para dentro da estrutura de conta para permitir múltiplas contas independentes.
- Persistir dados em arquivo (JSON, CSV ou banco) para manter estado entre execuções.
- Implementar autenticação simples ao operar uma conta (selecionar conta antes de depositar/sacar).
- Adicionar testes unitários para as funções puras (depositar, sacar, filtrar_usuario).
Exemplo de uso típico:
1. escolher "nu" para criar um usuário;
2. escolher "nc" e informar o CPF criado para gerar uma conta;
3. escolher "d" para depositar dinheiro;
4. escolher "s" para sacar, respeitando limites;
5. escolher "e" para ver o extrato;
6. escolher "lc" para listar contas;
7. escolher "q" para sair.
Este docstring destina-se a explicar o propósito, o fluxo e as partes críticas do código de forma clara e prática,
além de apontar limitações e sugestões rápidas de melhoria para tornar o sistema mais robusto e realista.
"""

def menu():
    menu = """\n
    ================ MENU ================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [lc] \tListar Contas
    [nu] \tNovo Usuário
    [q] \tSair 
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def nova_conta(agencia, numero_conta, usuarios):
    print("=== Nova Conta ===")
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("=== Conta criada com sucesso! ===")
        return conta
    print("Usuário não encontrado, fluxo de criação de conta encerrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def sair():
    print("Obrigado por usar nosso sistema bancário. Até logo!")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    limite = 500

    saldo = 0
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            novo_usuario(usuarios)

        elif opcao == "q":
            sair()
            break

        else:
            print("Operação inválida, por favor selecione novamente.")



main()





"""
menu = """
"""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""
"""
=> """

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
"""
"""
while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
"""
"""
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
"""
"""
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

"""