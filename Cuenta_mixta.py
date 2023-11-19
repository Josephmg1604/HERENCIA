from Cuenta_ahorro import Cuenta_ahorro
from Cuenta_corriente import Cuenta_corriente

class Cuenta_Mixta(Cuenta_ahorro, Cuenta_corriente):
    def _init_(self, numero, nombrePropietario, saldo, interes, TieneChequera, limite: float = None, bono: float = None):
        Cuenta_ahorro._init_(self, numero, nombrePropietario, saldo, interes)
        Cuenta_corriente._init_(self, numero, nombrePropietario, saldo, TieneChequera)
        self._limite = limite
        self._bono = bono

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, nuevo_limite):
        self._limite = nuevo_limite

    @property
    def bono(self):
        return self._limite

    @bono.setter
    def bono(self, nuevo_bono):
        self._bono = nuevo_bono

    def fijar_limite(self, limite):
        self.limite = 10000

    def fijar_bono(self, bono):
        self.bono = 5000

    def credito(self, cantidad):
        if self.saldo <= self.limite:
            self.saldo += cantidad
        else:
            print("El saldo de la cuenta a llegado a su limite")

    def bono(self, bono):
        if self.saldo <= self.limite:
            self.saldo += bono
        else:
            print("El saldo de la cuenta a llegado a su limite")

if __name__=="__main_":
    cuenta_pru = Cuenta_corriente("78954", "Joseph", 3500.00, True)
    print(cuenta_pru)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.credito(754.00)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.debito(356.00)
    cuenta_pru.mostrar_saldo()
    cuenta_pru.pagar_cheque(680.00)
    cuenta_pru.mostrar_saldo()