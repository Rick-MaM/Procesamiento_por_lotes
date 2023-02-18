import Class_Ordenar

class File():

    def __init__(self):
        self.Order = Class_Ordenar.Ordenar()

    def Read(self):
        self.file = open("Este.txt","r")

        self.line = self.file.readlines()
        self.file.close()

    def Format(self):
        i = 0
        number = len(self.line)
        while(i < number):
            
            self.Order.Separete(self.line[i])
            Separacion = self.Order.get_line()
            print(Separacion)
            i += 1
            



file = File()
file.Read()
file.Format()