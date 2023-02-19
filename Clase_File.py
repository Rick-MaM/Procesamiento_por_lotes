
class File:

    def __init__(self,name):
        self.file_name = name

    def size(self):
        file = open(self.file_name,"r")
        self.size = file.readlines()
        self.size = len(self.size)
        return self.size
        
    def Read(self):
        file = open(self.file_name,"r")

        self.line = file.readlines()
        file.close()

        return self.line

    def create(self,Date):
        new_file = open("Salida.txt","w")
        new_file.write(Date)
        new_file.close()

    def Edit(self,Date):
        Edit_file = open("Salida.txt","a")
        Edit_file.write(Date)
        Edit_file.close
