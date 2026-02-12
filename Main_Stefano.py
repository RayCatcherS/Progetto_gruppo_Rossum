import datetime

class Elettrodomestico():
    def __init__(self, marca: str, modello: str, anno: int, guasto: str):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__guasto = guasto
    
    # getter
    def get_marca(self) -> str:
        return self.__marca  
    
    def get_modello(self) -> str:
        return self.__modello
    
    def get_anno(self) -> int:
        return self.__anno

    def get_guasto(self) -> str:
        return self.__guasto

    # setter
    def set_marca(self, marca: str):
        self.__marca = marca

    def set_modello(self, modello: str):
        self.__modello = modello

    def set_anno(self, anno: int) -> bool:
        # controlla se anno > di anno attuale (system)
        if anno < datetime.datetime.now().year:
            return False
        else:
            self.__anno = anno
            return True

    def descrizione(self) -> str:
        return f"marca: {self.__marca}, modello: {self.__modello}, anno: {self.__anno}, guasto: {self.__guasto}"

    def stima_costa_base(self) -> int:
        costo_base = 100
        return costo_base
            

    def set_guasto(self, guasto: str):
        self.__guasto = guasto


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