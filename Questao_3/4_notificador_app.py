from notificador import Notificador

class NotificadorApp(Notificador):

    def notificar(self, mensagem):
        print(f"Mensagem no app enviada: {mensagem}")
