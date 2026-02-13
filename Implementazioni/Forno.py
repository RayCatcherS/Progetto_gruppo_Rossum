from Interfacce.Elettrodomestico import Elettrodomestico

alimentazioni = {
    "gas" : 20,
    "corrente" : 50
}

class Forno(Elettrodomestico):
    def __init__(self, marca:str, modello:str, anno:int, guasto:str, tipo_alimentazione:str,ha_ventilato:bool):
        super().__init__(marca, modello,anno, guasto)
        self.__tipo_alimentazione=tipo_alimentazione
        self.__ha_ventilato=ha_ventilato

    def get_venti(self):
        return self.__ha_ventilato

    def get_alio(self):
        return self.__tipo_alimentazione
    
    def set_ali(self, tipo_alimentazione):
        self.__tipo_alimentazione = tipo_alimentazione
    

    def set_venti(self, ha_ventilazione):
        self.__ha_ventilato = ha_ventilazione

    def stima_costa_base(self):
        costo = super().stima_costa_base()

        if self.__tipo_alimentazione == "gas":
            costo = costo + alimentazioni["gas"]
        elif self.__tipo_alimentazione == "corrente":  
            costo = costo + alimentazioni["corrente"] 

        if self.__ha_ventilato:
            costo = costo + 50

        return costo
        