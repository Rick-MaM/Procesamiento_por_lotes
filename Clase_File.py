import Class_Ordenar

class File():

    def __init__(self):
        self.Order = Class_Ordenar.Ordenar()

    def Read(self):
        self.file = open("Este.txt","r")

        self.line = self.file.readlines()
        self.file.close()

        return self.line

    def Edit(self):
        pass
            