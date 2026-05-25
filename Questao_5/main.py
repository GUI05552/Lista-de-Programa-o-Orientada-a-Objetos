from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem

def executar_salvamento_formal(armazenador, dado):
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto, dado):
    objeto.salvar(dado)

arquivo = ArmazenadorArquivo()
banco = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

print("=== Salvamento Formal ===")
executar_salvamento_formal(arquivo, "dados.txt")
executar_salvamento_formal(banco, "usuarios")

print("\n=== Salvamento Flexível ===")
executar_salvamento_flexivel(arquivo, "dados.txt")
executar_salvamento_flexivel(banco, "usuarios")
executar_salvamento_flexivel(nuvem, "backup.zip")
#fiz esse na força do ódio 
