class Voiture:
    def __init__(self, marque: str, modele: str, carburant: str, type_carroserie: str, vitesse: int):
        self._marque = marque
        self._modele = modele
        self._carburant = carburant
        self._type_carroserie = type_carroserie
        # il faut utiliser le setter s'il y a une procédure speciale de verification des données avant affectation
        self._vitesse(vitesse)

    def __str__(self):
        return f"Marque: {self._marque}, Modele: {self._modele}, Carburant: {self._carburant}, Carroserie: {self._type_carroserie}, vitesse: {self._vitesse}"
    
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_carburant(self):
        return self._carburant

    def get_type_carroserie(self):
        return self._type_carroserie

    #getter
    def get_vitesse(self) -> int:
        return self._vitesse
    
    #setter
    def set_vitesse(self, vitesse: int):
        if type(vitesse) is not int:
            raise Exception("la vitesse doit être un nombre entier")
        elif vitesse > 220:
            raise Exception("la vitesse max est de 220")
        elif vitesse < -10:
            raise Exception("La vitesse min est de -10")
        self._vitesse = vitesse

    def accelerer(self):
        vitesse = self.vitesse()
        vitesse += 20
        self.set_vitesse(vitesse)

    def ralentir(self):
        vitesse = self.vitesse()
        vitesse -= 20
        self.set_vitesse(vitesse)