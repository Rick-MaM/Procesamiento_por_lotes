
class Ordenar():

    def __init__(self):
        self.name = []

    #Eliminar la basura del archivo    
    def Separete(self,Line):
        self.name = Line.split(",")
        self.name.pop(4)
        self.name.pop(3)
        self.name.pop(1)
        
        band = False
        aux = ""
        for row in self.name[0]:
            if (row == "/"):
                band = True
            else:
                if (band):
                    pass
                else:
                    aux = aux + row

        self.name[0] = aux
        
    
    def get_line(self):
        return self.name


