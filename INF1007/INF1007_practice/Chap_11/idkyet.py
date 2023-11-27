class Velo:
    def __init__(self, couleur = 'rouge'):
        self.couleur = couleur
        self.position = 0
        
        
    def avance(self):
        self.position += 1
    
    def affiche_position(self):
        print(self.position)
        
        
    @property
    def position(self):
        return self.position
    
    @property.setter
    def position(self, position: int):
        if not isinstance(position, int):
            raise ValueError
        self._position = position

mon_Velo = Velo()

for _ in range(2):
    mon_Velo.avance()
    mon_Velo.affiche_position()
    
    
class Complexe:
    def __init__(self, reel, imaginaire):
        self.r , self.i = reel, imaginaire
    def __add__(self, autre):
        if isinstance(autre, Complexe):
            return Complexe(self.r + autre.r, self.i + autre.i)
        elif isinstance(autre, int):
            return Complexe
        
        
class Matrice:

    # == 
    # *entier
    # abs
    
    def __init__(self, donnees):
        """
        :param donnees: liste de liste
        """
        self.donnees = donnees
        self.taille = (len(self.donnees), len(self.donnees[0]))
        
    def __mul__(self, other):
       if isinstance(other, (int, float)):
            return Matrice([[element*other for element in row] for row in self.donnees])
    """ result_matrice = []
            for row in self.donnees:
                row_result = []
                for element in row:
                    row_result.append(element*other)
                result_matrice.append(row_result) 
            return result_matrice"""
        

    @staticmethod
    def zeros(taille: tuple[int, int]):
        return Matrice(donnees=[[0 for _ in range(taille[1])] for _ in range(taille[0])])

    def __add__(self, other):
        if not isinstance(other, Matrice):
            raise TypeError()
        if len(self.taille) != len(other.taille):
            raise ArithmeticError("Les matrices doivent être de la même taille")
        return Matrice(donnees=[[self.donnees[i][j] + other.donnees[i][j] for j in range(self.taille[1])] for i in range(self.taille[0])])

    def __str__(self):
        affichage = ''
        for l in self.donnees:
            affichage += '\t'.join(str(e) for e in l) + '\n'
        return affichage

        
    
    pass