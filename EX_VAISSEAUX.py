from dataclasses import dataclass, field

@dataclass
class Vaisseau:
    nom: str
    couleur: str
    vitesse: int
    T_A: int  # temps d'accélération
    distance: int = field(default=0)

@dataclass
class Circuit:
    longueur: int
    nb_tours: int

liste_vainceurs = []
def course(vaisseaux, circuit):
    tick = 0
    while len(liste_vainceurs) < len(vaisseaux):
        for v in vaisseaux:
            if tick < v.T_A:
                v.distance = 0
            else:
                v.distance += v.vitesse
        tick += 1
        for v in vaisseaux:
            if v.distance >= circuit.longueur * circuit.nb_tours and v.vitesse != 0:
                liste_vainceurs.append(v.nom)
                v.vitesse = 0

    print("dans la course, voici les gagnants :")
    for v in liste_vainceurs:
        print(v)
    return liste_vainceurs

if __name__ == "__main__":
    v1 = Vaisseau("V1", "Rouge", 10, 2)
    v2 = Vaisseau("V2", "Bleu", 12, 3)
    v3 = Vaisseau("V3", "Vert", 8, 1)
    circuit = Circuit(100, 5)
    course([v1, v2, v3], circuit)