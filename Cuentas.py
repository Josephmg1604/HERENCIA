                            # Elaborado por Joseph Montenegro
class Cuentas_Bancarias:
    def __init__(self, numero=None, nombre=None, saldo: float = 0):
        self._numero = numero
        self._nombre = nombre

        self._saldo = saldo

    def __str__(self):
        return f' Cuentas Bancarias: {self.__dict__.__str__()}'

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def credito(self, valor: float = 0):
        self._saldo = float(self._saldo) + float(valor)
        return self._saldo

    def debito(self, valor: float = 0):
        self._saldo = float(self._saldo) - float(valor)
        return self._saldo

    def mostrar_saldo(self):
        print(self._saldo)
