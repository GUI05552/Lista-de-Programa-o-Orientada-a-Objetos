[1_armazenador.py](https://github.com/user-attachments/files/28222666/1_armazenador.py)

from abc import ABC, abstractmethod

class Armazenador(ABC):

    @abstractmethod
    def salvar(self, dado):
        pass
