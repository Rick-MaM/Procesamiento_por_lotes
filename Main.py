import Clase_File
import Class_Ordenar
import os
from tqdm.auto import tqdm 

name = "prueba2.txt"

def main():
    file = Clase_File.File(name)

    size = file.size()
    
    for i in tqdm(range(size)):
        line = file.Read()
        order = Class_Ordenar.Ordenar(line[i])
        order.Clean_IPv6()
        order.Hexadecimal_Decimal()
        order.Decimal_Hexadecimal()
        order.Clean_Ipv4()
        Date = order.Last_Name + order.IPv6 + order.IPv4 + "\n"
        
        if os.path.exists(name):
            file.Edit(Date)
        else:
            file.create(Date)

    return 

main()
