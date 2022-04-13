from vehicule import Vehicule

class Camion(Vehicule):
    """
    Cette classe représente un camion.
    """
    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int, ptac : float):
        super().__init__(marque,modele,carburant,vitesse)
        # il faut utiliser le setter s'il y a une procédure speciale de verification des données avant affectation
        self.set_ptac(ptac)
        

    def __str__(self):
        return super().__str__()+ f" {self._ptac}"

    def get_ptac(self) -> float:
        return self._ptac

    def set_ptac(self, ptac : float):
        if type(ptac) != float:
            raise Exception("le ptac doit etre un float")

        self._ptac = ptac