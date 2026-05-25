class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        self.midias.append(midia)

    def listar_midias(self):
        for midia in self.midias:
            midia.mostrar_info()
            print("-" * 30)

    def reproduzir_todas(self):
        for midia in self.midias:
            midia.reproduzir()