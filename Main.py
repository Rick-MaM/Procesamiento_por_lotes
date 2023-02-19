import Clase_File
import Class_Ordenar
import os


def main():
    file = Clase_File.File("Este.txt")
    

    size = file.size()
    
    for i in range(size):
        order = Class_Ordenar.Ordenar()
        line = file.Read()
        order.Separete(line[i])
        order.Hexadecimal_Decimal()
        order.Decimal_Hexadecimal()
        order.Clean_Ipv4()
        Date = order.Last_Name + order.IPv6 + order.IPv4 + "\n"
        print(i)
        
        if os.path.exists("Este.txt"):
            file.Edit(Date)
        else:
            file.create(Date)

    return 

main()
"""
file = Clase_File.File("Este.txt")
line = file.Read()
order = Class_Ordenar.Ordenar()


# Clase Ordenar
result = order.Separete(line[0])
order.Hexadecimal_Decimal()
order.Decimal_Hexadecimal()
order.Clean_Ipv4()
Date = order.Last_Name + order.IPv6 + order.IPv4 + "\n"



#Escribir
file.Edit(Date)
"""


