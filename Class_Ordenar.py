
class Ordenar():

    def __init__(self):
        self.IPv6 = ""
        self.IPv4 = ""
        self.Last_Name = ""

    #Eliminar la basura del archivo    
    def Separete(self,Line):
        name = Line.split(",")
        
        band = False
        self.IPv4 = name[5]
        self.Last_Name = name[2]
        for row in name[0]:
            if (row == "/"):
                band = True
            else:
                if (band):
                    pass
                else:
                    self.IPv6 = self.IPv6 + row
        return 
    
    #Transforma la IPv6 en Decimal            
    def Hexadecimal_Decimal(self):
        aux = self.IPv6.split(":")
        self.IPv6 = ""
        for i in range(len(aux)):
            self.IPv6 = self.IPv6 + str(int(aux[i],16)) + ":"
        return 

    #Transforma la IPv4 en Hexadecimal        
    def Decimal_Hexadecimal(self):
        aux = self.IPv4.split(".")
        self.IPv4 = ""
        for i in range(len(aux)):
            self.IPv4 = self.IPv4 + str(hex(int(aux[i]))) + "."
        return
    


