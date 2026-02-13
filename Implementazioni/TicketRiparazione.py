from Interfacce.Elettrodomestico import Elettrodomestico

class TicketRiparazione:
    
    def __init__(self, id_ticket: int, elettrodomestico: Elettrodomestico, stato_ticket: str = "aperto"):
        # Assegnazione a variabili private (Incapsulamento)
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = stato_ticket
        self.__note = [] # Inizialmente vuota come da traccia

    # Getter e Setter
    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, nuovo_stato: str):
        self.__stato = nuovo_stato

    def get_note(self):
        return self.__note

    # Metodi operativi
    def aggiungi_nota(self, nota: str):
        """Append della stringa nota alla lista note"""
        if nota:
            self.__note.append(nota)

    def calcola_preventivo(self, *voci_extra) -> float:
        """
        Metodo variadico: usa stima_costo_base() dell'elettrodomestico 
        e somma tutte le voci extra passate come parametri.
        """
        # Polimorfismo: chiama la stima specifica (Lavatrice, Forno, ecc.)
        totale = self.__elettrodomestico.stima_costo_base()
        
        # Somma tutte le voci extra passate (Variadico)
        for costo in voci_extra:
            totale += costo
            
        return totale