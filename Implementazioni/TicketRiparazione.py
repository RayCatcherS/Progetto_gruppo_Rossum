from Interfacce.Elettrodomestico import Elettrodomestico

class TicketRiparazione:
    
    def __init__(self, id_ticket: int, elettrodomestico: Elettrodomestico, stato_ticket:bool, note:list):

        # assegnare a varibili private!
        pass

    # getter and setter

    def aggiungi_nota(self, nota:str):
        
        # append della stringa nota alle lista note
        pass

    def calcola_preventivo(self):

        # chiamata dell'elettrodomestico incapsulato in self.__elettrodomestico.stima_costa_base() per calcolare preventivo
        pass