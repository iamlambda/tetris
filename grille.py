class Grille:
    """
    classe representant une grille de tetris
    """

    def __init__(self) -> None:
        """
        initialise la grille avec des 0
        """
        self.grille = [[0 for i in range(10)] for j in range(40)]

    def supprimer_ligne(self, ligne: int) -> None:
        """
        supprime une ligne
        """
        for i in range(ligne, 0, -1):
            self.grille[i] = self.grille[i - 1]
        self.grille[0] = [0 for i in range(10)]

    def verifier_lignes(self) -> None:
        """
        verifie si une ligne est completee et la supprime si c'est le cas
        """
        for i in range(40):
            if 0 not in self.grille[i]:
                self.supprimer_ligne(i)

    def peut_placer(self, piece) -> bool:
        """
        verifie si une piece peut etre placee sur la grille
        """
        for i in range(piece.taille):
            for j in range(piece.taille):
                if piece.piece[i][j] != 0 and (
                    piece.x + j < 0
                    or piece.x + j > 9
                    or piece.y + i > 39
                    or self.grille[piece.y + i][piece.x + j] != 0
                ):
                    return False
        return True

    def placer(self, piece) -> None:
        """
        place une piece sur la grille
        """
        for i in range(piece.taille):
            for j in range(piece.taille):
                if piece.piece[i][j] != 0:
                    self.grille[piece.y + i][piece.x + j] = piece.piece[i][j]
