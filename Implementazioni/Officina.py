from Implementazioni.TicketRiparazione import TicketRiparazione

class Officina:

    def __init__(self, nome:str, tickets: list):
        self.__nome = nome
        self.__tickets = tickets
        pass
    

    def aggiungi_tickets(self, ticket: TicketRiparazione):
        self.__tickets.append(ticket)


    def chiudi_ticket(self, id_ticket):
        for ticket in self.__tickets:
            if ticket.get_id_ticket()==id_ticket:
                ticket.set_stato(False)

    def stampa_ticket_aperti(self):
        for ticket in self.__tickets:
            print ('il ticket è:', ticket.get_id_ticket(),' stato:',ticket.get_stato())
        # usare type per otttenere il tipo della classe
       

    def totale_preventivi(self):
        for ticket in self.__tickets:
            somma+=ticket.calcola_preventivo()
            return somma
        # ciclare su tutti i ticket e sommare tutti preventivi di tutti i ticket chiamando calcola_preventivo di ticket
