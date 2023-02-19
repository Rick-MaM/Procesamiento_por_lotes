
class File:

    def __init__(self,name):
        self.file_name = name
        
    def Read(self):
        self.file = open(self.file_name,"r")

        self.line = self.file.readlines()
        self.file.close()

        return self.line

    def create(self):
        new_file = open("Salida.txt","w")
        new_file.close()

    def Edit(self,Date):
        Edit_file = open("Salida.txt","a")
        Edit_file.write(Date)
        Edit_file.close
