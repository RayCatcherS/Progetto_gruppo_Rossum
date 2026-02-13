from Interfacce.Elettrodomestico import Elettrodomestico


class Frigorifero(Elettrodomestico): 

    soglia_litri = 100

    def __init__(self, marca: str, modello: str, anno: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno, guasto)
        self.__litri = litri 
        self.__ha_freezer = ha_freezer 

    # riscrittura 
    def stima_costa_base(self) -> int:
        costo = super().stima_costa_base()

        if self.__ha_freezer:
            costo = costo + 50

        if self.soglia_litri < self.__litri:
            costo = costo + 50
        return costo