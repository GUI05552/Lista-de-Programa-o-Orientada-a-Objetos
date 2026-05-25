from boleto import Boleto
from etiqueta import Etiqueta
from relatorio_simples import RelatorioSimples

def processar_impressao(item):
    item.imprimir()

boleto = Boleto("123456", 250)
etiqueta = Etiqueta("Maria", "Rua A, 100")
relatorio = RelatorioSimples("Relatório Financeiro")

processar_impressao(boleto)
processar_impressao(etiqueta)
processar_impressao(relatorio)
