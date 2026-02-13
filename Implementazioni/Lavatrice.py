from Interfacce.Elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno: int, guasto: str, kg: int, giri: int):
        # Passiamo i dati comuni alla classe base Elettrodomestico
        super().__init__(marca, modello, anno, guasto)
        # kg è l'attributo unico e privato della lavatrice
        self.__kg = kg
        self.__giri = giri

    # Getter per i kg
    def get_kg(self) -> int:
        return self.__kg
    
    def get_giri(self) -> int:
        return self.__giri

    # Setter per i kg
    def set_kg(self, kg: int):
        if kg > 0:
            self.__kg = kg

    def set_giri(self, giri: int):
        self.__giri = giri

    # Override Polimorfismo con super()
    def stima_costo_base(self) -> int:
        # Chiamiamo il metodo del padre per avere i 100 euro iniziali
        costo_partenza = super().stima_costa_base() 
        
        # Usiamo il getter per controllare i kg
        if self.get_kg() > 7:
            return costo_partenza + 60.0
        else:
            return costo_partenza + 40.0