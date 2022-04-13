from vehicule import Vehicule

class Voiture(Vehicule):
    """
    Cette classe représxente une voiture
    C'est une classe concrète qui étend (ou herite de) la classe vehicule
    cette classe est destinée à être instanciée
    """

    _acceleration = 20

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, type_carroserie: str,):
        super().__init__(marque,modele,carburant,vitesse)
        self._type_carroserie = type_carroserie
        # il faut utiliser le setter s'il y a une procédure speciale de verification des données avant affectation

    def __str__(self):
        return super().__str__() + f"{self._type_carroserie}"

    def get_type_carroserie(self) -> str:
        return self._type_carroserie