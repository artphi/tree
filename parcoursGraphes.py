import sys
class Noeud:
    def __init__(self,no):
        self.__no = no
        self.__listAdj = []
        self.__visite = False

    def getNo(self):
        return self.__no

    def addAdj(self, noeud):
        self.__listAdj.append(noeud)

    def getListAdj(self):
        return(self.__listAdj)

    def getVisite(self):
        return self.__visite

    def setVisite(self):
        self.__visite = True


class ParcoursGraphes:

    def __init__(self):
        self.__listeNoeuds = []

    def generationAdj(self):
        noeud = input("Saisir le no du noeud de depart : ")
        print("\n")
        noeud = Noeud(noeud)
        noeud.setVisite
        listeFIFO = [noeud]
        self.__listeNoeuds.append(noeud)
        while len(listeFIFO) != 0:
            nAT = listeFIFO.pop(0)
            tempAdj = []
            print("Traitement du noeud "+ str(nAT.getNo()) + " : \n")
            nVoisin = input("Saisir le no d'un noeud voisin (0 pour finir) : ")
            while nVoisin != 0:
                visite = False
                for n in self.__listeNoeuds:
                    if n.getNo() == nVoisin:
                        visite = True
                        noeud = n
                if visite != True:
                    noeud = Noeud(nVoisin)
                    tempAdj.append(noeud)
                nAT.addAdj(noeud)
                nVoisin = input("Saisir le no d'un noeud voisin (0 pour finir) : ")
            listeFIFO.extend(tempAdj)
            self.__listeNoeuds.extend(tempAdj)
            print("\n\n")
        

        

    def printAdj(self):
        for n in self.__listeNoeuds:
            sys.stdout.write(str(n.getNo()) + " | ")
            for m in n.getListAdj():
                sys.stdout.write(str(m.getNo()) + " ")
            print("")

    def parcoursLargeur(self):
        tree = ""
        listeFIFO = []
        listeFIFO.append(self.__listeNoeuds[0])
        listeInsere = []
        listeInsere.append(self.__listeNoeuds[0])
        tree = tree + str(listeFIFO[0].getNo()) + "->"
        while len(listeFIFO) != 0:
            listeAdj = []
            tree = tree + "("
            sommet = listeFIFO.pop(0)
            listeAdj = sommet.getListAdj()
            while len(listeAdj) > 0:
                v = listeAdj.pop(0)
                try:
                    listeInsere.index(v)
                except ValueError:
                    tree = tree + str(v.getNo()) + ", "
                    listeFIFO.append(v)
                    listeInsere.append(v)
                
            tree = tree + ")"
        tree = tree + ")"
        print(tree)

    def parcoursProfondeur(self):
        tree = ""
        listeFIFO = []
        listeFIFO.append(self.__listeNoeuds[0])
        listeInsere = []
        listeInsere.append(self.__listeNoeuds[0])
        tree = tree + str(listeFIFO[0].getNo()) + "->"
        while len(listeFIFO) != 0:
            listeAdj = []
            tree = tree + "("
            sommet = listeFIFO.pop(len(listeFIFO)-1)
            listeAdj = sommet.getListAdj()
            while len(listeAdj) > 0:
                v = listeAdj.pop(0)
                try:
                    listeInsere.index(v)
                except ValueError:
                    tree = tree + str(v.getNo()) + ", "
                    listeFIFO.append(v)
                    listeInsere.append(v)
                
            tree = tree + ")"
        tree = tree + ")"
        print(tree)
                    



print("Parcours de graphes")
print("*******************")
parcours = ParcoursGraphes()
parcours.generationAdj()
print("Liste d'adjacences") 
print("******************")
parcours.printAdj()
print("\n")
print("Parcours en Largeur")
print("*******************")
parcours.parcoursLargeur()
parcours.parcoursProfondeur()
