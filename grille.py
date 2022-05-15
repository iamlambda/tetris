class Grille:
    """
    classe representant une grille de tetris
    """

    def __init__(self) -> None:
        """
        initialise la grille avec des 0
        """
        self.grille = [[0 for i in range(10)] for j in range(40)]

    def supprime_ligne(self, ligne: int) -> None:
        """
        supprime une ligne
        """
        for i in range(ligne, 0, -1):
            self.grille[i] = self.grille[i - 1]
        self.grille[0] = [0 for i in range(10)]

    def verifie_ligne(self) -> None:
        """
        verifie si une ligne est completee et la supprime si c'est le cas
        """
        for i in range(40):
            if 0 not in self.grille[i]:
                self.supprime_ligne(i)
