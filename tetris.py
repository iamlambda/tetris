from grille import Grille
from piece import Piece


class Tetris:
    """
    classe permettant de gerer la mecanique du jeu tetris
    """

    def __init__(self) -> None:
        """
        initialise la grille et la piece
        """
        self.grille = Grille()
        self.piece = Piece(self.grille)
        self.score = 0

    def affiche(self) -> None:
        """
        affiche la grille et la piece (testing)
        """
        print("grille:")
        for i in range(20, 40):
            for j in range(10):
                if (
                    self.piece.x <= j < self.piece.x + self.piece.taille
                    and self.piece.y <= i < self.piece.y + self.piece.taille
                    and self.piece.piece[i - self.piece.y][j - self.piece.x] != 0
                ):
                    print(self.piece.piece[i - self.piece.y][j - self.piece.x], end="")
                else:
                    print(self.grille.grille[i][j], end="")

            print()
        print("-" * 20)

    def placer_piece(self) -> None:
        """
        place la piece sur la grille
        """
        # on place la piece sur la grille et on supprime des lignes si necessaire
        self.piece.descendre_max()
        self.grille.placer(self.piece)
        self.grille.verifier_lignes()
        # on genere une nouvelle piece
        self.piece.nouvelle_piece()
        if not (self.grille.peut_placer(self.piece)):
            print("perdu")
            exit()

    def deplacer(self, direction: str) -> None:
        """
        deplace la piece dans la direction indiquee
        """
        if direction == "gauche":
            self.piece.deplacer(-1, 0)
        elif direction == "droite":
            self.piece.deplacer(1, 0)
        elif direction == "bas":
            self.piece.deplacer(0, 1)

    def tourner(self, horaire: bool) -> None:
        """
        effectue une rotation dans le sens indique (horaire ou non)
        """
        self.piece.tourner(horaire)


if __name__ == "__main__":
    # testing
    tetris = Tetris()
    while True:
        tetris.affiche()
        depl = int(input("0:rien, 1:gauche, 2:droite, 3:bas, 4:placer ?"))
        rota = int(input("0:rien, 1:horaire, 2:antihoraire ?"))

        if depl == 1:
            tetris.deplacer(-1, 0)
        elif depl == 2:
            tetris.deplacer(1, 0)
        elif depl == 3:
            tetris.deplacer(0, 1)
        elif depl == 4:
            tetris.placer_piece()

        if rota == 1:
            tetris.tourner(True)
        elif rota == 2:
            tetris.tourner(False)
