from Implementazioni.Lavatrice import Lavatrice
from Implementazioni.Forno import Forno
from Implementazioni.Frigorifero import Frigorifero
from Implementazioni.Officina import Officina
from Implementazioni.TicketRiparazione import TicketRiparazione


def statistiche_per_tipo( tickets: list[TicketRiparazione]):
    lavatrici = 0
    forni = 0
    frigoriferi = 0

    for ticket in tickets:
        if(type(ticket.get_elettrodomestico()). __name__ == "Lavatrice"):
             lavatrici += 1
        elif(type(ticket.get_elettrodomestico()).__name__ == "Forno"):
            forni += 1
        elif(type(ticket.get_elettrodomestico()).__name__ == "Frigorifero"):
            frigoriferi += 1
    print("Numero di lavatrici: ", lavatrici)
    print("Numero di forni: ", forni)
    print("Numero di frigoriferi: ", frigoriferi)


def main():

    officina = Officina("Officina Da Mario")

    while True: 
        scelta = input("Scegli opzione: 1) Aggiungi ticket, 2) Chiudi ticket, 3) Stampa ticket aperti, 4) totale preventivi 5) mostra statistiche")

        if scelta == '1':
            
            id_ticket = officina.genera_id()

            elettrodomestico = None


            while True:
                scelta_elettr = input("Scegli opzione: 1) Lavatrice, 2) Forno, 3) Frigorifero")
                if scelta_elettr == "1":
                    marca = input("Inserisci marca: ")
                    modello = input("Inserisci modello")
                    anno = int(input("Inserisci anno: "))
                    guasto = input("Inserisci guasto: ")

                    kg = int(input("Inserisci kg della lavatrice: "))
                    giri = int(input("Inserisci giri della lavatrice"))
                    elettrodomestico = Lavatrice(marca, modello, anno, guasto, kg, giri)
                    break
                elif scelta_elettr == "2":
                    marca = input("Inserisci marca: ")
                    modello = input("Inserisci modello")
                    anno = int(input("Inserisci anno: "))
                    guasto = input("Inserisci guasto: ")

                    tipo = input("Inserisci il tipo ventilazione")

                    ventilato = False
                    while True:
                        scelta_ventilato = input("Vuoi che il forno sia ventilato? (s/n)")
                        if scelta_ventilato.lower() == "s":
                            ventilato = True
                            break
                        elif scelta_ventilato.lower() == "n":
                            ventilato = False
                            break
                        else:
                            print("Errore, inserisci")
                    
                    elettrodomestico = Forno(marca, modello, anno, guasto, tipo, ventilato)
                    break
                elif scelta_elettr == "3":
                    marca = input("Inserisci marca: ")
                    modello = input("Inserisci modello")
                    anno = int(input("Inserisci anno: "))
                    guasto = input("Inserisci guasto: ")

                    litri = int(input("Inserisci litri"))
                    freezer = False
                    while True:
                        scelta_ventilato = input("Vuoi che il frigo abbia il freezer? (s/n)")
                        if scelta_ventilato.lower() == "s":
                            freezer = True
                            break
                        elif scelta_ventilato.lower() == "n":
                            freezer = False
                            break
                        else:
                            print("Errore, inserisci")

                    elettrodomestico = Frigorifero(marca, modello, anno, guasto, litri, freezer)
                    break
                else:
                    print("errore scelta eletrodomestico")

            
            ticket = TicketRiparazione(id_ticket, elettrodomestico, True)
            officina.aggiungi_ticket(ticket)

        elif scelta == "2":
            id_ticket = int(input("Inserisci id ticket da chiudere"))
            officina.chiudi_ticket(id_ticket)
        elif scelta == "3":
            officina.stampa_ticket_aperti()
        elif scelta == "4":
            officina.totale_preventivi()
        elif scelta == "5":
            statistiche_per_tipo(officina.get_tickets())

main()

