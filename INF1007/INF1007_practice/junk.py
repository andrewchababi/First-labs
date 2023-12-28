
    
   
# def new_function(function):
#     def internal_funciton():
#         print("hi")
#         function()
#         print("bye")
#     return internal_funciton()

# #lol = new_function(lol)


# @new_function
# def lol():
#     print("middle")

# lol()



class Matrice:

    num  = 1

    def __init__(self, donnees) -> None:
        self.donnees = donnees
        self.taille = (len(donnees), len(donnees[0]))


    @staticmethod
    def zeros(taille: tuple[int, int]):
        return [[0 for _ in range(taille[1])] for _ in range(taille[0])]
    
    def __add__(self, other):
        return Matrice(donnees=[[self.donnees[i][j] + other.donnees[i][j] for j in range(self.taille[1])] for i in range(self.taille[0])])
    

m1 = Matrice([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m1.num)


class Fib:
    def __init__(self):
        self.premier = 0 
        self.deuxieme = 1



    def fib_iterative(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for _ in range(n - 1):
                self.premier, self.deuxieme = self.deuxieme, self.premier + self.deuxieme
            return self.deuxieme
    

fib =  Fib()

print(fib.fib_iterative(6))


def recursion_fact(x):
    if x>1:
        return x * recursion_fact(x - 1 )
    else:
        return 1
    
print(recursion_fact(3))