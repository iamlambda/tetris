from random import sample
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
        self.nouvelle_grille()
        self.sac = []
        self.nouvelle_piece()
        self.hold = None

        self.score = 0

        self.hold_possible = True

    def afficher(self) -> None:
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
        print("hold:", self.hold)
        print("-" * 20)

    def nouvelle_grille(self) -> None:
        """
        genere une nouvelle grille
        """
        self.grille = Grille()

    def nouvelle_piece(self) -> None:
        """
        genere une nouvelle piece
        """
        # on utilise un sac pour generer les pieces aleatoires
        # on le reremplit avant qu'il y en ai moins de 7 (pour l'affichage des pieces suivantes)
        if len(self.sac) < 7:
            formes = ["J", "L", "S", "T", "Z", "I", "O"]
            self.sac += sample(formes, 7)
        # on prend la premiere piece du sac
        self.piece = Piece(self.sac.pop(0), self.grille)

    def placer_piece(self) -> None:
        """
        place la piece sur la grille
        """
        # on place la piece sur la grille et on supprime des lignes si necessaire
        self.piece.descendre_max()
        self.grille.placer(self.piece)
        self.grille.verifier_lignes()
        # on genere une nouvelle piece
        self.nouvelle_piece()
        if not (self.grille.peut_placer(self.piece)):
            print("perdu")
            exit()
        # on redonne la possibilité de hold
        self.hold_possible = True

    def deplacer_piece(self, direction: str) -> None:
        """
        deplace la piece dans la direction indiquee
        """
        if direction == "gauche":
            self.piece.deplacer(-1, 0)
        elif direction == "droite":
            self.piece.deplacer(1, 0)
        elif direction == "bas":
            self.piece.deplacer(0, 1)

    def tourner_piece(self, horaire: bool) -> None:
        """
        effectue une rotation dans le sens indique (horaire ou non)
        """
        self.piece.tourner(horaire)

    def hold_piece(self) -> None:
        """
        place la forme de la piece dans le hold
        """
        if self.hold_possible:
            if self.hold is None:
                self.hold = self.piece.forme
                self.nouvelle_piece()
            else:
                forme = self.hold
                self.hold = self.piece.forme
                self.piece = Piece(forme, self.grille)
            self.hold_possible = False


if __name__ == "__main__":
    # testing
    tetris = Tetris()
    while True:
        tetris.afficher()

        hold = int(input("0:rien, 1:hold ? "))
        rota = int(input("0:rien, 1:horaire, 2:antihoraire ? "))
        depl = int(input("0:rien, 1:gauche, 2:droite, 3:bas, 4:placer ? "))

        if hold == 1:
            tetris.hold_piece()

        if rota == 1:
            tetris.tourner_piece(True)
        elif rota == 2:
            tetris.tourner_piece(False)

        if depl == 1:
            tetris.deplacer_piece("gauche")
        elif depl == 2:
            tetris.deplacer_piece("droite")
        elif depl == 3:
            tetris.deplacer_piece("bas")
        elif depl == 4:
            tetris.placer_piece()
