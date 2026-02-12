import Main_Stefano as ModuloElettrodomestici

class Forno(ModuloElettrodomestici.Elettrodomestico):
    def __init__(self, marca:str, modello:str, anno:int, guasto:str, tipo_alimentazione:str,ha_ventilato:bool):
        super().__init__(marca, modello,anno, guasto)
        self.__tipo_alimentazione=tipo_alimentazione
        self.__ha_ventilato=ha_ventilato
    def get_venti(self):
        super().get_anno()
        print('il forno ha ventilazione:',self.__ha_ventilato)
    def get_alio(self):
        super().get_guasto()
        if self.__guasto=='guasto':
            print('il forno ha alimentazione:',self.__tipo_alimentazione)
   
    def stima_costa_base(self):
        costo = super().stima_costa_base()
        if self.__tipo_alimentazione=='si' or self.__ha_ventilato==True:
            costo+=22
            print(costo)
        elif self.__ha_ventilato==False and self.__tipo_alimentazione=='no':
            costo+=66
            print(costo)
        elif self.__tipo_alimentazione=='si' and self.__ha_ventilato==True:
            costo+=100
            print(costo)
        
    def setali(self, tipo_alimentazione):
        self.__tipo_alimentazione=tipo_alimentazione
        print(self.__tipo_alimentazione)
    

    def set_venti(self, ha_ventilazione):
        self.__ha_ventilato=ha_ventilazione
        print(self.__ha_ventilato)
    
  