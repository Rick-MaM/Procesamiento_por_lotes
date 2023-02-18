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
        
        
    def Hexadecimal_Decimal(self):
        aux = self.IPv6.split(":")
        self.IPv6 = ""
        for i in range(len(aux)):
            self.IPv6 = self.IPv6 + str(int(aux[i],16)) + ":"
        
        print(self.IPv6)
        
       


    def Decimal_Hexadecimal(self):
        pass


