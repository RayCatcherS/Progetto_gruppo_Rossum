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
        pass

    def stima_costa_base(self) -> int:
        pass
            

    def set_guasto(self, guasto: str):
        self.__guasto = guasto