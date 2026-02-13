from Main_Stefano import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno: int, guasto: str, kg: int):
        # Passiamo i dati comuni alla classe base Elettrodomestico
        super().__init__(marca, modello, anno, guasto)
        self.__kg = kg

    # Getter per i kg
    def get_kg(self) -> int:
        return self.__kg

    # Setter per i kg
    def set_kg(self, kg: int):
        if kg > 0:
            self.__kg = kg

    # Override della descrizione
    def descrizione(self) -> str:
        # Usiamo i getter per tutto: quelli del padre (get_marca) e il tuo (get_kg)
        return f"Lavatrice {self.get_marca()} {self.get_modello()} da {self.get_kg()}kg - Guasto: {self.get_guasto()}"

    # Override Polimorfismo con super()
    def stima_costa_base(self) -> float:
        # Chiamiamo il metodo del padre per avere i 100 euro iniziali
        costo_partenza = super().stima_costa_base() 
        
        # Usiamo il getter per controllare i kg
        if self.get_kg() > 7:
            return costo_partenza + 60.0
        else:
            return costo_partenza + 40.0
        


        class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

    def stima_costo_base(self) -> float:
        costo = super().stima_costo_base()
        if self.__ha_freezer:
            costo += 50.0
        return costo + (self.__litri * 0.1)

class Forno(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno: int, guasto: str, tipo_alimentazione: str, ventilato: bool):
        super().__init__(marca, modello, anno, guasto)
        self.__tipo_alimentazione = tipo_alimentazione # "elettrico" o "gas"
        self.__ventilato = ventilato

    def stima_costo_base(self) -> float:
        costo = super().stima_costo_base()
        if self.__tipo_alimentazione == "gas":
            costo += 30.0
        if self.__ventilato:
            costo += 20.0
        return costo
    


