from Implementazioni.Lavatrice import Lavatrice
from Implementazioni.Forno import Forno
from Implementazioni.Frigorifero import Frigorifero
from Implementazioni.Officina import Officina
from Implementazioni.TicketRiparazione import TicketRiparazione


def statistiche_per_tipo( tickets: list[TicketRiparazione]):
    lavatrici = 0
    forni = 0
    frigoriferi = 0

    for ticket in ticket:
        if(type(ticket).__name__ == "Lavatrice"):
             lavatrici += 1
        elif(type(ticket).__name__ == "Forno"):
            forni += 1
        elif(type(ticket).__name__ == "Frigorifero"):
            frigoriferi += 1
    print("Numero di lavatrici: ", lavatrici)
    print("Numero di forni: ", forni)
    print("Numero di frigoriferi: ", frigoriferi)


def main():

    officina = Officina()
    pass




main()

