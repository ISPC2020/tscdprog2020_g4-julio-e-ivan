from cliente import Cliente


class Banco(Cliente):
    def __init__(self, base_inicial, contactos):
        super().__init__(contactos)
        self.base_inicial = base_inicial

    def arqueoInicial(self):
        montoInicial = 0
        for contacto in range(len(self.base_inicial)):
            montoInicial += self.base_inicial[contacto]['cantidad']
        return montoInicial

    def arqueoFinal(self):
        montoFinal = 0
        for contacto in range(len(self.contactos)):
            montoFinal += self.contactos[contacto]['cantidad']
        return montoFinal

    def balance(self):
        monto_total = self.arqueoFinal() - self.arqueoInicial()
        print(monto_total)
