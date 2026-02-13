from Implementazioni.TicketRiparazione import TicketRiparazione

class Officina:

    def __init__(self, nome:str ):
        self.__nome = nome
        self.__tickets: list[TicketRiparazione] = []
        pass
    
    def get_tickets(self) -> list[TicketRiparazione]:
        return self.__tickets

    def aggiungi_ticket(self, ticket: TicketRiparazione):
        self.__tickets.append(ticket)
        print("ticket aggunto")


    def chiudi_ticket(self, id_ticket):
        for ticket in self.__tickets:
            if ticket.get_id_ticket()==id_ticket:
                ticket.set_stato(False)
                break
        print("ticket non trovato")

    def stampa_ticket_aperti(self):
        for ticket in self.__tickets:
            print ('il ticket è:', ticket.get_id_ticket(),' stato: ', ticket.get_stato(), "tipo elettrodomestico: ", type(ticket.get_elettrodomestico()).__name__, ", altre info", ticket.get_elettrodomestico().descrizione())

        # usare type per otttenere il tipo della classe
       

    def totale_preventivi(self):
        somma = 0
        for ticket in self.__tickets:
            somma+=ticket.calcola_preventivo([20, 30, 60, 10])
        return somma
        # ciclare su tutti i ticket e sommare tutti preventivi di tutti i ticket chiamando calcola_preventivo di ticket

    def genera_id(self) -> int:
        return len(self.__tickets) + 1
