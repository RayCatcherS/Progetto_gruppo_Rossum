from Implementazioni.TicketRiparazione import TicketRiparazione

class Officina:

    def __init__(self, nome:str, tickets: list):
        self.__nome = nome
        self.__tickets = tickets
        pass
    

    def aggiungi_tickets(self, ticket: TicketRiparazione):
        self.__tickets.append(ticket)


    def chiudi_ticket(self, id_ticket):
        # ciclare nei ticket fermarti all'id
        pass

    def stampa_ticket(self):

        # usare type per otttenere il tipo della classe
        pass

    def totale_preventivi(self):
        # ciclare su tutti i ticket e sommare tutti preventivi di tutti i ticket chiamando calcola_preventivo di ticket

        pass