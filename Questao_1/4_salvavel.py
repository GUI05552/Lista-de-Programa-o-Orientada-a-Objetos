from armazenador import Armazenador

class ArmazenadorBanco(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' no banco de dados")
class ArmazenadorNuvem:

    def salvar(self, dado):
        print(f"Salvando '{dado}' na nuvem")
from armazenador import Armazenador

class ArmazenadorBanco(Armazenador):

    def salvar(self, dado):
        print(f"Salvando '{dado}' no banco de dados")
