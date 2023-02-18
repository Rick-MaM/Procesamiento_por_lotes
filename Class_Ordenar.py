
class Ordenar():

    def __init__(self):
        self.IPv6 = ""
        self.IPv4 = ""
        self.Last_Name = ""

    #Eliminar la basura del archivo    
    def Separete(self,Line):
        name = Line.split(",")
        
        band = False
        self.IPv4 = name[2]
        self.Last_Name = name[5]
        for row in name[0]:
            if (row == "/"):
                band = True
            else:
                if (band):
                    pass
                else:
                    self.IPv6 = self.IPv6 + row
        
        print(self.Last_Name,self.IPv4)
        return self.IPv6

    def Hexadecimal_Decimal(self):
        pass

    def Decimal_Hexadecimal(self):
        pass


