import random


class Piece:
    """
    classe qui represente une piece de tetris
    """

    formes = ["J", "L", "S", "T", "Z", "I", "O"]
    pieces = {
        "J": [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        "L": [
            [0, 0, 2],
            [2, 2, 2],
            [0, 0, 0],
        ],
        "S": [
            [0, 3, 3],
            [3, 3, 0],
            [0, 0, 0],
        ],
        "T": [
            [0, 4, 0],
            [4, 4, 4],
            [0, 0, 0],
        ],
        "Z": [
            [5, 5, 0],
            [0, 5, 5],
            [0, 0, 0],
        ],
        "I": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 6, 6, 6, 6],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        "O": [
            [0, 7, 7],
            [0, 7, 7],
            [0, 0, 0],
        ],
    }
    table_decalages = {
        "JLSTZ": {
            0: [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
            1: [(0, 0), (1, 0), (1, -1), (0, 2), (1, 2)],
            2: [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
            3: [(0, 0), (-1, 0), (-1, -1), (0, 2), (-1, 2)],
        },
        "I": {
            0: [(0, 0), (-1, 0), (2, 0), (-1, 0), (2, 0)],
            1: [(-1, 0), (0, 0), (0, 0), (0, 1), (0, -2)],
            2: [(-1, 1), (1, 1), (-2, 1), (1, 0), (-2, 0)],
            3: [(0, 1), (0, 1), (0, 1), (0, -1), (0, 2)],
        },
        "O": {
            0: [(0, 0)],
            1: [(0, -1)],
            2: [(-1, -1)],
            3: [(-1, 0)],
        },
    }

    def __init__(self, forme, grille) -> None:
        """
        initialise la piece
        """
        # choix aleatoire de la forme
        self.forme = forme if forme else random.choice(self.formes)
        self.piece = self.pieces[self.forme]
        self.table = self.table_decalages[
            "JLSTZ" if self.forme in "JLSTZ" else self.forme
        ]

        self.x, self.y = (2, 18) if self.forme == "I" else (3, 19)
        self.taille = len(self.piece)
        self.etat = 0  # 0 a 3, incremente de 1 dans le sens horaire

        self.grille = grille

    def deplacer(self, dx: int, dy: int) -> None:
        """
        deplace la piece dans la direction indiquee si possible
        """
        self.x += dx
        self.y += dy
        if not self.grille.peut_placer(self):
            self.x -= dx
            self.y -= dy

    def descendre_max(self) -> None:
        """
        descend la piece au max
        """
        while self.grille.peut_placer(self):
            self.y += 1
        self.y -= 1

    def tourner(self, horaire: bool, decalage=True) -> None:
        """
        effectue une rotation de 90 degres dans le sens indique
        """
        etat_initial = self.etat

        # on effectue la rotation
        if horaire:
            self.piece = [
                [self.piece[i][j] for i in range(self.taille - 1, -1, -1)]
                for j in range(self.taille)
            ]
            self.etat = (self.etat + 1) % 4
        else:
            self.piece = [
                [self.piece[i][j] for i in range(self.taille)]
                for j in range(self.taille - 1, -1, -1)
            ]
            self.etat = (self.etat - 1) % 4

        # si on ne doit pas decaler, ou que le decalage fonctionne, on return
        if not decalage or self.decaler(etat_initial, self.etat):
            return

        # sinon on inverse la rotation
        self.tourner(not horaire, False)

    def decaler(self, etat_initial: int, etat_final: int) -> bool:
        """
        teste les kick possibles pour la piece, renvoie True si un kick a ete effectue
        """
        # technique basée sur le guide https://harddrop.com/wiki/SRS
        for i in range(len(self.table[etat_final])):
            # on calcule le kick
            dx = self.table[etat_initial][i][0] - self.table[etat_final][i][0]
            dy = self.table[etat_initial][i][1] - self.table[etat_final][i][1]

            # on teste si le kick est possible
            self.deplacer(dx, -dy)
            if self.grille.peut_placer(self):
                return True
            self.deplacer(-dx, dy)

        return False
