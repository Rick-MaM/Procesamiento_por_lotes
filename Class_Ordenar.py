
class Ordenar:

    def __init__(self,Line):
        self.name = Line.split(",")
        self.IPv6 = self.name[0]
        self.IPv4 = self.name[5]
        self.Last_Name = self.name[2] + " : "

    #Eliminar la basura de IPv6
    def Clean_IPv6(self):
        band = False
        aux = self.IPv6
        self.IPv6 = ""
        for row in aux:
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
            self.IPv6 = self.IPv6 + str(int(aux[i],16)) + " : "
        return 

    #Transforma la IPv4 en Hexadecimal        
    def Decimal_Hexadecimal(self):
        aux = self.IPv4.split(".")
        self.IPv4 = ""
        for i in range(len(aux)):
            self.IPv4 = self.IPv4 + str(hex(int(aux[i]))) + "."
        return
    
    #Limpia el IPv4
    def Clean_Ipv4(self):
        aux =  self.IPv4.split(".")
        self.IPv4 = ""
        for i in range(len(aux)):
            cont = 0
            if i != 0 and i != 4:
                self.IPv4 = self.IPv4 + "."
            for j in aux[i]:
                if (cont == 0 or cont == 1):
                    pass
                else:
                    self.IPv4 = self.IPv4 + j.upper()
                cont += 1
        return 


