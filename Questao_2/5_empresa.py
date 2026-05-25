class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            print("-" * 30)

    def mostrar_folha_pagamento(self):
        for funcionario in self.funcionarios:
            print(f"{funcionario.nome}: R$ {funcionario.calcular_pagamento():.2f}")
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado
from empresa import Empresa

empresa = Empresa("Tech Solutions")

f1 = FuncionarioAssalariado("Ana", "111.111.111-11", 5000)
f2 = FuncionarioHorista("Bruno", "222.222.222-22", 160, 30)
f3 = FuncionarioComissionado("Carlos", "333.333.333-33", 20000, 0.1)

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

empresa.listar_funcionarios()

print("\nFolha de Pagamento:\n")

empresa.mostrar_folha_pagamento()
from funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self):
        return self.total_vendas * self.percentual_comissao
