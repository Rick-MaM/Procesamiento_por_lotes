import Clase_File
import Class_Ordenar


file = Clase_File.File()
order = Class_Ordenar.Ordenar()

line = file.Read()
result = order.Separete(line[0])
print(result)


